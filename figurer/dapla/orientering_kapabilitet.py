"""Orientering × Kapabilitet: kapabilitetskart i tre lag.
Oversikt + tre fokusvarianter (ett lag om gangen, med tjenestene som realiserer kapabilitetene).
Elementene står på samme sted i alle variantene."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
# (navn, beskrivelse, fyll, kapabiliteter[(navn, effekt, tjenester[(tekst, sikker)])])
LAYERS = [
    ("Kjerne", ["Det statistikk-", "produksjonen gjør"], C["white"], [
        ("Hente inn og motta data", ["Data fra registre, undersøkelser og", "andre kilder kommer inn på én måte"],
         [("Transfer Service", 1), ("Altinn / Maskinporten", 1), ("Kildomaten", 1), ("Kudoc", 1)]),
        ("Bearbeide og produsere", ["Fra kildedata til statistikk i kode,", "med felles verktøy og datatilstander"],
         [("Dapla Lab", 1), ("Python og R", 1), ("Metodebiblioteket", 1), ("ssb-fagfunksjoner", 1)]),
        ("Dele og formidle", ["Data og statistikk gjøres tilgjengelig", "internt, for forskning og publisering"],
         [("Delt-bøtter", 1), ("Delomaten", 1), ("Statistikkbanken", 1), ("Microdata.no", 1)]),
    ]),
    ("Styring", ["Det som gjør", "produksjonen trygg", "og etterprøvbar"], C["tealp"], [
        ("Beskrive og finne data", ["Datasett, variabler og kodeverk er", "dokumentert og søkbare på tvers"],
         [("Datadoc", 1), ("Vardef", 1), ("Klass", 1), ("SSB Dataportal", 1)]),
        ("Automatisere og overvåke", ["Faste løp kjører av seg selv,", "og avvik blir synlige"],
         [("Kildomaten", 1), ("Tidsstyring / hendelser", 0), ("Logging og varsling", 0), ("Kostnadskontroll", 0)]),
        ("Dokumentere kvalitet", ["Det går an å etterprøve hva som", "ble gjort, av hvem og hvorfor"],
         [("Prosessdata", 0), ("Kvalitetsindikatorer", 0), ("StatDoc", 0), ("GitHub-historikk", 1)]),
    ]),
    ("Fundament", ["Det alt", "står på"], C["teal"], [
        ("Beskytte og styre tilgang", ["Sensitive data er skjermet,", "og tilgang er sporbar"],
         [("Dapla-team", 1), ("Dapla Ctrl", 1), ("Pseudonymisering", 1), ("JIT-tilgang", 1)]),
        ("Lagre og beregne i skala", ["Kapasitet etter behov,", "uten egne servere"],
         [("Google Cloud", 1), ("Bøtter (GCS)", 1), ("Onyxia / Kubernetes", 1), ("CloudSQL", 1)]),
        ("Utvikle og dele kode", ["Felles standarder og biblioteker,", "versjonert og gjenbrukbart"],
         [("GitHub", 1), ("ssb-project", 1), ("PyPI / CRAN", 1), ("Godkjentlisten", 1)]),
    ]),
]
PRINCIPLES = ["Selvbetjente team", "Kode framfor klikk", "Data eid av fagmiljøet", "Felles plattform"]

VARIANTS = [
    dict(file="kapabiliteter-0-oversikt.svg", focus=None, tag="Oversikt",
         title="Hva Dapla gjør mulig", sub="Ni kapabiliteter i tre lag"),
    dict(file="kapabiliteter-1-kjerne.svg", focus=0, tag="Fokus 1 av 3",
         title="Kjernen: fra data inn til statistikk ut", sub="Fokus: kjernekapabilitetene og tjenestene som realiserer dem"),
    dict(file="kapabiliteter-2-styring.svg", focus=1, tag="Fokus 2 av 3",
         title="Styring: trygg og etterprøvbar produksjon", sub="Fokus: styringskapabilitetene og tjenestene som realiserer dem"),
    dict(file="kapabiliteter-3-fundament.svg", focus=2, tag="Fokus 3 av 3",
         title="Fundamentet: sikkerhet, skala og kode", sub="Fokus: fundamentet og tjenestene som realiserer det"),
]


def status(f, gid, x, y, kind):
    g, r = C["green"], 11
    if kind == "ok":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f.col(gid,"stroke",g)}"/>')
    elif kind == "wip":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{g}" stroke-width="3"/>')
        f.add(f'<path d="M{x},{y-r} A{r},{r} 0 0 1 {x},{y+r} Z" fill="{g}"/>')
    elif kind == "plan":
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{g}" stroke-width="3"/>')
    else:
        f.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{f.col(gid,"stroke",C["grey"])}" '
              f'stroke-width="2" stroke-dasharray="4 3"/>')
        f.text(gid, x, y + 6, "?", 16, C["grey"], 700, "middle")


def chip(f, gid, x, y, w, label, sure):
    f.rect(gid, x, y, w, 32, C["white"], C["dark"] if sure else C["grey"], 1.5, 16,
           dash=None if sure else "5 4")
    f.text(gid, x + w / 2, y + 22, label, 16, C["dark"] if sure else C["grey"], 600, "middle")


def build(v):
    fo = v["focus"]
    hi = None if fo is None else {f"L{fo}"}
    f = Fig(hi)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    # topptekst
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, v["tag"], 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    # prinsippbånd
    g = "pr"
    f.rect(g, 60, 184, 1800, 76, C["purplep"], C["purplep"], 0, 12)
    f.lines(g, 84, 216, ["Prinsipper for", "hvordan det leveres"], 19, PT, 700)
    px, pw, gap = 360, 360, 20
    for i, p in enumerate(PRINCIPLES):
        x = px + i * (pw + gap)
        f.rect(g, x, 198, pw, 48, C["white"], C["purple"], 2, 24)
        f.text(g, x + pw / 2, 230, p, 21, PT, 700, "middle")

    # lag
    y0, rh, rg = 282, 216, 14
    cx0, cw, cg = 360, 487, 20
    for li, (name, desc, fill, caps) in enumerate(LAYERS):
        gid = f"L{li}"
        y = y0 + li * (rh + rg)
        f.rect(gid, 60, y, 8, rh, C["dark"], C["dark"], 0, 0)
        f.text(gid, 88, y + 40, name, 30, C["ink"], 700)
        f.lines(gid, 88, y + 76, desc, 19, C["grey"], lh=25)
        for ci, (cap, eff, svc) in enumerate(caps):
            x = cx0 + ci * (cw + cg)
            f.rect(gid, x, y, cw, rh, fill, C["dark"] if li == 0 else fill, 2, 12)
            f.text(gid, x + 28, y + 48, cap, 26, C["ink"], 700)
            f.rect(gid, x + 28, y + 62, 60, 4, C["green"], C["green"], 0, 0)
            f.lines(gid, x + 28, y + 98, eff, 20, C["dark"], lh=26)
            status(f, gid, x + cw - 30, y + 30, "?")
            if fo == li:
                chw = (cw - 56 - 10) / 2
                for k, (lab, sure) in enumerate(svc):
                    cxk = x + 28 + (k % 2) * (chw + 10)
                    cyk = y + 138 + (k // 2) * 38
                    chip(f, gid, cxk, cyk, chw, lab, sure)

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    f.text("_", 60, y, "Status:", 17, C["dark"], 700)
    x = 140
    for k, lab in [("ok", "Etablert"), ("wip", "Under utvikling"), ("plan", "Planlagt"), ("?", "Ikke vurdert ennå")]:
        status(f, "_", x + 11, y - 6, k)
        f.text("_", x + 32, y, lab, 17, C["dark"])
        x += 60 + len(lab) * 9 + 20
    if fo is not None:
        x += 30
        f.rect("_", x, y - 22, 90, 28, C["white"], C["dark"], 1.5, 14)
        f.text("_", x + 45, y - 3, "Tjeneste", 15, C["dark"], 600, "middle")
        f.rect("_", x + 104, y - 22, 124, 28, C["white"], C["grey"], 1.5, 14, dash="5 4")
        f.text("_", x + 166, y - 3, "Må bekreftes", 15, C["grey"], 600, "middle")
    f.text("_", 1860, y, f"Utkast {DATO} · Inndeling og status er foreløpige", 16, C["grey"], 400, "end")
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in VARIANTS:
        open(os.path.join(out, v["file"]), "w", encoding="utf-8").write(build(v).svg())
    print("ok")
