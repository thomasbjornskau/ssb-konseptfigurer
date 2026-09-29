"""Standardkomponenter for nye figurer: ramme, forklaringspanel, tegnforklaring, flater, brikker og status.

Alle funksjoner tar en gruppe-id `g`. Figuren nedtoner alt som ikke er i fokus
(Fig(hi={...})), så samme grunnfigur kan gi både oversikt og fokusvarianter.
"""
from konseptfigurer.fig import Fig, C

PT = "#4b2fb0"          # mørk lilla tekst
GREYF = "#f3f5f5"        # bakgrunn for «utenfor»
GREYS = "#b9c5c6"        # strek for «utenfor»
STIPLET = "5 4"          # uavklart / ikke bekreftet
FORSLAG = "7 5"          # forslag / målbilde


def ramme(f, tittel, undertittel, etikett, panel_tittel, punkter, tegnforklaring, dato, status="Utkast til diskusjon, ikke kvalitetssikret", kilde=None):
    """Standard oppsett 1920 × 1080: tittel, undertittel, etikett, forklaringspanel til høyre, tegnforklaring og bunnlinje."""
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, tittel, 46, C["ink"], 700)
    f.text("_", 60, 136, undertittel, 24, C["grey"])
    w = max(170, len(etikett) * 11 + 40)
    f.rect("_", 1860 - w, 62, w, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1860 - w / 2, 89, etikett, 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')
    f.rect("_", 1440, 180, 420, 806, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, panel_tittel, 25, C["ink"], 700)
    y = 276
    for i, (h, linjer) in enumerate(punkter):
        f.badge(1485, y - 8, i + 1)
        f.text("_", 1516, y, h, 20, C["ink"], 700)
        f.lines("_", 1516, y + 27, linjer, 17, C["dark"], lh=23)
        y += 27 + len(linjer) * 23 + 24
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    x = 60
    for type_, tekst in tegnforklaring:
        x = forklaring(f, x, 1046, type_, tekst)
    bunn = f"{dato} · {status}" + (f" · Kilde: {kilde}" if kilde else "")
    f.text("_", 1860, 1046, bunn, 15, C["grey"], 400, "end")


def forklaring(f, x, y, type_, tekst):
    stiler = {"flate": (C["tealp"], C["dark"], None), "data": (C["greenp"], C["green"], None),
              "rolle": (C["purplep"], C["purple"], None), "uavklart": (C["white"], C["grey"], STIPLET),
              "utenfor": (GREYF, GREYS, None), "forslag": (C["white"], C["purple"], FORSLAG)}
    fi, st, da = stiler[type_]
    f.rect("_", x, y - 20, 26, 24, fi, st, 1.8, 5, dash=da)
    f.text("_", x + 36, y, tekst, 16, C["dark"])
    return x + 36 + len(tekst) * 8.6 + 30


def flate(f, g, x, y, w, h, tittel, linjer=(), brikker=(), uavklart=None, stiplet=False):
    """En flate eller tjeneste (blågrønn). `brikker` = det den bærer (grønt)."""
    f.rect(g, x, y, w, h, C["tealp"], C["dark"] if not stiplet else C["grey"], 1.8, 8, dash=STIPLET if stiplet else None)
    f.text(g, x + 14, y + 28, tittel, 18, C["ink"] if not stiplet else C["grey"], 700)
    for i, s in enumerate(linjer):
        f.text(g, x + 14, y + 50 + i * 19, s, 14, C["grey"])
    cx = x + 14
    for b in brikker:
        cx += brikke(f, g, cx, y + h - 34, b) + 8
    if uavklart:
        ww = len(uavklart) * 7 + 22
        f.rect(g, x + w - ww - 10, y + h - 33, ww, 22, C["white"], C["grey"], 1.2, 11, dash=STIPLET)
        f.text(g, x + w - ww / 2 - 10, y + h - 18, uavklart, 12, C["grey"], 600, "middle")


def brikke(f, g, x, y, tekst, type_="data"):
    """Liten pille. type_: data (grønn), uavklart (grå stiplet), rolle (lilla), flate (blågrønn)."""
    w = len(tekst) * 7.2 + 22
    fi, st, tc, da = {"data": (C["greenp"], C["green"], C["green"], None),
                      "uavklart": (C["white"], C["grey"], C["grey"], STIPLET),
                      "rolle": (C["purplep"], C["purple"], PT, None),
                      "flate": (C["tealp"], C["dark"], C["dark"], None)}[type_]
    f.rect(g, x, y, w, 24, fi, st, 1.3, 12, dash=da)
    f.text(g, x + w / 2, y + 17, tekst, 12.5, tc, 700, "middle")
    return w


def status(f, g, x, y, verdi):
    """Statusmarkør: 'finnes', 'arbeid', 'forslag' eller None (ikke vurdert). Gjett aldri status."""
    r = 10
    if verdi == "finnes":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f.col(g, "stroke", C["green"])}"/>')
    elif verdi == "arbeid":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{f.col(g, "stroke", C["green"])}" stroke-width="3"/>')
        f.add(f'<path d="M{x},{y-r} A{r},{r} 0 0 1 {x},{y+r} Z" fill="{f.col(g, "stroke", C["green"])}"/>')
    elif verdi == "forslag":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{f.col(g, "stroke", C["purple"])}" stroke-width="2" stroke-dasharray="4 3"/>')
    else:
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{f.col(g, "stroke", C["grey"])}" stroke-width="1.6" stroke-dasharray="3 2"/>')
        f.text(g, x, y + 5, "?", 12, C["grey"], 700, "middle")
