# Referências

## Material-fonte primário

- **Vídeo YouTube:** [Master ALL 7 Levels of Claude Code Memory](https://www.youtube.com/watch?v=OMkdlwZxSt8)
- **Skill Memory Architect:** documento-base que inspirou a estrutura do curso (disponível em `skills/memory-architect/` quando empacotada).

## Documentação oficial Claude Code

- Documentação geral: https://docs.claude.com/en/docs/claude-code
- Hooks (guia oficial): https://docs.claude.com/en/docs/claude-code/hooks
- Skills: https://docs.claude.com/en/docs/claude-code/skills
- Settings: https://docs.claude.com/en/docs/claude-code/settings

## Repositórios citados no vídeo

- **Mem Palace** — sistema de memória com ChromaDB e salience scoring
- **Claudsidian** — integração Obsidian + Claude Code (markdown puro)
- **Mem Zero** — camada de memória vetorial modular

Consulte cada um para ver abordagens alternativas. Este curso é complementar, não substituto.

## Backends usados no curso

- **sqlite-vec:** https://github.com/asg017/sqlite-vec — extensão de vetor para SQLite
- **fastembed:** https://github.com/qdrant/fastembed — embeddings locais
- **Obsidian CLI:** recurso nativo do Obsidian para operar o vault via linha de comando

## LLMs auxiliares

- **Gemini Flash:** usado no lab `gemini-summary` para resumir sessões no SessionEnd.
  Requer `GEMINI_API_KEY`. Alternativas: GPT-4o-mini, Claude Haiku, DeepSeek.

## Leitura complementar

- Ebbinghaus forgetting curve (memória humana) — base teórica do decay.
- Progressive disclosure (UX) — princípio aplicado ao carregamento de memória.
- Attention is all you need (Vaswani et al., 2017) — por que LLMs são stateless.

## Recursos INEMA.CLUB

- Site: https://inema.club
- Outros cursos: formato idêntico, trilhas temáticas em HTML + Tailwind.
