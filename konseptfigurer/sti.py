"""Felles stier: alle figurer skrives til utdata/<serie>/ i repoet."""
import os

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def utdata(serie):
    d = os.path.join(ROT, "utdata", serie)
    os.makedirs(d, exist_ok=True)
    return d
