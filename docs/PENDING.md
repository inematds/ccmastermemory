# Status do curso — PENDING.md

## O que está COMPLETO ✅

### Landing e README
- `index.html` — landing com hero, grande ideia (CLAUDE.md vs hooks), 6 cards de trilha, metodologia
- `README.md` — visão geral, estrutura, como usar, pré-requisitos

### Trilhas (6 índices + 36 módulos)
Todas as 6 trilhas estão com **navegação completa** (índice + 6 módulos cada):

| Trilha | Cor | Status |
|--------|-----|--------|
| T1 Por que memória importa | Emerald | ✅ Índice + 6 módulos **detalhados** |
| T2 Os 7 níveis | Blue | ✅ Índice detalhado + 6 módulos placeholder |
| T3 Anatomia dos 18 hooks | Purple | ✅ Índice detalhado + 6 módulos placeholder |
| T4 Os 3 hooks críticos | Amber | ✅ Índice detalhado + 6 módulos placeholder |
| T5 Arquitetura e backends | Teal | ✅ Índice detalhado + 6 módulos placeholder |
| T6 Projeto prático | Rose | ✅ Índice detalhado + 6 módulos placeholder |

**Todos os índices têm conteúdo rico**: 6 módulos × 6 tópicos × 3 seções (O que é / Por que / Conceitos-chave) = 108 blocos de conteúdo por trilha.

### Labs (código executável)
- `labs/palavra-codigo/` — experimento A/B CLAUDE.md vs hook + settings.json + hook.sh
- `labs/prime-md/` — template de identidade
- `labs/context-md/` — template de contexto crítico
- `labs/promote-py/promote.py` — detector 3-strikes funcional
- `labs/decay-py/decay.py` — decay com salience scoring funcional
- `labs/gemini-summary/summarize_session.py` — SessionEnd + Gemini Flash funcional

### Exemplos de configuração
- `exemplos-hooks/completo-final.json` — settings.json completo com SessionStart + PreCompact + UserPromptSubmit + SessionEnd

---

## O que está PENDENTE 🚧

### Módulos detalhados (Trilhas 2–6)
Os 30 módulos de T2–T6 estão atualmente em formato **placeholder**: cada um tem a navegação padrão, breadcrumb, header completo, lista dos 6 tópicos e uma nota indicando que o conteúdo detalhado (boxes ricos, diagramas ASCII, casos comparativos) está no índice da trilha e será adicionado em releases futuros.

**O que falta ser escrito em cada módulo:**
- 6 seções ricas (uma por tópico) com:
  - Box de "Conceito principal" (gradiente da cor da trilha)
  - Box de "Dados/Pesquisa" (blue) quando aplicável
  - Box de "Dica prática" (primary/yellow)
  - Grid "O que fazer / O que NÃO fazer" (emerald/red)
  - Timeline de passos (quando didaticamente útil)
  - Box de alerta (red) para armadilhas
- Resumo final com checklist de pontos aprendidos

**Estimativa:** ~500 linhas HTML por módulo × 30 módulos = ~15k linhas.

### Skill empacotada
- `skills/memory-architect/` — versão adaptada do `memorydesigner.md` original, empacotada como skill Claude Code instalável.

### Documentação complementar
- `docs/glossario.md` — termos técnicos usados no curso
- `docs/referencias.md` — vídeo fonte, repos citados, leitura extra
- `docs/roadmap.md` — releases futuros planejados

---

## Como completar o restante

### Opção 1 — incremental (recomendada)
Rodar sessões focadas: uma trilha por vez, cada módulo detalhado de uma vez. Commit a cada módulo. Em ~5–6 sessões de ~1h cada, completa T2–T6.

### Opção 2 — sub-agente em paralelo
Spawnar agente `general-purpose` para cada trilha, com template do `modulo-1-1.html` como referência. Revisar e ajustar.

### Opção 3 — usuário escreve, Claude revisa
Escreva o conteúdo em markdown simples, Claude converte para o template HTML e aplica skill `revisar-curso`.

---

## Estado no GitHub

Tudo que está neste estado foi empurrado para:
https://github.com/inematds/ccmastermemory

Commits principais:
1. `feat: landing + README + Trilha 1 completa` — estrutura inicial e pilot
2. `feat: Trilha 2 index (Os 7 niveis)` — blue
3. `feat: Trilhas 3-6 indexes` — purple, amber, teal, rose
4. `feat: labs + placeholder modules + docs` — este estado

O site é navegável, todas as trilhas respondem, todos os "Ver Completo" funcionam (abrem os placeholders). Nenhum link quebrado.
