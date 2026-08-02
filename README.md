# Cidades Inteligentes

Anotações e materiais da disciplina, uma pasta por aula (`aula-01/`, `aula-02/`, ...).

## Transcrições

`transcricao_md.py` converte a transcrição HTML do Google Meet em markdown, mantendo
tempo e falante e descartando todo o wrapper HTML.

### Como salvar o HTML

No Meet (ou na gravação), abra o painel **Transcrição**, clique com o botão direito na
barra lateral → **Inspecionar** → botão direito no `<div>` da barra lateral →
**Copy → Copy outerHTML** e cole em `aula-XX/transcricao.html`.

### Como executar

```bash
python3 transcricao_md.py aula-01/transcricao.html
```

Gera `aula-01/transcricao.md` ao lado do HTML (sobrescreve se já existir):

```markdown
**[0:00] EDSON MOACIR AHLERT:** para assistir depois gravando. Então, pessoal...
```

Cada bloco do markdown corresponde a um trecho da transcrição original (um timestamp).
Se dois falantes aparecem no mesmo trecho, viram dois blocos com o mesmo tempo.

Sem dependências — Python 3 puro. O script roda um autoteste (`demo()`) antes de
converter; se o Meet mudar o formato, ele falha com erro claro em vez de gerar
um arquivo vazio.
