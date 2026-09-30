"""Komponenter for presentasjonssekvensen Spørsmål → Konsept → Oversikt → Fokus.

Alle fire bildetypene deler samme geometri: sonene i oversikten ligger på samme sted
i spørsmåls- og konseptfoilen. Da kan seeren følge bildene, og PowerPoint Morph kan
animere overgangen. Se docs/standard.md, avsnittet «Presentasjonssekvens».
"""
from konseptfigurer.fig import C

PT = "#4b2fb0"
SONE = "#e3e9e9"                     # svak, stiplet kontur av en sone i oversikten
PLASS = ("#dcebeb", "#e6f1f1")       # plassholdere for svar som kommer
GREYS = "#b9c5c6"


def topp(f, tittel, undertittel, etikett):
    """Hvit bakgrunn, tittel, undertittel, etikett og skillelinje (samme som i ramme())."""
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, tittel, 46, C["ink"], 700)
    f.text("_", 60, 136, undertittel, 24, C["grey"])
    w = max(170, len(etikett) * 11 + 40)
    f.rect("_", 1860 - w, 62, w, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1860 - w / 2, 89, etikett, 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')


def sone(f, x, y, w, h, r=14):
    """Svak kontur av en sone fra oversikten. Brukes på spørsmålsfoilen."""
    f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" '
          f'stroke="{SONE}" stroke-width="2.5" stroke-dasharray="10 8"/>')


def sporsmal(f, n, x, y, linjer, storrelse=27):
    """Nummerert spørsmål, plassert der svaret kommer i oversikten."""
    f.badge(x - 32, y - 9, n)
    f.lines("_", x, y, linjer, storrelse, C["ink"], 700, "start", lh=round(storrelse * 1.26))


def _panel(f, tittel):
    f.rect("_", 1440, 180, 420, 806, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, tittel, 25, C["ink"], 700)


def plassholderpanel(f, n, tittel="Svarene kommer her"):
    """Panel med nummererte, tomme plassholdere: lover svar uten å gi dem."""
    _panel(f, tittel)
    bredder = [(300, 220), (280, 170), (310, 240), (260, 200), (290, 210)]
    y = 282
    for i in range(n):
        a, b = bredder[i % len(bredder)]
        f.badge(1485, y - 8, i + 1)
        f.rect("_", 1516, y - 22, a, 16, PLASS[0], PLASS[0], 0, 8)
        f.rect("_", 1516, y + 4, b, 12, PLASS[1], PLASS[1], 0, 6)
        f.rect("_", 1516, y + 26, b - 60, 12, PLASS[1], PLASS[1], 0, 6)
        y += 110


def svarpanel(f, svar, regel=None, tittel=None):
    """Konseptfoilens panel. `regel` (liste med linjer) er hovedpoenget i stor skrift,
    `svar` er korte svar (overskrift, én linje) nummerert som spørsmålene."""
    if regel:
        _panel(f, tittel or "Én regel")
        f.lines("_", 1466, 290, regel, 34, PT, 700, lh=44)
        yl = 290 + (len(regel) - 1) * 44 + 42
        f.add(f'<line x1="1466" y1="{yl}" x2="1834" y2="{yl}" stroke="{C["teal"]}" stroke-width="2"/>')
        f.text("_", 1466, yl + 46, "Kort svar", 20, C["grey"], 700)
        y, steg, s1, s2 = yl + 100, 100, 20, 18
    else:
        _panel(f, tittel or "Kort svar")
        y, steg, s1, s2 = 282, 110, 22, 20
    for i, (a, b) in enumerate(svar):
        f.badge(1485, y - 8, i + 1)
        f.text("_", 1516, y, a, s1, C["ink"], 700)
        f.text("_", 1516, y + s1 + 7, b, s2, C["dark"])
        y += steg


def grunnbegreper(f, begreper, bunntekst, innledning="Tre ting å holde øye med:"):
    """Forenklet tegnforklaring for spørsmål og konsept: bare grunnbegrepene.
    begreper: liste av (type, tekst), type = person | team | data | flate | utenfor."""
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    f.text("_", 60, y, innledning, 17, C["grey"], 700)
    x = 60 + len(innledning) * 8.9 + 30
    farger = {"team": (C["purplel"], C["purple"]), "data": (C["greenl"], C["green"]),
              "flate": (C["tealp"], C["dark"]), "utenfor": ("#f3f5f5", GREYS)}
    for type_, tekst in begreper:
        if type_ == "person":
            f.person("_", x, y - 4, 0.45)
            f.text("_", x + 22, y, tekst, 17, C["dark"])
            x += 22 + len(tekst) * 9.6 + 34
        else:
            fi, st = farger[type_]
            f.rect("_", x - 12, y - 20, 24, 24, fi, st, 2, 4)
            f.text("_", x + 22, y, tekst, 17, C["dark"])
            x += 22 + len(tekst) * 9.6 + 42
    f.text("_", 1860, y, bunntekst, 15, C["grey"], 400, "end")
