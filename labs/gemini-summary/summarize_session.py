#!/usr/bin/env python3
"""
summarize_session.py — SessionEnd hook que resume a sessao via Gemini Flash.

Lê o JSONL da sessao, envia para Gemini e grava sumário em:
  - ~/.memory/context.md (atualizacao do contexto critico)
  - ~/.memory/long-term/sessions/YYYY-MM-DD.md (archive)

Requer: GEMINI_API_KEY no env. Fallback silencioso se nao disponivel ou timeout.

Uso (como hook SessionEnd):
    {"hooks": {"SessionEnd": [{"hooks": [{"type":"command","command":"python3 labs/gemini-summary/summarize_session.py"}]}]}}

Input esperado no stdin: JSON do hook com `transcript_path`.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

TIMEOUT_SECONDS = 20
MEMORY_DIR = Path(os.path.expanduser("~/.memory"))


def read_hook_input() -> dict:
    try:
        data = sys.stdin.read()
        return json.loads(data) if data else {}
    except Exception:
        return {}


def load_transcript(path: Path, max_tokens_approx: int = 50_000) -> str:
    """Carrega JSONL e junta mensagens relevantes. Trunca se for gigante."""
    if not path.exists():
        return ""
    lines = []
    total = 0
    for line in path.read_text().splitlines():
        try:
            msg = json.loads(line)
        except Exception:
            continue
        role = msg.get("role")
        content = msg.get("content")
        if not content or role not in ("user", "assistant"):
            continue
        text = content if isinstance(content, str) else json.dumps(content)[:2000]
        lines.append(f"[{role}] {text}")
        total += len(text) // 4  # aproximacao grosseira de tokens
        if total > max_tokens_approx:
            lines.append("[... truncado por tamanho ...]")
            break
    return "\n\n".join(lines)


def call_gemini(prompt: str) -> str:
    """Chama Gemini Flash. Timeout agressivo. Retorna '' se falhar."""
    import urllib.request
    import urllib.error

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return ""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 400}
    }).encode()

    try:
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            out = json.loads(resp.read())
        return out["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as exc:
        sys.stderr.write(f"gemini error: {exc}\n")
        return ""


def build_prompt(transcript: str) -> str:
    return f"""Voce e um assistente que resume sessoes de coding em 150 palavras.

Da transcricao abaixo, extraia:
1. **Projeto ativo:** nome.
2. **Decisoes tomadas:** uma linha cada.
3. **Bloqueios atuais:** se houver.
4. **Proximo passo:** uma acao concreta.

Formato de saida (markdown, max 150 palavras):

## Projeto ativo
...

## Decisoes
- ...

## Bloqueios
- ...

## Proximo passo
...

Transcript:
{transcript}
"""


def update_context(summary: str) -> None:
    ctx = MEMORY_DIR / "context.md"
    ctx.parent.mkdir(parents=True, exist_ok=True)
    header = f"# Contexto critico — atualizado em {datetime.now().isoformat(timespec='minutes')}\n\n"
    ctx.write_text(header + summary + "\n")


def append_session_archive(summary: str) -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    archive = MEMORY_DIR / "long-term" / "sessions" / f"{today}.md"
    archive.parent.mkdir(parents=True, exist_ok=True)
    existing = archive.read_text() if archive.exists() else ""
    archive.write_text(existing + f"\n\n---\n\n## Sessao {datetime.now().isoformat(timespec='minutes')}\n\n{summary}")


def main():
    hook_input = read_hook_input()
    transcript_path = Path(hook_input.get("transcript_path", ""))
    if not transcript_path.exists():
        # Fallback silencioso
        sys.exit(0)

    transcript = load_transcript(transcript_path)
    if not transcript.strip():
        sys.exit(0)

    summary = call_gemini(build_prompt(transcript))
    if not summary:
        sys.exit(0)

    update_context(summary)
    append_session_archive(summary)
    # Nao imprimir additionalContext — e um hook de fim, sem retorno util para Claude


if __name__ == "__main__":
    main()
