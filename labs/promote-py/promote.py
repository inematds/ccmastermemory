#!/usr/bin/env python3
"""
promote.py — detecta padroes repetidos em knowledge/ e propoe promocao para CLAUDE.md.

Regra: se uma mesma observacao aparece 3+ vezes, vira candidata a regra permanente.
Saida: knowledge/promotions/pending.md com sugestoes. Voce revisa e aprova manualmente.

Uso:
    python3 promote.py ~/.memory/knowledge

Roda como hook SessionEnd ou via cron semanal.
"""

import os
import sys
import re
import hashlib
from collections import Counter
from pathlib import Path
from datetime import datetime


def normalize(text: str) -> str:
    """Reduz a forma canonica para agrupamento aproximado."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s-]", "", text)
    return text[:200]


def extract_observations(knowledge_dir: Path) -> list[tuple[Path, str]]:
    """Le knowledge/**/*.md e retorna lista de (path, first-paragraph-norm)."""
    obs = []
    for md in knowledge_dir.rglob("*.md"):
        if "promotions" in md.parts:
            continue
        try:
            content = md.read_text().strip()
            if not content:
                continue
            first = content.split("\n\n", 1)[0]
            obs.append((md, normalize(first)))
        except Exception:
            continue
    return obs


def find_patterns(observations: list[tuple[Path, str]], threshold: int = 3) -> dict[str, list[Path]]:
    """Agrupa observacoes por forma canonica e retorna clusters com >= threshold."""
    buckets: dict[str, list[Path]] = {}
    for path, norm in observations:
        buckets.setdefault(norm, []).append(path)
    return {k: v for k, v in buckets.items() if len(v) >= threshold}


def write_proposals(patterns: dict[str, list[Path]], output: Path) -> int:
    """Gera arquivo de sugestoes para revisao humana."""
    if not patterns:
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Promocoes pendentes",
        "",
        f"> Gerado em {datetime.now().isoformat(timespec='seconds')}",
        "> Cada item e um cluster de observacoes repetidas. Revise e decida se vira regra em CLAUDE.md.",
        "",
    ]
    for i, (norm, paths) in enumerate(patterns.items(), start=1):
        lines.append(f"## Proposta {i} ({len(paths)} ocorrencias)")
        lines.append("")
        lines.append(f"Padrao detectado: {norm[:150]}")
        lines.append("")
        lines.append("Origens:")
        for p in paths:
            lines.append(f"- {p}")
        lines.append("")
        lines.append("Regra sugerida (edite antes de aprovar):")
        lines.append("")
        lines.append("```")
        lines.append(f"Sempre [acao] quando [condicao].")
        lines.append("```")
        lines.append("")
    output.write_text("\n".join(lines))
    return len(patterns)


def main():
    if len(sys.argv) < 2:
        print("uso: promote.py <knowledge_dir>", file=sys.stderr)
        sys.exit(1)

    knowledge = Path(sys.argv[1]).expanduser()
    if not knowledge.exists():
        print(f"Pasta nao existe: {knowledge}", file=sys.stderr)
        sys.exit(1)

    observations = extract_observations(knowledge)
    patterns = find_patterns(observations, threshold=3)
    output = knowledge / "promotions" / "pending.md"
    count = write_proposals(patterns, output)

    print(f"Observacoes analisadas: {len(observations)}")
    print(f"Padroes detectados (3+ ocorrencias): {count}")
    if count:
        print(f"Revisar em: {output}")


if __name__ == "__main__":
    main()
