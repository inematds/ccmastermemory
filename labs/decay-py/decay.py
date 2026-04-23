#!/usr/bin/env python3
"""
decay.py — aplica curva de esquecimento em knowledge/ com salience scoring.

Regras:
  - Dia 0-7: full detail (nada muda)
  - Dia 8-30: comprime para resumo de 50%
  - Dia 31-90: one-liner
  - Dia 90+: arquivado em archive/

Salience: cada memoria tem access_count no frontmatter. decay_delay = base * access_count.
Assim memorias acessadas muito resistem mais.

Uso:
    python3 decay.py ~/.memory/knowledge

Roda cron semanal.
"""

import sys
import re
import shutil
from pathlib import Path
from datetime import datetime, timedelta


AGGRESSIVENESS = {
    "conservador": (14, 60, 180),
    "moderado": (7, 30, 90),
    "agressivo": (3, 14, 45),
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extrai frontmatter YAML simples (chave: valor) do markdown."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = parts[2].lstrip("\n")
    return meta, body


def render(meta: dict, body: str) -> str:
    lines = ["---"]
    for k, v in meta.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines)


def age_in_days(meta: dict) -> int:
    created = meta.get("created") or meta.get("date")
    if not created:
        return 0
    try:
        dt = datetime.fromisoformat(created)
        return (datetime.now() - dt).days
    except ValueError:
        return 0


def salience_factor(meta: dict) -> float:
    try:
        n = int(meta.get("access_count", "0"))
    except ValueError:
        n = 0
    # Cada acesso extra adiciona 20% de resistencia
    return 1.0 + (n * 0.2)


def compress(body: str, target_ratio: float) -> str:
    """Mantem as primeiras N% das linhas (proxy simples para sumarizacao)."""
    lines = [l for l in body.splitlines() if l.strip()]
    keep = max(1, int(len(lines) * target_ratio))
    return "\n".join(lines[:keep])


def one_liner(body: str) -> str:
    lines = [l for l in body.splitlines() if l.strip()]
    return lines[0][:140] if lines else ""


def apply_decay(path: Path, archive_dir: Path, thresholds: tuple[int, int, int]) -> str:
    text = path.read_text()
    meta, body = parse_frontmatter(text)

    age = age_in_days(meta) / salience_factor(meta)
    t_summary, t_oneliner, t_archive = thresholds

    if age >= t_archive:
        archive_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(archive_dir / path.name))
        return "archived"

    if age >= t_oneliner:
        new_body = one_liner(body)
        meta["decay_stage"] = "oneliner"
        path.write_text(render(meta, new_body))
        return "oneliner"

    if age >= t_summary:
        new_body = compress(body, 0.5)
        meta["decay_stage"] = "summary"
        path.write_text(render(meta, new_body))
        return "summary"

    return "kept"


def main():
    if len(sys.argv) < 2:
        print("uso: decay.py <knowledge_dir> [conservador|moderado|agressivo]", file=sys.stderr)
        sys.exit(1)

    knowledge = Path(sys.argv[1]).expanduser()
    mode = sys.argv[2] if len(sys.argv) > 2 else "moderado"
    thresholds = AGGRESSIVENESS.get(mode, AGGRESSIVENESS["moderado"])

    archive = knowledge.parent / "archive"
    counts = {"kept": 0, "summary": 0, "oneliner": 0, "archived": 0}

    for md in list(knowledge.rglob("*.md")):
        if any(x in md.parts for x in ("archive", "promotions")):
            continue
        result = apply_decay(md, archive, thresholds)
        counts[result] += 1

    print(f"Modo: {mode} (thresholds em dias: summary={thresholds[0]} oneliner={thresholds[1]} archive={thresholds[2]})")
    for k, v in counts.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
