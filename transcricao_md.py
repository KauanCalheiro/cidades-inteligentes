#!/usr/bin/env python3
"""Converte a transcrição HTML do Google Meet em markdown (tempo + falante)."""
import html
import re
import sys
from pathlib import Path

# ponytail: casa pelos data-timestamp, não pelos nomes de classe (que o Meet ofusca e troca).
# \s* entre as tags porque alguns dumps vêm indentados.
SEG = re.compile(
    r'data-timestamp="\d+"\s*>\s*(\d[\d:]*)</div>\s*'
    r'<div[^>]*data-timestamp="\d+"\s*>(.*?)</div>',
    re.S,
)
SPEAKER = re.compile(r"\(([^)]+)\)\n")


def segments(raw):
    """(tempo, falante, texto) preservando os blocos originais da transcrição."""
    for tempo, bloco in SEG.findall(raw):
        partes = SPEAKER.split(html.unescape(bloco))
        # partes = [antes, falante, texto, falante, texto, ...]
        if len(partes) == 1:  # dump sem marcação de falante
            texto = " ".join(partes[0].split())
            if texto:
                yield tempo.strip(), None, texto
            continue
        atual = None  # une as metades do mesmo falante, sem cruzar o timestamp
        for falante, texto in zip(partes[1::2], partes[2::2]):
            texto = " ".join(texto.split())
            if not texto:
                continue
            if atual and atual[1] == falante:
                atual[2] += " " + texto
            else:
                if atual:
                    yield tuple(atual)
                atual = [tempo.strip(), falante, texto]
        if atual:
            yield tuple(atual)


def to_markdown(raw):
    return "\n\n".join(
        f"**[{t}] {falante}:** {texto}" if falante else f"**[{t}]** {texto}"
        for t, falante, texto in segments(raw)
    )


def demo():
    raw = (
        'data-timestamp="0">0:00</div><div data-timestamp="0">(ANA)\nol&aacute; a</div>'
        'data-timestamp="8000">0:08</div><div data-timestamp="8000">(ANA)\ntodos (BOB)\ne a&#237;</div>'
    )
    assert to_markdown(raw) == (
        "**[0:00] ANA:** olá a\n\n**[0:08] ANA:** todos\n\n**[0:08] BOB:** e aí"
    )
    # dump indentado e sem falante
    indentado = (
        '<div class="QvmvOc" data-timestamp="2800">0:03</div>\n'
        '                    <div class="wyBDIb" data-timestamp="2800">bom dia,\n'
        "                        pessoal</div>"
    )
    assert to_markdown(indentado) == "**[0:03]** bom dia, pessoal"
    assert to_markdown("<div>sem transcrição</div>") == ""


def main(argv):
    if len(argv) != 1 or argv[0] in ("-h", "--help"):
        sys.exit(f"uso: {Path(__file__).name} <caminho/transcricao.html>")

    src = Path(argv[0])
    if not src.is_file():
        sys.exit(f"erro: arquivo não encontrado: {src}")

    md = to_markdown(src.read_text(encoding="utf-8", errors="replace"))
    if not md:
        sys.exit(f"erro: nenhuma fala encontrada em {src} — é mesmo a transcrição do Meet?")

    saida = src.with_suffix(".md")
    saida.write_text(md + "\n", encoding="utf-8")
    print(f"{saida} ({md.count('**[')} falas)")


if __name__ == "__main__":
    demo()
    main(sys.argv[1:])
