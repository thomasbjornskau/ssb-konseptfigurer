"""Bruk × Ansvar og tilgang: «Min tilgang». Én figur, bevisst enkel."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
GREYF = "#f3f5f5"


def build():
    f = Fig(None)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, "Min tilgang på Dapla", 46, C["ink"], 700)
    f.text("_", 60, 136, "Hva du ser, hva du ikke ser, og hvem du spør for å få mer", 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, "Oversikt", 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    # topp: tilgangen følger teamet
    f.rect("_", 60, 180, 1340, 96, C["purplep"], C["purple"], 1.5, 12)
    f.person("_", 112, 234, 0.9)
    f.text("_", 160, 220, "Tilgangen din følger teamet, ikke deg", 22, PT, 700)
    f.text("_", 160, 250, "Når du starter en tjeneste i Dapla Lab, velger du hvilket team du jobber for. Da får du det teamet har tilgang til.", 16, C["dark"])

    W, G, Y, H = 433, 20, 300, 570
    cols = [60, 60 + W + G, 60 + 2 * (W + G)]

    # kolonne 1: dette ser du
    x = cols[0]
    f.rect("_", x, Y, W, H, C["white"], C["green"], 2, 12)
    f.rect("_", x, Y, W, 62, C["green"], C["green"], 0, 12)
    f.rect("_", x, Y + 40, W, 22, C["green"], C["green"], 0, 0)
    f.text("_", x + 24, Y + 41, "Dette ser du", 22, C["white"], 700)
    items = [("greenl", "Produktbøtta i teamet ditt", ["inndata, klargjorte data, statistikk", "og utdata · lese og skrive"]),
             ("greenp", "Delt-bøtter fra andre team", ["det andre team har valgt å dele", "med teamet ditt · kun lese"]),
             ("greenp", "Dapla Felles", ["felles team for alle ansatte", "åpne data og kursmateriell"])]
    yy = Y + 92
    for fill, t, d in items:
        f.cyl("_", x + 24, yy, 64, 70, C[fill], C["green"])
        f.text("_", x + 106, yy + 26, t, 19, C["ink"], 700)
        f.lines("_", x + 106, yy + 52, d, 15, C["dark"], lh=20)
        yy += 150

    # kolonne 2: dette ser du ikke
    x = cols[1]
    f.rect("_", x, Y, W, H, GREYF, "#b9c5c6", 2, 12)
    f.text("_", x + 24, Y + 41, "Dette ser du ikke", 22, C["ink"], 700)
    f.add(f'<line x1="{x}" y1="{Y+62}" x2="{x+W}" y2="{Y+62}" stroke="#b9c5c6" stroke-width="1.5"/>')
    items = [("Kildedata", ["heller ikke i ditt eget team.", "Du møter dataene først som", "inndata, etter Kildomaten."]),
             ("Andre teams produktbøtter", ["bare det de legger i en", "delt-bøtte og deler med deg."]),
             ("Data i team du ikke er med i", ["uansett hvilken seksjon", "du tilhører."])]
    yy = Y + 92
    for t, d in items:
        f.lock("_", x + 34, yy + 4, C["grey"])
        f.text("_", x + 84, yy + 26, t, 19, C["ink"], 700)
        f.lines("_", x + 84, yy + 52, d, 15, C["dark"], lh=20)
        yy += 150

    # kolonne 3: slik får du mer
    x = cols[2]
    f.rect("_", x, Y, W, H, C["white"], C["purple"], 2, 12)
    f.rect("_", x, Y, W, 62, C["purple"], C["purple"], 0, 12)
    f.rect("_", x, Y + 40, W, 22, C["purple"], C["purple"], 0, 0)
    f.text("_", x + 24, Y + 41, "Slik får du mer", 22, C["white"], 700)
    asks = [("Jobbe i et annet team", "Seksjonslederen", "legger deg til i Dapla Ctrl"),
            ("Data fra et annet team", "Eierteamet", "deler via delt-bøtte"),
            ("Se kildedata i klartekst", "Bare data-admins", "tidsavgrenset, med begrunnelse"),
            ("Bli data-admin", "Seksjonslederen", "2–3 per team")]
    yy = Y + 84
    for need, who, how in asks:
        f.text("_", x + 24, yy + 20, need, 18, C["ink"], 700)
        f.rect("_", x + 24, yy + 34, 170, 28, C["purplel"], C["purple"], 1.5, 14)
        f.text("_", x + 109, yy + 53, who, 14, PT, 700, "middle")
        f.text("_", x + 206, yy + 53, how, 14, C["dark"])
        yy += 118
        if need != asks[-1][0]:
            f.add(f'<line x1="{x+24}" y1="{yy-16}" x2="{x+W-24}" y2="{yy-16}" stroke="{C["line"]}" stroke-width="1"/>')

    # bunn
    f.rect("_", 60, 890, 1340, 92, C["white"], C["dark"], 1.5, 12)
    f.text("_", 80, 926, "Tilgang gis aldri direkte til deg som person", 19, C["ink"], 700)
    f.text("_", 80, 956, "Alt går via gruppene i teamet. Når du slutter i et team, forsvinner tilgangen til teamets data.", 16, C["dark"])

    # sidepanel
    f.rect("_", 1440, 180, 420, 802, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, "Tre ting å huske", 25, C["ink"], 700)
    tips = [("Velg riktig team", ["Hvilke data du ser, avhenger av", "teamet du velger når du starter", "en tjeneste i Dapla Lab."]),
            ("Kildedata er skjermet", ["Det daglige arbeidet starter", "fra inndata og videre."]),
            ("Spør riktig person", ["Seksjonslederen om medlemskap.", "Eierteamet om data. Data-admins", "om kildedata."])]
    y = 276
    for i, (h, b) in enumerate(tips):
        f.badge(1485, y - 8, i + 1)
        f.text("_", 1516, y, h, 20, C["ink"], 700)
        f.lines("_", 1516, y + 27, b, 17, C["dark"], lh=23)
        y += 27 + len(b) * 23 + 26
    f.text("_", 1466, 930, "Mer detaljer: se orienterings- og", 15, C["grey"])
    f.text("_", 1466, 952, "teknisk utgave av tilgangsfiguren.", 15, C["grey"])

    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    f.text("_", 1860, 1046, f"Utkast {DATO} · Kilde: manual.dapla.ssb.no", 15, C["grey"], 400, "end")
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "bruk-tilgang-oversikt.svg"), "w", encoding="utf-8").write(build().svg())
    print("ok")
