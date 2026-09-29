"""Teknisk × Prosess og flyt.
Grunnfigur: svømmebaner (soner fra strukturfiguren) × datatilstander (SSB-standard),
med egen bane nederst for kontrollflyt. Varianter: dataflyt (oversikt), kontroll i dag, kontroll forslag.
Egen figur: endringsflyt (i dag + forslag)."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
GREYF = "#f3f5f5"
GREYS = "#b9c5c6"
U = "5 4"
X0, CW = 252, 164
def cx(i): return X0 + CW * i + CW / 2
def tx(i): return X0 + CW * (i + 1)  # overgang mellom kolonne i og i+1

COLS = ["Innhenting", "Kildedata", "Inndata", "Klargjorte data", "Statistikk", "Utdata", "Formidling"]
STATE = [False, True, True, True, True, True, False]
LANES = [  # id, label, sub, y, h, fill, stroke
    ("L1", "Utenfor Dapla", ["kilder og mottakere"], 244, 118, GREYF, GREYS),
    ("L2", "Kildeprosjekt", ["per team"], 372, 118, C["purplep"], C["purple"]),
    ("L3", "Standardprosjekt", ["per team"], 500, 160, C["purplep"], C["purple"]),
    ("L4", "Felles tjenester", ["driftes én gang"], 670, 118, C["tealp"], C["teal"]),
    ("L5", "Hva starter steget?", ["kontrollflyt"], 798, 186, C["white"], C["dark"]),
]


# ---------- ikoner ----------
def ic_clock(f, g, x, y, c):
    c = f.col(g, "stroke", c)
    f.add(f'<circle cx="{x}" cy="{y}" r="15" fill="{C["white"]}" stroke="{c}" stroke-width="3"/>')
    f.add(f'<polyline points="{x},{y-9} {x},{y} {x+7},{y+4}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')

def ic_event(f, g, x, y, c):
    c = f.col(g, "stroke", c)
    f.add(f'<polygon points="{x+3},{y-17} {x-10},{y+3} {x-1},{y+3} {x-4},{y+17} {x+10},{y-4} {x+1},{y-4}" fill="{c}"/>')

def ic_person(f, g, x, y, c):
    f.person(g, x, y + 4, 0.55, c)

def ic_check(f, g, x, y, c):
    c = f.col(g, "stroke", c)
    f.add(f'<circle cx="{x}" cy="{y}" r="15" fill="{c}"/>')
    f.add(f'<polyline points="{x-7},{y} {x-2},{y+6} {x+8},{y-6}" fill="none" stroke="{C["white"]}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')

def ic_job(f, g, x, y, c):
    c = f.col(g, "stroke", c)
    f.add(f'<rect x="{x-16}" y="{y-13}" width="32" height="26" rx="4" fill="{C["white"]}" stroke="{c}" stroke-width="3"/>')
    f.add(f'<polygon points="{x-5},{y-7} {x+7},{y} {x-5},{y+7}" fill="{c}"/>')

def ic_api(f, g, x, y, c):
    c = f.col(g, "stroke", c)
    f.add(f'<rect x="{x-20}" y="{y-12}" width="40" height="24" rx="12" fill="{C["white"]}" stroke="{c}" stroke-width="2.5"/>')
    f.text(g, x, y + 5, "API", 12, c, 700, "middle")

ICONS = dict(clock=ic_clock, event=ic_event, person=ic_person, check=ic_check, job=ic_job, api=ic_api)


def marker(f, g, x, icons, label, sure=True, line_to=None):
    """Kontrollmarkør i bane L5 ved overgang x."""
    col = C["dark"] if sure else C["grey"]
    if False and line_to:
        f.add(f'<line x1="{x}" y1="836" x2="{x}" y2="{line_to}" stroke="{f.col(g,"stroke",GREYS)}" stroke-width="2" stroke-dasharray="2 5"/>')
    n = len(icons)
    for k, ic in enumerate(icons):
        ICONS[ic](f, g, x + (k - (n - 1) / 2) * 40, 862, col)
    for i, l in enumerate(label):
        f.text(g, x, 904 + i * 19, l, 15, col, 600 if i == 0 else 400, "middle")


def lanes(f):
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    # kolonneoverskrifter
    for i, name in enumerate(COLS):
        x = X0 + CW * i
        if STATE[i]:
            f.rect("hdr", x + 6, 190, CW - 12, 40, C["greenp"], C["green"], 1.5, 20)
            f.text("hdr", cx(i), 216, name, 16, C["green"], 700, "middle")
        else:
            f.text("hdr", cx(i), 216, name, 16, C["grey"], 700, "middle")
    f.text("hdr", 60, 216, "Datatilstand →", 16, C["grey"], 700)
    for lid, lab, sub, y, h, fill, stroke in LANES:
        f.rect(lid, 60, y, 1340, h, fill, stroke, 1.5 if lid != "L5" else 2, 10)
        f.text(lid, 76, y + 30, lab, 18, C["ink"], 700)
        f.lines(lid, 76, y + 52, sub, 14, C["grey"])
    # kolonneskiller (svake)
    for i in range(1, 7):
        x = X0 + CW * i
        f.add(f'<line x1="{x}" y1="244" x2="{x}" y2="788" stroke="#e6ebeb" stroke-width="1"/>')


def data(f):
    # L1
    f.rect("src", cx(0) - 72, 262, 144, 82, C["white"], C["dark"], 2, 8)
    f.lines("src", cx(0), 290, ["On-prem og", "eksterne kilder"], 15, C["ink"], 600, "middle", 19)
    f.text("src", cx(0), 332, "filer · Oracle · Altinn", 12, C["grey"], 400, "middle")
    f.rect("rcv", cx(6) - 72, 262, 144, 82, C["white"], C["grey"], 1.8, 8, dash=U)
    f.lines("rcv", cx(6), 292, ["Statistikkbanken", "Microdata.no"], 15, C["grey"], 600, "middle", 19)
    f.text("rcv", cx(6), 334, "leveransevei ?", 12, C["grey"], 400, "middle")
    # L2
    f.cyl("kb", cx(1) - 60, 386, 120, 90, C["green"], C["green"])
    f.text("kb", cx(1), 440, "Kildebøtte", 15, C["white"], 700, "middle")
    # L3: produktbøtte-bånd
    f.rect("pb", X0 + CW * 2 + 8, 512, CW * 4 - 16, 136, C["white"], C["green"], 1.5, 10)
    f.text("pb", X0 + CW * 2 + 22, 534, "Produktbøtte", 14, C["green"], 700)
    names = ["inndata", "klargjorte", "statistikk", "utdata"]
    for k, n in enumerate(names):
        i = k + 2
        f.cyl("pb", cx(i) - 52, 546, 104, 84, C["greenl"], C["green"])
        f.text("pb", cx(i), 596, n, 14, C["ink"], 700, "middle")
    f.cyl("delt", cx(6) - 52, 546, 104, 84, C["greenp"], C["green"])
    f.text("delt", cx(6), 596, "Delt-bøtte", 14, C["ink"], 700, "middle")
    # L4
    f.rect("l4a", X0 + 8, 686, CW - 16, 86, C["white"], C["dark"], 1.5, 8)
    f.lines("l4a", cx(0), 714, ["Transfer Service", "SUV-API (ORDS)"], 14, C["ink"], 600, "middle", 19)
    f.text("l4a", cx(0), 756, "ORDS midlertidig", 12, C["grey"], 400, "middle")
    f.rect("l4b", X0 + CW + 8, 686, CW - 16, 86, C["white"], C["grey"], 1.5, 8, dash=U)
    f.lines("l4b", cx(1), 722, ["Pseudo-", "nøkler"], 15, C["grey"], 600, "middle", 19)
    f.rect("l4c", X0 + CW * 2 + 8, 686, CW * 4 - 16, 86, C["white"], C["dark"], 1.5, 8)
    f.text("l4c", cx(4), 718, "Metadatatjenester", 15, C["ink"], 600, "middle")
    f.text("l4c", cx(4), 740, "Datadoc · Vardef · Klass", 13, C["grey"], 400, "middle")
    f.rect("l4d", X0 + CW * 6 + 8, 686, CW - 16, 86, C["white"], C["dark"], 1.5, 8)
    f.lines("l4d", cx(6), 722, ["SSB", "Dataportal"], 15, C["ink"], 600, "middle", 19)

    # dataflyt
    g = C["green"]
    f.arrow("f0", [(cx(0), 344), (cx(0), 430), (cx(1) - 62, 430)], g, 3, hs=10)
    f.arrow("f1", [(cx(1) + 60, 430), (tx(1), 430), (tx(1), 588), (cx(2) - 54, 588)], g, 3, hs=10)
    f.rect("f1", tx(1) + 10, 446, 116, 26, C["white"], g, 1.5, 13)
    f.text("f1", tx(1) + 68, 464, "Kildomaten", 14, g, 700, "middle")
    for i in (2, 3, 4):
        f.arrow(f"f{i}", [(cx(i) + 52, 588), (cx(i + 1) - 54, 588)], g, 3, hs=10)
    f.arrow("f5", [(cx(5) + 52, 588), (cx(6) - 54, 588)], g, 3, hs=10)
    f.arrow("f6", [(cx(6), 546), (cx(6), 346)], g, 2.5, dash=U, hs=10)
    # metadata + pseudo (avhengigheter)
    f.arrow("fm", [(cx(4), 648), (cx(4), 684)], C["dark"], 2, dash="5 4", hs=9)
    f.text("fm", cx(4) + 8, 664, "dokumenteres", 12, C["dark"], 600)
    f.arrow("fp", [(cx(1), 686), (cx(1), 490), (tx(1) - 4, 490)], C["grey"], 2, hs=9)
    f.text("fp", cx(1) + 8, 560, "nøkler", 12, C["grey"], 600)


def frame(f, v):
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
    x = 1520
    if v.get("forslag"):
        f.rect("_", 1350, 62, 150, 40, C["white"], C["purple"], 2.5, 20, dash="7 5")
        f.text("_", 1425, 89, "FORSLAG", 19, PT, 700, "middle")
    f.rect("_", 1520, 62, 150, 40, C["ink"], C["ink"], 0, 20)
    f.text("_", 1595, 89, "INTERN", 19, C["white"], 700, "middle")
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, v["tag"], 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')
    f.rect("_", 1440, 180, 420, 804, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, v["panel"], 25, C["ink"], 700)
    y = 276
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


def legend_flow(f, extra_note):
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    f.arrow("_", [(60, y - 6), (100, y - 6)], C["green"], 3, hs=9)
    f.text("_", 110, y, "Dataflyt", 16, C["dark"])
    ic_clock(f, "_", 222, y - 6, C["dark"]); f.text("_", 244, y, "Tidsplan", 16, C["dark"])
    ic_event(f, "_", 346, y - 6, C["dark"]); f.text("_", 364, y, "Hendelse", 16, C["dark"])
    ic_person(f, "_", 470, y - 6, C["dark"]); f.text("_", 490, y, "Manuelt", 16, C["dark"])
    ic_check(f, "_", 586, y - 6, C["dark"]); f.text("_", 608, y, "Godkjenning", 16, C["dark"])
    ic_job(f, "_", 732, y - 6, C["dark"]); f.text("_", 756, y, "Container-jobb", 16, C["dark"])
    ic_api(f, "_", 900, y - 6, C["dark"]); f.text("_", 928, y, "Ved behov (API)", 16, C["dark"])
    f.rect("_", 1070, y - 20, 26, 24, C["white"], C["grey"], 1.8, 4, dash=U)
    f.text("_", 1106, y, "Ubekreftet", 16, C["dark"])
    f.text("_", 1860, y, f"Utkast {DATO} · {extra_note}", 15, C["grey"], 400, "end")


# ---------- kontroll-lag ----------
def control_today(f):
    g = "ctl"
    marker(f, g, tx(0), ["clock", "api"], ["Transfer: tidsplan", "ORDS: ved behov"], line_to=436)
    marker(f, g, tx(1), ["event", "check"], ["Ny fil starter", "Kildomaten", "(kode godkjent)"], line_to=596)
    f.rect(g, tx(2) - 70, 836, tx(4) - tx(2) + 140, 132, GREYF, GREYF, 0, 10)
    for i in (2, 3, 4):
        ic_person(f, g, tx(i), 862, C["dark"])
    f.text(g, tx(3), 910, "Manuelt i Dapla Lab", 16, C["dark"], 700, "middle")
    f.text(g, tx(3), 932, "Ingen felles runtime for automatisert", 14, C["dark"], 400, "middle")
    f.text(g, tx(3), 951, "kjøring utenfor Dapla Lab i dag", 14, C["dark"], 400, "middle")
    marker(f, g, tx(5), ["person"], ["Deling: IaC", "Publisering: ?"], sure=True, line_to=596)


def control_proposal(f):
    g = "ctl"
    marker(f, g, tx(0), ["clock", "api"], ["Transfer: tidsplan", "ORDS: ved behov"], line_to=436)
    marker(f, g, tx(1), ["event", "check"], ["Ny fil starter", "Kildomaten", "(uendret)"], line_to=596)
    # orkestratorbånd
    x1, x2 = tx(2) - 76, tx(4) + 76
    f.rect(g, x1, 812, x2 - x1, 40, C["white"], C["purple"], 2, 20, dash="7 5")
    f.text(g, (x1 + x2) / 2, 838, "Orkestrator (valgfri): tidsplan · Workflows · Airflow", 14, PT, 700, "middle")
    for i in (2, 3, 4):
        f.arrow(g, [(tx(i), 852), (tx(i), 872)], C["dark"], 2, hs=8)
        ic_job(f, g, tx(i), 890, C["dark"])
    f.text(g, tx(3), 930, "Container-jobb på felles runtime", 15, C["dark"], 700, "middle")
    f.text(g, tx(3), 950, "Cloud Run Jobs · kjører som teamets Runner-SA", 14, C["dark"], 400, "middle")
    marker(f, g, tx(5), ["person"], ["Deling: IaC", "Publisering: ?"], line_to=596)


V = [
    dict(file="prosess-0-dataflyt.svg", tag="Oversikt", ctl=None,
         hi=None,
         title="Fra kildedata til utdata",
         sub="Teknisk prosess · dataflyt gjennom soner og datatilstander",
         panel="Slik leses figuren",
         items=[("Kolonner er datatilstander", ["SSB-standarden fra kildedata til", "utdata er ryggraden i figuren."]),
                ("Rader er soner", ["Samme soner og farger som i", "strukturfiguren. Lilla gjentas", "per team."]),
                ("Nederste rad: kontroll", ["Hva som starter hvert steg vises", "i to varianter: i dag og forslag."]),
                ("Stiplet er ubekreftet", ["Leveransen til Statistikkbanken", "og Microdata er ikke avklart."])]),
    dict(file="prosess-1-kontroll-i-dag.svg", tag="I dag", ctl="today",
         hi=None,
         title="Hva starter hvert steg, i dag",
         sub="Teknisk prosess · kontrollflyt slik den fungerer nå",
         panel="Kontrollflyt i dag",
         items=[("Inn: tidsplan eller API", ["Transfer Service kjører maks én", "gang i timen. ORDS gir data ved", "behov (midlertidig, ADR0017)."]),
                ("Kilde til inndata: automatisk", ["Kildomaten starter på nye filer.", "Koden er godkjent av data-admins", "før den rulles ut."]),
                ("Resten er manuelt", ["Teamene kjører koden selv i", "Dapla Lab. Det finnes ingen", "felles runtime for automatisert", "kjøring i dag."]),
                ("Ut: delvis uavklart", ["Deling via delt-bøtter styres", "som IaC. Veien til publisering", "er ikke bekreftet."])],
         badges=[(tx(0) - 60, 846), (tx(1) - 50, 846), (tx(2) - 70, 836), (tx(5) - 50, 846)]),
    dict(file="prosess-2-kontroll-forslag.svg", tag="Forslag", ctl="proposal", forslag=True,
         hi=None,
         title="Hva kan starte hvert steg, i forslaget",
         sub="Teknisk prosess · kontrollflyt med felles runtime og valgfri orkestrering",
         panel="Forslag fra arkitektur",
         items=[("Kode blir container-jobber", ["Jobbkontrakt: entrypoint,", "miljøvariabler, exitkode. Ingen", "avhengighet til orkestrator."]),
                ("Én felles runtime", ["Cloud Run Jobs som startpunkt,", "GKE der det trengs. Jobben", "kjører som teamets Runner-SA."]),
                ("Orkestrering på toppen", ["Tidsplan, Workflows, Airflow", "eller manuelt. Byttbart uten", "endring i kode."]),
                ("Kildomaten uendret", ["Forslaget gjelder stegene etter", "inndata."])],
         badges=[(tx(2) - 60, 890), (tx(4) + 60, 890), (tx(2) - 76, 812), (tx(1) - 50, 846)]),
]


def build(v):
    f = Fig(v["hi"])
    lanes(f)
    data(f)
    if v["ctl"] == "today":
        control_today(f)
    elif v["ctl"] == "proposal":
        control_proposal(f)
    else:
        f.text("_", 820, 900, "Se variantene «I dag» og «Forslag»", 18, C["grey"], 600, "middle")
    frame(f, v)
    note = "Kilder: Dapla-manualen, ADR0017, notat om orkestrering (forslag)" if v["ctl"] else "Kilder: Dapla-manualen, ADR0015, 0017"
    legend_flow(f, note)
    return f


# ---------- endringsflyt ----------
def step(f, x, y, w, h, title, subs, sure=True, fill=None):
    f.rect("_", x, y, w, h, fill or C["white"], C["dark"] if sure else C["grey"], 2, 8, dash=None if sure else U)
    f.text("_", x + 14, y + 28, title, 18, C["ink"] if sure else C["grey"], 700)
    for i, s in enumerate(subs):
        f.text("_", x + 14, y + 50 + i * 19, s, 14, C["grey"])


def build_change():
    f = Fig(None)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    FR = (dict(title="Fra kode til drift", sub="Teknisk prosess · endringsflyt for infrastruktur og jobber",
                  tag="Endringsflyt", forslag=False, panel="To spor",
                  items=[("I dag: PR og godkjenning", ["Endringer i bøtter, deling og", "Kildomaten går via PR i teamets", "repo. Data-admins godkjenner,", "Atlantis ruller ut."]),
                         ("Forslag: fire ansvarslag", ["Kode, bygg, kjøring og", "rekkefølge skilles. Teamet eier", "koden, plattformen eier resten."]),
                         ("Jobbkontrakten er grensen", ["Så lenge den holdes, kan runtime", "og orkestrator byttes uten", "endring i koden."]),
                         ("To identiteter", ["Invoker får bare starte jobben.", "Runner-SA bestemmer hvilke data", "jobben får lese og skrive."])],
                  badges=[(260, 262), (260, 548), (260, 722), (1000, 604)]))

    # Spor A: i dag
    f.rect("_", 60, 180, 1340, 240, C["white"], C["dark"], 2, 12)
    f.text("_", 80, 214, "I dag", 22, C["ink"], 700)
    f.lines("_", 80, 240, ["infrastruktur og", "Kildomaten"], 15, C["grey"])
    xs = [260, 480, 700, 920, 1140]
    steps = [("Utvikler", ["endrer kode eller", "IaC-konfig"]), ("Pull request", ["i teamets repo", "på GitHub"]),
             ("Data-admins", ["godkjenner", "endringen"]), ("Atlantis", ["plan og apply", "ruller ut"]),
             ("I drift", ["bøtter, deling,", "Kildomaten"])]
    for i, (x, (t, s)) in enumerate(zip(xs, steps)):
        step(f, x, 262, 196, 120, t, s, fill=C["purplep"] if i == 2 else None)
        if i < 4:
            f.arrow("_", [(x + 196, 322), (x + 220, 322)], C["dark"], 2.5, hs=9)
    ic_check(f, "_", 700 + 170, 290, C["dark"])

    # Spor B: forslag
    f.rect("_", 60, 440, 1340, 544, C["white"], C["purple"], 2.5, 12, dash="8 6")
    f.text("_", 80, 474, "Forslag", 22, PT, 700)
    f.lines("_", 80, 500, ["batchjobber", "utenfor Dapla Lab"], 15, C["grey"])
    # ansvarskolonner
    heads = [(260, "Kode", "teamet"), (500, "Bygg", "CI"), (740, "Lager", "image")]
    for x, h1, h2 in heads:
        f.text("_", x, 530, h1.upper(), 15, PT, 700)
        f.text("_", x + len(h1) * 13 + 10, 530, "· " + h2, 15, C["grey"], 600)
    step(f, 260, 548, 210, 150, "Teamets repo", ["src/job/main.py", "requirements.txt", "Dockerfile", "workflow for bygg"])
    step(f, 500, 548, 210, 150, "GitHub Actions", ["bygg og test", "tag = git-sha", "WIF mot GCP"])
    step(f, 740, 548, 210, 150, "Artifact Registry", ["image per team", "eller prosjekt"])
    f.rect("_", 1000, 604, 380, 150, C["white"], C["dark"], 2, 8)
    f.text("_", 1014, 628, "KJØRING", 15, PT, 700)
    f.text("_", 1096, 628, "· runtime", 15, C["grey"], 600)
    f.text("_", 1014, 658, "Cloud Run Jobs", 18, C["ink"], 700)
    f.lines("_", 1014, 682, ["kjører containeren som Runner-SA", "per team (GKE ved særskilte behov)"], 14, C["grey"], lh=19)
    f.arrow("_", [(470, 622), (498, 622)], C["dark"], 2.5, hs=9)
    f.arrow("_", [(710, 622), (738, 622)], C["dark"], 2.5, hs=9)
    f.arrow("_", [(950, 660), (998, 660)], C["dark"], 2.5, hs=9)
    # orkestrator (når)
    f.text("_", 1000, 530, "NÅR", 15, PT, 700)
    f.text("_", 1048, 530, "· orkestrator, valgfri", 15, C["grey"], 600)
    f.rect("_", 1000, 544, 380, 44, C["white"], C["purple"], 2, 22, dash="7 5")
    f.text("_", 1190, 572, "Tidsplan · Workflows · Airflow · manuelt", 15, PT, 700, "middle")
    f.arrow("_", [(1190, 588), (1190, 602)], C["dark"], 2.5, hs=8)
    f.text("_", 1200, 600, "", 12, C["grey"])
    # jobbkontrakt
    f.rect("_", 260, 722, 740, 40, C["purplep"], C["purple"], 2, 20)
    f.text("_", 630, 748, "Jobbkontrakt: container · entrypoint · miljøvariabler · exitkode", 15, PT, 700, "middle")
    # ressurser
    res = [(1000, "Bøtter (GCS)", "input og output"), (1130, "Secret Manager", "hemmeligheter"), (1260, "Cloud Logging", "logger og metrikker")]
    for x, t, s in res:
        f.rect("_", x, 856, 120, 90, C["white"], C["dark"], 1.5, 8)
        f.lines("_", x + 60, 886, t.split(" ", 1) if len(t) > 12 else [t], 14, C["ink"], 700, "middle", 17)
        f.text("_", x + 60, 932, s, 11, C["grey"], 400, "middle")
        f.arrow("_", [(x + 60, 754), (x + 60, 854)], C["dark"] if x != 1000 else C["green"], 2, hs=8)
    f.lines("_", 260, 866, ["Plattformen standardiserer kontrakt og", "rammer (navn, policy, logging, merking),", "ikke teamenes forretningslogikk."], 15, C["dark"], lh=21)

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    f.rect("_", 60, y - 20, 26, 24, C["white"], C["purple"], 2.5, 4, dash="7 5")
    f.text("_", 96, y, "Forslag, ikke vedtatt", 16, C["dark"])
    f.rect("_", 290, y - 20, 26, 24, C["purplep"], C["purple"], 2, 4)
    f.text("_", 326, y, "Godkjenning / kontrakt", 16, C["dark"])
    f.arrow("_", [(530, y - 6), (570, y - 6)], C["dark"], 2.5, hs=9)
    f.text("_", 580, y, "Leveres videre", 16, C["dark"])
    f.text("_", 1860, y, f"Utkast {DATO} · Kilder: Dapla-manualen, notat om orkestrering (forslag), ADR0026", 15, C["grey"], 400, "end")
    frame(f, FR)
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in V:
        open(os.path.join(out, "teknisk-" + v["file"]), "w", encoding="utf-8").write(build(v).svg())
    open(os.path.join(out, "teknisk-prosess-3-endringsflyt.svg"), "w", encoding="utf-8").write(build_change().svg())
    print("ok")
