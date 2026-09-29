"""Introduksjonsfoil: matrisen målgruppe × perspektiv."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
U = "5 4"

COLS = [("Kapabilitet", "Hva Dapla gjør mulig"), ("Prosess og flyt", "Hvordan data og arbeid flyter"),
        ("Struktur", "Hva det består av"), ("Ansvar og tilgang", "Hvem eier og får gjøre hva")]
ROWS = [("Orientering", ["Ledere, eksterne og", "samarbeidspartnere"], "Hvorfor og hva?"),
        ("Bruk", ["Statistikere og", "nye brukere"], "Hvordan gjør jeg det?"),
        ("Teknisk", ["Arkitekter, utviklere", "og plattformteamet"], "Hvordan er det bygget?")]
# prioritet: 2 trengs, 1 nyttig, 0 unødvendig ; status: tekst eller None
CELLS = [
    [(2, "Kapabilitetskart", ["Ni kapabiliteter i tre lag,", "uten produktnavn."], "Utkast · 1 + 3 fokus"),
     (1, "Verdikjeden på én side", ["Fra kilde til publisering,", "uten teknikk."], None),
     (1, "Dapla forenklet", ["Hovedbyggeklossene og", "hvordan de henger sammen."], None),
     (2, "Brukere, team og tilgang", ["Tilgang følger teamet,", "ikke personen."], "Utkast · 1 + 4 fokus")],
    [(2, "Jeg vil … og med hva", ["Ni kapabiliteter, med", "verktøyene du bruker."], "Utkast · 1 + 3 fokus"),
     (2, "Slik jobber teamet", ["Fra kildedata til publisering:", "hva du gjør og bruker."], "Utkast · 1 + 5 fokus"),
     (0, "Dekkes av prosess", ["Brukere trenger sjelden", "en egen strukturfigur."], None),
     (2, "Min tilgang", ["Hva jeg ser, hva jeg ikke ser,", "og hvem jeg spør."], "Utkast · 1 figur")],
    [(1, "Kapabilitet → komponent", ["Sporbarhet ned til", "tjenester og teknologi."], None),
     (2, "Tre flyter", ["Dataflyt, kontrollflyt i dag", "og i forslag, endringsflyt."], "Utkast · 4 figurer"),
     (2, "Soner og byggeklosser", ["Hva kjører hvor, og hva", "avhenger av hva."], "Utkast · 1 + 5 fokus"),
     (2, "Grupper og kontoer", ["Hvordan tilgang gis, til", "personer og maskiner."], "Utkast · 1 + 4 fokus")],
]


def prio(f, x, y, p):
    if p == 2:
        f.add(f'<circle cx="{x}" cy="{y}" r="9" fill="{C["ink"]}"/>')
    elif p == 1:
        f.add(f'<circle cx="{x}" cy="{y}" r="8" fill="{C["white"]}" stroke="{C["ink"]}" stroke-width="2.5"/>')
    else:
        f.add(f'<line x1="{x-8}" y1="{y}" x2="{x+8}" y2="{y}" stroke="{C["grey"]}" stroke-width="3"/>')


def build():
    f = Fig(None)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, "Én figur, ett perspektiv, én målgruppe", 46, C["ink"], 700)
    f.text("_", 60, 136, "Slik er den nye serien med Dapla-tegninger organisert", 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, "Introduksjon", 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    f.lines("_", 60, 200, ["Dapla har vært forklart med mange tegninger som blander nivåer, begreper og målgrupper. Den nye serien",
                           "skiller dem. Hver celle under er ett spørsmål for én målgruppe, og hver figur svarer bare på det spørsmålet."],
            19, C["dark"], lh=27)

    # akser
    X0, W0 = 60, 230          # radoverskrifter
    CX, CWd, G = 300, 267, 10  # celler
    YH, HH = 262, 82           # kolonneoverskrift
    RY, RH, RG = 356, 196, 10
    f.text("_", CX, 256, "PERSPEKTIV →", 14, C["grey"], 700)
    f.text("_", X0, 256, "MÅLGRUPPE ↓", 14, C["grey"], 700)
    for j, (h, s) in enumerate(COLS):
        x = CX + j * (CWd + G)
        f.rect("_", x, YH + 6, CWd, HH, C["dark"], C["dark"], 0, 10)
        f.text("_", x + 18, YH + 42, h, 21, C["white"], 700)
        f.text("_", x + 18, YH + 68, s, 15, "#d6e6e5")
    for i, (r, who, q) in enumerate(ROWS):
        y = RY + i * (RH + RG)
        f.rect("_", X0, y, W0, RH, C["tealp"], C["teal"], 1.5, 10)
        f.text("_", X0 + 18, y + 40, r, 23, C["ink"], 700)
        f.lines("_", X0 + 18, y + 72, who, 15, C["dark"], lh=20)
        f.text("_", X0 + 18, y + 170, q, 15, C["green"], 700)
        for j, (p, t, d, st) in enumerate(CELLS[i]):
            x = CX + j * (CWd + G)
            if p == 0:
                f.rect("_", x, y, CWd, RH, "#f3f5f5", "#dfe5e5", 1.5, 10)
            else:
                f.rect("_", x, y, CWd, RH, C["white"], C["dark"] if p == 2 else C["line"], 2 if p == 2 else 1.5, 10)
            prio(f, x + 26, y + 30, p)
            lab = {2: "Trengs", 1: "Nyttig", 0: "Trolig unødvendig"}[p]
            f.text("_", x + 44, y + 36, lab, 14, C["grey"], 700)
            tc = C["ink"] if p else C["grey"]
            f.text("_", x + 18, y + 74, t, 19, tc, 700)
            f.lines("_", x + 18, y + 102, d, 15, C["dark"] if p else C["grey"], lh=21)
            if st:
                f.rect("_", x + 18, y + 150, CWd - 36, 30, C["greenp"], C["green"], 1.5, 15)
                f.text("_", x + CWd / 2, y + 170, st, 14, C["green"], 700, "middle")
            elif p:
                f.rect("_", x + 18, y + 150, CWd - 36, 30, C["white"], C["line"], 1.5, 15, dash=U)
                f.text("_", x + CWd / 2, y + 170, "Ikke laget ennå", 14, C["grey"], 600, "middle")

    # sidepanel: regler
    f.rect("_", 1440, 262, 420, 722, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 306, "Regler for alle figurer", 24, C["ink"], 700)
    rules = [("Oversikt og fokus", ["Én grunnfigur per celle. Fokus-", "varianter framhever deler av den."]),
             ("Faste farger", ["Lilla er team og roller, grønn", "er data, blågrønn er plattform."]),
             ("Status synlig", ["Stiplet er ubekreftet. Forslag", "og målbilder merkes som det."]),
             ("Samme begreper", ["Ingen figur innfører nye navn", "på noe som allerede finnes."]),
             ("Alltid med", ["Tegnforklaring, dato og kilder", "på hver figur."])]
    y = 352
    for i, (h, b) in enumerate(rules):
        f.badge(1485, y - 8, i + 1)
        f.text("_", 1516, y, h, 19, C["ink"], 700)
        f.lines("_", 1516, y + 26, b, 16, C["dark"], lh=22)
        y += 26 + len(b) * 22 + 26

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    prio(f, 70, y - 6, 2); f.text("_", 88, y, "Trengs", 16, C["dark"])
    prio(f, 180, y - 6, 1); f.text("_", 198, y, "Nyttig", 16, C["dark"])
    prio(f, 290, y - 6, 0); f.text("_", 308, y, "Trolig unødvendig", 16, C["dark"])
    f.rect("_", 480, y - 20, 150, 26, C["greenp"], C["green"], 1.5, 13)
    f.text("_", 555, y - 2, "Utkast finnes", 14, C["green"], 700, "middle")
    f.rect("_", 646, y - 20, 150, 26, C["white"], C["line"], 1.5, 13, dash=U)
    f.text("_", 721, y - 2, "Ikke laget ennå", 14, C["grey"], 600, "middle")
    f.text("_", 1860, y, f"Utkast {DATO}", 15, C["grey"], 400, "end")
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "introduksjon-matrise.svg"), "w", encoding="utf-8").write(build().svg())
    print("ok")
