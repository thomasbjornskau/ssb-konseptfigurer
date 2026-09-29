"""Bruk × Prosess og flyt: «Slik jobber teamet».
Samme kolonner (datatilstander) som den tekniske prosessfiguren, men radene er
brukerens spørsmål: hva skjer, hva gjør jeg, hvilke verktøy, hva dokumenterer jeg."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
U = "5 4"
GREYF = "#f3f5f5"
LX, X0, CW = 60, 240, 165
def cx(j): return X0 + CW * j + CW / 2
COLS = ["Innhenting", "Kildedata", "Inndata", "Klargjorte", "Statistikk", "Utdata", "Formidling"]
STATE = [0, 1, 1, 1, 1, 1, 0]
R1, R2, R3, R4 = (300, 104), (414, 150), (574, 150), (734, 132)
ROWS = [("Hva skjer", "med dataene", R1), ("Hva du gjør", "og hvem", R2), ("Verktøy", "", R3), ("Dokumentasjon", "påkrevd", R4)]


def cell(f, g, j, y, h, span=1, fill=None, stroke=None, dash=None):
    f.rect(g, X0 + CW * j + 4, y, CW * span - 8, h, fill or C["white"], stroke or C["line"], 1.5, 8, dash=dash)


def chip(f, g, x, y, w, label, kind="tool"):
    styles = {"tool": (C["white"], C["dark"], C["dark"]), "dev": (C["purplel"], C["purple"], PT),
              "da": (C["white"], C["purple"], PT), "none": (C["white"], C["grey"], C["grey"]),
              "full": (C["green"], C["green"], C["white"]), "min": (C["greenl"], C["green"], C["ink"]),
              "no": (C["white"], C["line"], C["grey"])}
    fi, st, tc = styles[kind]
    f.rect(g, x, y, w, 26, fi, st, 1.5, 13, dash=U if kind in ("none", "no") else None)
    f.text(g, x + w / 2, y + 18, label, 13, tc, 700, "middle")


def base(f):
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    # Før du starter
    g = "pre"
    f.rect(g, 60, 176, 1340, 58, C["purplep"], C["purple"], 1.5, 10)
    f.text(g, 80, 211, "Før du starter", 18, PT, 700)
    steps = ["Bli medlem av et Dapla-team", "Lag et ssb-project med kode i GitHub", "Start en tjeneste i Dapla Lab med teamet ditt"]
    xs = [250, 580, 950]
    for k, (x, s) in enumerate(zip(xs, steps)):
        f.badge(x + 14, 205, k + 1) if f.on(g) else f.add(f'<circle cx="{x+14}" cy="205" r="15" fill="{DIMC}"/>')
        f.text(g, x + 40, 211, s, 16, C["ink"], 600)

    # kolonneoverskrifter
    for j, n in enumerate(COLS):
        x = X0 + CW * j
        if STATE[j]:
            f.rect("_", x + 6, 250, CW - 12, 36, C["greenp"], C["green"], 1.5, 18)
            f.text("_", cx(j), 274, n, 15, C["green"], 700, "middle")
        else:
            f.text("_", cx(j), 274, n, 15, C["grey"], 700, "middle")
    f.text("_", LX, 274, "Datatilstand →", 15, C["grey"], 700)
    for lab, sub, (y, h) in ROWS:
        f.rect("_", LX, y, 170, h, C["tealp"], C["teal"], 1.5, 8)
        f.text("_", LX + 14, y + 30, lab, 17, C["ink"], 700)
        if sub:
            f.text("_", LX + 14, y + 52, sub, 14, C["grey"])

    # ---- Rad 1: hva skjer ----
    y, h = R1
    r1 = [["Data kommer inn", "fra Altinn, registre", "eller on-prem"], ["Lagres urørt", "i kildebøtta"],
          ["Pseudonymisert", "og standardisert"], ["Editert, koblet", "og kontrollert"], ["Aggregert", "og beregnet"],
          ["Tilpasset for", "publisering og", "konfidensialitet"], ["Publisert eller", "delt med andre"]]
    for j, t in enumerate(r1):
        g = f"c{j}"
        fill = C["green"] if j == 1 else (C["greenl"] if STATE[j] else C["white"])
        tc = C["white"] if j == 1 else C["ink"]
        cell(f, g, j, y, h, fill=fill, stroke=C["green"] if STATE[j] else C["line"])
        f.lines(g, cx(j), y + 36 + (3 - len(t)) * 10, t, 14, tc, 600, "middle", 19)
    # piler mellom tilstander
    for j in range(6):
        g = f"c{j+1}"
        xa = X0 + CW * (j + 1)
        f.add(f'<polygon points="{xa-5},{y+h/2-8} {xa+5},{y+h/2} {xa-5},{y+h/2+8}" fill="{f.col(g,"stroke",C["green"])}"/>')

    # ---- Rad 2: hva du gjør ----
    y, h = R2
    cell(f, "c0", 0, y, h); chip(f, "c0", X0 + 14, y + 12, CW - 28, "data-admins", "da")
    f.lines("c0", cx(0), y + 64, ["Setter opp", "overføring", "fra kilden"], 14, C["ink"], 400, "middle", 19)
    cell(f, "c1", 1, y, h, fill=GREYF); chip(f, "c1", X0 + CW + 14, y + 12, CW - 28, "ingen fast tilgang", "none")
    f.lines("c1", cx(1), y + 64, ["Du ser ikke", "kildedata. JIT for", "data-admins ved behov"], 13, C["ink"], 400, "middle", 19)
    cell(f, "c2", 2, y, h); chip(f, "c2", X0 + CW * 2 + 14, y + 12, CW - 28, "developers", "dev")
    f.lines("c2", cx(2), y + 64, ["Skriver koden,", "Kildomaten kjører.", "Data-admins", "godkjenner."], 14, C["ink"], 400, "middle", 19)
    cell(f, "cm", 3, y, h, span=3); chip(f, "cm", X0 + CW * 3 + 14, y + 12, 150, "developers", "dev")
    f.lines("cm", X0 + CW * 3 + 18, y + 70, ["Skriver og kjører egen kode i Dapla Lab, steg for steg.",
                                            "Leser og skriver i produktbøtta.",
                                            "Koden versjoneres i teamets repo på GitHub."], 15, C["ink"], 400, lh=22)
    cell(f, "c6", 6, y, h); chip(f, "c6", X0 + CW * 6 + 14, y + 12, CW - 28, "developers", "dev")
    f.lines("c6", cx(6), y + 64, ["Overfører til", "Statistikkbanken.", "Legger data i", "delt-bøtte."], 14, C["ink"], 400, "middle", 19)

    # ---- Rad 3: verktøy ----
    y, h = R3
    tools = {0: ["Transfer Service", "Altinn 3"], 1: ["Kildebøtte"], 2: ["Kildomaten", "Pseudonymisering"],
             6: ["statbank-client", "Delt-bøtte", "Delomaten"]}
    for j in (0, 1, 2, 6):
        g = f"c{j}"
        cell(f, g, j, y, h, fill=GREYF if j == 1 else None)
        for k, t in enumerate(tools[j]):
            chip(f, g, X0 + CW * j + 14, y + 14 + k * 34, CW - 28, t, "none" if j == 1 else "tool")
    f.lock("c1", cx(1) - 12, y + 60, C["grey"])
    cell(f, "cm", 3, y, h, span=3)
    mx = X0 + CW * 3 + 14
    chip(f, "cm", mx, y + 14, 150, "Dapla Lab", "tool")
    f.text("cm", mx + 164, y + 32, "Jupyter · RStudio · VS Code", 14, C["dark"], 600)
    chip(f, "cm", mx, y + 48, 150, "ssb-project", "tool")
    f.text("cm", mx + 164, y + 66, "GitHub · poetry", 14, C["dark"], 600)
    chip(f, "cm", mx, y + 82, 150, "/buckets/produkt", "tool")
    f.text("cm", mx + 164, y + 100, "pandas · arrow, som lokalt", 14, C["dark"], 600)
    f.text("cm", mx, y + 136, "Felles funksjoner: ssb-fagfunksjoner · Metodebiblioteket", 13, C["grey"], 600)

    # ---- Rad 4: dokumentasjon ----
    y, h = R4
    docs = {0: [("Kudoc", "tool"), ("kilde og utvalg", None)], 1: [("Datadoc · minimal", "min")],
            2: [("ikke påkrevd ?", "no")], 3: [("Datadoc · full", "full"), ("Vardef", "tool")],
            4: [("Datadoc · full", "full"), ("Vardef", "tool")], 5: [("Datadoc · full", "full"), ("Vardef", "tool")],
            6: [("ikke avklart", "no")]}
    for j in range(7):
        g = f"d{j}"
        cell(f, g, j, y, h)
        k = 0
        for t, kind in docs[j]:
            if kind:
                chip(f, g, X0 + CW * j + 14, y + 16 + k * 34, CW - 28, t, kind)
            else:
                f.text(g, cx(j), y + 16 + k * 34 + 18, t, 13, C["grey"], 600, "middle")
            k += 1
    f.lines("dnote", X0 + 14, y + h - 14, [""], 12, C["grey"])

    # ---- I dag-merknad ----
    f.rect("now", 60, 882, 1340, 100, C["white"], C["dark"], 1.5, 10)
    f.text("now", 80, 916, "I dag", 18, C["ink"], 700)
    f.lines("now", 80, 944, ["Etter inndata kjører du koden selv. Automatisert kjøring av egne jobber er foreslått,",
                             "men ikke innført. Kildomaten er det eneste automatiske steget i løpet."], 16, C["dark"], lh=22)


DIMC = "#dfe5e5"


def frame(f, v):
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, v["tag"], 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')
    f.rect("_", 1440, 176, 420, 806, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 222, v["panel"], 25, C["ink"], 700)
    y = 272
    num = bool(v.get("badges"))
    for i, (head, body) in enumerate(v["items"]):
        tx_ = 1516 if num else 1466
        if num:
            f.badge(1485, y - 8, i + 1)
        f.text("_", tx_, y, head, 20, C["ink"], 700)
        f.lines("_", tx_, y + 27, body, 17, C["dark"], lh=23)
        y += 27 + len(body) * 23 + 22
    for k, (bx, by) in enumerate(v.get("badges", [])):
        f.badge(bx, by, k + 1)
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    chip(f, "_", 60, y - 20, 120, "developers", "dev")
    f.text("_", 190, y, "Du, i det daglige", 16, C["dark"])
    chip(f, "_", 350, y - 20, 120, "data-admins", "da")
    f.text("_", 480, y, "Godkjenner, får JIT", 16, C["dark"])
    chip(f, "_", 660, y - 20, 150, "Datadoc · full", "full")
    chip(f, "_", 820, y - 20, 150, "Datadoc · minimal", "min")
    f.text("_", 980, y, "Dokumentasjonskrav", 16, C["dark"])
    chip(f, "_", 1160, y - 20, 120, "ubekreftet", "no")
    f.text("_", 1860, y, f"Utkast {DATO} · Kilde: manual.dapla.ssb.no", 15, C["grey"], 400, "end")


ALLC = {f"c{j}" for j in range(7)} | {f"d{j}" for j in range(7)} | {"cm"}
V = [
    dict(file="0-oversikt.svg", hi=None, tag="Oversikt",
         title="Slik jobber teamet på Dapla",
         sub="Fra kildedata til publisering: hva som skjer, hva du gjør og hva du bruker",
         panel="Slik leses figuren",
         items=[("Kolonner er datatilstander", ["De samme som i de tekniske", "figurene, fra kildedata til utdata."]),
                ("Rader er dine spørsmål", ["Hva skjer, hva gjør jeg, hvilke", "verktøy, og hva må dokumenteres."]),
                ("Du er developer", ["Du jobber i produktbøtta. Kilde-", "data ser du ikke. Data-admins", "godkjenner og kan få JIT."]),
                ("Mesteparten skjer i Dapla Lab", ["Fra inndata til utdata skriver", "og kjører du koden selv."])]),
    dict(file="1-kom-i-gang.svg", tag="Fokus 1 av 5", hi={"pre"},
         title="Før du starter", sub="Fokus: tre ting som må være på plass",
         panel="Kom i gang",
         items=[("Bli medlem av et team", ["Seksjonslederen legger deg til", "i Dapla Ctrl. Tilgang følger", "teamet, ikke deg."]),
                ("Lag et ssb-project", ["Standard prosjektmal med kode", "i GitHub og pakker via poetry."]),
                ("Start en tjeneste i Dapla Lab", ["Velg Jupyter, RStudio eller VS", "Code, og velg teamet du jobber", "for. Da får du teamets data."])],
         badges=[(250, 205), (580, 205), (950, 205)]),
    dict(file="2-inn.svg", tag="Fokus 2 av 5", hi={"c0", "c1", "c2", "d0", "d1", "d2"},
         title="Inn: fra kilde til inndata", sub="Fokus: det du ikke ser, og det Kildomaten gjør for deg",
         panel="Fram til inndata",
         items=[("Overføring settes opp", ["Data-admins setter opp over-", "føring fra Altinn, registre eller", "on-prem via Transfer Service."]),
                ("Kildedata er skjermet", ["Ingen har fast tilgang. Du ser", "først dataene som inndata."]),
                ("Kildomaten gjør jobben", ["Du skriver koden som pseudo-", "nymiserer og standardiserer.", "Data-admins godkjenner den."])],
         badges=[(X0 + 4, 414), (X0 + CW + 4, 300), (X0 + CW * 2 + 4, 414)]),
    dict(file="3-daglig-arbeid.svg", tag="Fokus 3 av 5", hi={"c3", "c4", "c5", "cm", "d3", "d4", "d5", "now"},
         title="Daglig arbeid: fra inndata til utdata", sub="Fokus: der du bruker mesteparten av tiden",
         panel="I Dapla Lab",
         items=[("Egen kode, steg for steg", ["Editering, koblinger, beregning", "og konfidensialitet gjøres i", "Python eller R."]),
                ("Filer som lokalt", ["Produktbøtta ligger under", "/buckets/produkt. pandas og", "arrow fungerer som vanlig."]),
                ("Kode i GitHub", ["Alt versjoneres i teamets repo.", "Bruk felles funksjoner der de", "finnes."]),
                ("Du starter selv", ["Automatisert kjøring er foreslått,", "ikke innført."])],
         badges=[(X0 + CW * 3 + 4, 414), (X0 + CW * 3 + 2, 669), (X0 + CW * 3 + 2, 635), (60, 882)]),
    dict(file="4-ut.svg", tag="Fokus 4 av 5", hi={"c6", "d6", "c5"},
         title="Ut: publisering og deling", sub="Fokus: fra utdata til Statistikkbanken og andre team",
         panel="Ut av teamet",
         items=[("Statistikkbanken", ["dapla-statbank-client validerer", "mot filbeskrivelsen og overfører.", "Test går bare til testbasen."]),
                ("Deling med andre team", ["Legg data i delt-bøtta. Eierteamet", "bestemmer hvem som får lese."]),
                ("Personopplysninger", ["Deles via Delomaten, ikke", "vanlig delt-bøtte."])],
         badges=[(X0 + CW * 6 + 4, 414), (X0 + CW * 6 + 4, 574), (X0 + CW * 6 + 4, 642)]),
    dict(file="5-dokumentasjon.svg", tag="Fokus 5 av 5", hi={f"d{j}" for j in range(7)},
         title="Hva du må dokumentere", sub="Fokus: dokumentasjonskrav per datatilstand",
         panel="Dokumentasjon",
         items=[("Datadoc for datasett", ["Påkrevd for kildedata (minimalt)", "og for klargjorte data, statistikk", "og utdata (fullt)."]),
                ("Vardef for variabler", ["Variablene i datasettet kobles", "til definisjonene i Vardef."]),
                ("Editor eller kode", ["Datadoc-editoren i Dapla Lab, eller", "dapla-toolbelt-metadata i koden."]),
                ("Må avklares", ["Om inndata skal dokumenteres, og", "hva som følger med til publisering."])],
         badges=[(X0 + CW + 4, 734), (X0 + CW * 3 + 4, 734), (X0 + CW * 4 + 4, 734), (X0 + CW * 2 + 4, 734)]),
]


def main():
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in V:
        f = Fig(v["hi"])
        base(f)
        frame(f, v)
        open(os.path.join(out, "bruk-prosess-" + v["file"]), "w", encoding="utf-8").write(f.svg())
    print("ok")


if __name__ == "__main__":
    main()
