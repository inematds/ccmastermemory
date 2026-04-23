# 🧠 CC Master Memory

> Curso completo e profundo sobre **injeção de memória em Claude Code via hooks**.
> Formato **INEMA.CLUB** — HTML puro, dark/light, sem build.

---

## O que você vai aprender

Dominar a memória do Claude Code é dominar a sua produtividade. Este curso vai do **problema** (por que Claude esquece) até o **sistema completo** (hooks + camadas + backends), passando por todas as decisões de design que você precisa tomar.

### A grande ideia

- **CLAUDE.md é sugestivo** → acerta 7 em 10 vezes.
- **Hooks são determinísticos** → acerta 10 em 10.

O curso prova isso com experimentos reproduzíveis e ensina você a construir seu próprio sistema de memória sob medida.

---

## Trilhas

| # | Trilha | Cor | Foco |
|---|--------|-----|------|
| **T1** | Por que memória importa | 🟢 Emerald | Fundamento + problema |
| **T2** | Os 7 níveis de memória | 🔵 Blue | Modelo mental em camadas |
| **T3** | Anatomia dos 18 hooks | 🟣 Purple | Ferramental completo |
| **T4** | Os 3 hooks críticos | 🟡 Amber | SessionStart, PreCompact, UserPromptSubmit |
| **T5** | Arquitetura e backends | 🟢 Teal | Camadas, formatos, paradigmas |
| **T6** | Projeto prático + integrações | 🔴 Rose | Construir seu sistema + Gemini/multi-agent |

**Total:** 6 trilhas · 36 módulos · ~24h de conteúdo

---

## Como usar

### Opção 1 — Online (GitHub Pages)

Acesse direto o `index.html` hospedado.

### Opção 2 — Local

```bash
git clone https://github.com/inematds/ccmastermemory.git
cd ccmastermemory
# Abrir index.html no navegador (Chrome, Firefox, Edge)
xdg-open index.html   # Linux
open index.html       # macOS
start index.html      # Windows
```

Não precisa de servidor, build ou dependências. É HTML + Tailwind CDN.

---

## Estrutura

```
ccmastermemory/
├── index.html                     # Landing do curso
├── curso/
│   ├── trilha1/ ... trilha6/     # Trilhas com index + módulos
├── labs/                          # Código dos experimentos
│   ├── palavra-codigo/            # Lab CLAUDE.md vs hook
│   ├── prime-md/                  # Template de identidade
│   ├── context-md/                # Template de contexto crítico
│   ├── promote-py/                # Script de promoção 3-strikes
│   ├── decay-py/                  # Script de decay
│   └── gemini-summary/            # SessionEnd → Gemini Flash
├── exemplos-hooks/                # settings.json de referência
└── docs/                          # Documentação complementar
```

---

## Pré-requisitos

- **Claude Code** instalado (`npm install -g @anthropic-ai/claude-code`)
- Editor de texto (VS Code recomendado)
- Terminal com `bash` ou `zsh`
- Para Trilha 6: Python 3.10+ e (opcional) chave Gemini API

---

## Material-fonte

- Vídeo: [Master ALL 7 Levels of Claude Code Memory](https://www.youtube.com/watch?v=OMkdlwZxSt8)
- Skill: `memory-architect` (derivada)
- Docs oficiais: https://docs.claude.com/en/docs/claude-code

---

## Licença

Conteúdo didático de uso livre para estudo pessoal e institucional.
Contribuições e correções: abra uma issue ou PR.

**INEMA.CLUB** · 2026
