# Lab: palavra-codigo

Experimento que prova empiricamente por que CLAUDE.md é sugestivo e hooks são determinísticos.

## O teste

Coloque uma palavra-código no CLAUDE.md, abra 10 sessões novas e faça a mesma pergunta. Conte quantas respondem certo. Depois faça o mesmo com um SessionStart hook. Compare.

## Arquivos

- `CLAUDE.md` — palavra-código em formato CLAUDE.md padrão
- `prime.md` — mesma palavra em formato de hook
- `hook.sh` — script que retorna `prime.md` como additionalContext
- `settings.json` — config de hook SessionStart
- `run_experiment.sh` — automatiza as 10 rodadas e conta resultados

## Rodando

### Fase A — só CLAUDE.md (baseline)

```bash
cd labs/palavra-codigo
cp CLAUDE.md ./CLAUDE.md   # garantir que esta ai
./run_experiment.sh claude-md
```

### Fase B — com hook SessionStart

```bash
# Instale a config local (só para esta pasta)
mkdir -p .claude && cp settings.json .claude/settings.local.json
./run_experiment.sh hook
```

### Comparar

```bash
./run_experiment.sh compare
```

## Resultado esperado

| Fase | Acertos |
|------|---------|
| A (CLAUDE.md) | 6-8 em 10 |
| B (hook) | 10 em 10 |

## Reproduzir no seu projeto

Substitua a palavra-código por qualquer regra crítica do seu contexto. O padrão vale.
