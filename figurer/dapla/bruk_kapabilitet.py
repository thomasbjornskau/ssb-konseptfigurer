"""Bruk × Kapabilitet: «Hva skal du gjøre, og med hva?»
Samme ni kapabiliteter og plassering som orienteringskartet. Fokus = ett lag utvidet,
de andre sammenfoldet."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
U = "5 4"

# (tittel, effekt, [(verktøy, [beskrivelse], sikker)])
LAYERS = [
    ("Kjerne", ["Det du gjør"], C["white"], [
        ("Hente inn data", ["Få data fra kilden og inn", "i teamets bøtter"],
         [("Transfer Service", ["flytter filer fra on-prem til", "kildebøtta (data-admins)"], 1),
          ("Altinn 3", ["skjemadata fra undersøkelser", "kommer rett inn på Dapla"], 1),
          ("Kildomaten", ["gjør nye kildedata om til", "inndata, automatisk"], 1),
          ("Kudoc", ["dokumenterer kilde og", "utvalg"], 1)]),
        ("Bearbeide og produsere", ["Skrive og kjøre koden som", "lager statistikken"],
         [("Dapla Lab", ["Jupyter, RStudio eller VS Code", "i nettleseren"], 1),
          ("Jupyter-pyspark", ["for datamengder som krever", "Spark"], 1),
          ("ssb-fagfunksjoner", ["felles funksjoner i Python;", "Metodebiblioteket i R"], 1),
          ("pandas / arrow", ["leser og skriver filer i", "bøttene som lokalt"], 1)]),
        ("Dele og publisere", ["Få resultatene ut til", "brukere og andre team"],
         [("statbank-client", ["validerer og overfører til", "Statistikkbanken"], 1),
          ("Delt-bøtter", ["deler data med andre team,", "kun lesetilgang"], 1),
          ("Delomaten", ["deler personopplysninger", "på en kontrollert måte"], 1)]),
    ]),
    ("Styring", ["Det som gjør arbeidet", "ditt etterprøvbart"], C["tealp"], [
        ("Beskrive og finne data", ["Dokumentere egne data og", "finne andres"],
         [("Datadoc", ["dokumenterer datasett, i editor", "eller med toolbelt-metadata"], 1),
          ("Vardef", ["variabeldefinisjoner du kobler", "variablene dine til"], 1),
          ("Klass", ["kodeverk og klassifikasjoner,", "via klassR og ssb-klass-python"], 1),
          ("SSB Dataportal", ["søk etter datasett på", "tvers av team"], 1)]),
        ("Automatisere", ["La faste steg kjøre", "av seg selv"],
         [("Kildomaten", ["det eneste automatiske steget", "i dag, fra kilde til inndata"], 1),
          ("Container-jobber", ["automatisert kjøring av egen", "kode er foreslått, ikke innført"], 0)]),
        ("Dokumentere kvalitet", ["Vise hva som er gjort,", "av hvem og hvorfor"],
         [("GitHub", ["historikken viser hver endring", "i koden"], 1),
          ("Datadoc", ["hvem som eier og hva som", "gjelder for datasettet"], 1),
          ("Prosessdata", ["logg av endringer i data;", "løsningen er under arbeid"], 0),
          ("Kvalitetsindikatorer", ["felles indikatorer er", "under arbeid"], 0)]),
    ]),
    ("Fundament", ["Det du", "bygger på"], C["teal"], [
        ("Styre tilgang", ["Få tilgang til riktige data,", "og bare dem"],
         [("Dapla Ctrl", ["viser team og medlemmer;", "seksjonsleder legger til"], 1),
          ("Velg team i Lab", ["teamet du velger, avgjør", "hvilke data du ser"], 1),
          ("toolbelt-pseudo", ["pseudonymiserer", "personidentifikatorer"], 1)]),
        ("Lagre og regne", ["Ha plass og kraft nok,", "uten å tenke på servere"],
         [("/buckets", ["bøttene vises som mapper", "i Dapla Lab"], 1),
          ("Parquet", ["standard lagringsformat", "(obligatorisk)"], 1),
          ("Ressursvalg", ["velg CPU og minne når du", "starter en tjeneste"], 0)]),
        ("Utvikle og dele kode", ["Skrive kode som andre kan", "lese, kjøre og gjenbruke"],
         [("ssb-project", ["mal for nye prosjekter", "med riktig oppsett"], 1),
          ("GitHub", ["versjonering, pull requests", "og samarbeid"], 1),
          ("Kvakk", ["SSBs standarder for", "kodekvalitet"], 1),
          ("Godkjentlisten", ["hvilke verktøy og pakker", "som er godkjent"], 1)]),
    ]),
]
BAND = ["Dapla Lab: der du jobber", "/buckets: der dataene ligger", "GitHub: der koden ligger", "Datadoc: der data beskrives"]

VARIANTS = [
    dict(file="0-oversikt.svg", focus=None, tag="Oversikt", title="Hva skal du gjøre, og med hva?",
         sub="Ni kapabiliteter i Dapla, og verktøyene du bruker til hver av dem"),
    dict(file="1-kjerne.svg", focus=0, tag="Fokus 1 av 3", title="Kjernen: hente inn, bearbeide, dele",
         sub="Fokus: verktøyene i det daglige produksjonsarbeidet"),
    dict(file="2-styring.svg", focus=1, tag="Fokus 2 av 3", title="Styring: beskrive, automatisere, dokumentere",
         sub="Fokus: det som gjør arbeidet ditt etterprøvbart"),
    dict(file="3-fundament.svg", focus=2, tag="Fokus 3 av 3", title="Fundamentet: tilgang, lagring og kode",
         sub="Fokus: det du bygger på"),
]


def chip(f, g, x, y, w, label, sure=True, h=28):
    f.rect(g, x, y, w, h, C["white"], C["dark"] if sure else C["grey"], 1.5, h / 2, dash=None if sure else U)
    f.text(g, x + w / 2, y + h / 2 + 5, label, 14, C["dark"] if sure else C["grey"], 700, "middle")


def build(v):
    fo = v["focus"]
    f = Fig(None if fo is None else {f"L{fo}"})
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, v["tag"], 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    # bånd: fire steder du alltid er innom
    g = "band"
    f.rect(g, 60, 184, 1800, 76, C["purplep"], C["purplep"], 0, 12)
    f.lines(g, 84, 216, ["Fire steder du", "alltid er innom"], 19, PT, 700)
    px, pw, gap = 360, 360, 20
    for i, p in enumerate(BAND):
        x = px + i * (pw + gap)
        f.rect(g, x, 198, pw, 48, C["white"], C["purple"], 2, 24)
        a, b = p.split(": ")
        f.add(f'<text x="{x+pw/2}" y="229" font-family="Open Sans, Segoe UI, Arial, sans-serif" font-size="19" text-anchor="middle" '
              f'fill="{f.col(g,"text",PT)}"><tspan font-weight="700">{a}</tspan><tspan font-weight="400">  {b}</tspan></text>')

    # rader
    total, rg = 702 - 28, 14
    if fo is None:
        hs = [total / 3] * 3
    else:
        hs = [110] * 3
        hs[fo] = total - 220
    y = 282
    cx0, cw, cg = 360, 487, 20
    for li, (name, desc, fill, caps) in enumerate(LAYERS):
        gid = f"L{li}"
        h = hs[li]
        open_ = fo == li
        folded = fo is not None and not open_
        f.rect(gid, 60, y, 8, h, C["dark"], C["dark"], 0, 0)
        f.text(gid, 88, y + 40, name, 30, C["ink"], 700)
        if not folded:
            f.lines(gid, 88, y + 76, desc, 19, C["grey"], lh=25)
        for ci, (cap, eff, tools) in enumerate(caps):
            x = cx0 + ci * (cw + cg)
            f.rect(gid, x, y, cw, h, fill, C["dark"] if li == 0 else fill, 2, 12)
            f.text(gid, x + 28, y + 30, "JEG VIL", 13, C["grey"], 700)
            f.text(gid, x + 28, y + 62, cap, 26, C["ink"], 700)
            if folded:
                continue
            f.rect(gid, x + 28, y + 76, 60, 4, C["green"], C["green"], 0, 0)
            f.lines(gid, x + 28, y + 110, eff, 18, C["dark"], lh=25)
            if not open_:
                # oversikt: tre verktøy som brikker
                n = min(3, len(tools))
                w = (cw - 56 - (n - 1) * 8) / n
                for k in range(n):
                    t, _, sure = tools[k]
                    chip(f, gid, x + 28 + k * (w + 8), y + h - 50, w, t, sure)
            else:
                yy = y + 170
                for t, d, sure in tools:
                    chip(f, gid, x + 28, yy, 170, t, sure, 30)
                    f.lines(gid, x + 212, yy + 12, d, 15, C["dark"] if sure else C["grey"], lh=20)
                    yy += 64
        y += h + rg

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    yb = 1046
    chip(f, "_", 60, yb - 22, 120, "Verktøy", True)
    f.text("_", 192, yb, "I bruk", 16, C["dark"])
    chip(f, "_", 290, yb - 22, 150, "Verktøy", False)
    f.text("_", 452, yb, "Under arbeid, forslag eller ubekreftet", 16, C["dark"])
    f.text("_", 1860, yb, f"Utkast {DATO} · Kilder: manual.dapla.ssb.no, godkjentlisten", 15, C["grey"], 400, "end")
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in VARIANTS:
        open(os.path.join(out, "bruk-kapabilitet-" + v["file"]), "w", encoding="utf-8").write(build(v).svg())
    print("ok")
