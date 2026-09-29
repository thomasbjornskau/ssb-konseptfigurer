"""Bedre faktaformidling – figursamling. Felles rammeverk + F2, F3, F1, F9, F11 (oversikter).
Farger (bestilling): grønt = data/statistikk/metadata, lilla = brukere/roller/ansvar,
blågrønt = plattform/tjenester/flater, grått = uavklart/forslag/utenfor scope, stiplet = forslag/uavklart."""
import os, math
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "29.09.2026"
PT = "#4b2fb0"
GREYF = "#f3f5f5"
GREYS = "#b9c5c6"
U = "5 4"
G = "_"
FONT = "Open Sans, Segoe UI, Arial, sans-serif"


# ---------- felles byggeklosser ----------
def frame(f, title, sub, tag, panel, items, legend, status="Utkast til diskusjon, ikke kvalitetssikret"):
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, title, 46, C["ink"], 700)
    f.text("_", 60, 136, sub, 24, C["grey"])
    w = max(170, len(tag) * 11 + 40)
    f.rect("_", 1860 - w, 62, w, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1860 - w / 2, 89, tag, 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')
    f.rect("_", 1440, 180, 420, 806, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, panel, 25, C["ink"], 700)
    y = 276
    for i, (h, b) in enumerate(items):
        f.badge(1485, y - 8, i + 1)
        f.text("_", 1516, y, h, 20, C["ink"], 700)
        f.lines("_", 1516, y + 27, b, 17, C["dark"], lh=23)
        y += 27 + len(b) * 23 + 24
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    x, yb = 60, 1046
    for kind, lab in legend:
        x = legend_item(f, x, yb, kind, lab)
    f.text("_", 1860, yb, f"{DATO} · {status}", 15, C["grey"], 400, "end")


def legend_item(f, x, y, kind, lab):
    if kind == "flate":
        f.rect("_", x, y - 20, 26, 24, C["tealp"], C["dark"], 1.8, 5)
    elif kind == "data":
        f.rect("_", x, y - 18, 26, 20, C["greenp"], C["green"], 1.5, 10)
    elif kind == "rolle":
        f.rect("_", x, y - 20, 26, 24, C["purplep"], C["purple"], 1.8, 5)
    elif kind == "uavklart":
        f.rect("_", x, y - 20, 26, 24, C["white"], C["grey"], 1.6, 5, dash=U)
    elif kind == "utenfor":
        f.rect("_", x, y - 20, 26, 24, GREYF, GREYS, 1.6, 5)
    elif kind == "forslag":
        f.rect("_", x, y - 20, 26, 24, C["white"], C["purple"], 2, 5, dash="6 4")
    elif kind.startswith("line:"):
        _, color, dash = kind.split(":")
        f.arrow("_", [(x, y - 7), (x + 40, y - 7)], C[color] if color in C else color, 2.5, dash=dash or None, hs=9)
        f.text("_", x + 50, y, lab, 16, C["dark"])
        return x + 50 + len(lab) * 8.6 + 34
    f.text("_", x + 36, y, lab, 16, C["dark"])
    return x + 36 + len(lab) * 8.6 + 30


def flate(f, x, y, w, h, title, sub=(), chips=(), unclear=None, dash=None, fill=None, stroke=None):
    f.rect(G, x, y, w, h, fill or C["tealp"], stroke or C["dark"], 1.8, 8, dash=dash)
    f.text(G, x + 14, y + 28, title, 18, C["ink"] if not dash else C["grey"], 700)
    for i, s in enumerate(sub):
        f.text(G, x + 14, y + 50 + i * 19, s, 14, C["grey"])
    cx = x + 14
    cy = y + h - 34
    for c in chips:
        chip(f, cx, cy, c)
        cx += len(c) * 7.2 + 30
    if unclear:
        ww = len(unclear) * 7 + 22
        f.rect(G, x + w - ww - 10, y + h - 33, ww, 22, C["white"], C["grey"], 1.2, 11, dash=U)
        f.text(G, x + w - ww / 2 - 10, y + h - 18, unclear, 12, C["grey"], 600, "middle")


def chip(f, x, y, label, kind="data"):
    w = len(label) * 7.2 + 22
    if kind == "data":
        f.rect(G, x, y, w, 24, C["greenp"], C["green"], 1.3, 12)
        f.text(G, x + w / 2, y + 17, label, 12.5, C["green"], 700, "middle")
    elif kind == "uavklart":
        f.rect(G, x, y, w, 24, C["white"], C["grey"], 1.3, 12, dash=U)
        f.text(G, x + w / 2, y + 17, label, 12.5, C["grey"], 700, "middle")
    return w


def label(f, x, y, text, color=None, anchor="start", size=13, weight=600):
    f.text(G, x, y, text, size, color or C["grey"], weight, anchor)


def save(f, name):
    out = utdata("bedre-faktaformidling")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, name), "w", encoding="utf-8").write(f.svg())


# ---------- F2 SSBs formidlingsøkosystem ----------
def f2(v=None):
    global G
    f = Fig(v["hi"] if v else None)
    if v:
        frame(f, v["title"], v["sub"], v["tag"], v["panel"], v["items"], v["legend"])
    else:
      frame(f, "SSBs formidlingsøkosystem", "Flatene, rollene og grenseflatene. Ikke én løsning, og det skal det heller ikke være", "Oversikt",
            "Slik leses figuren",
            [("Flere flater, ulike roller", ["Hver flate har sine brukere og", "sitt ansvar. Figuren viser roller,", "ikke én sammenhengende reise."]),
             ("Det juridiske skillet", ["Åpent publisert statistikk og", "tilgangsstyrte mikrodata har", "ulike regler. Skillet skal synes."]),
             ("Metadata bor for seg", ["Klass og Vardef er egne tjenester.", "Hvordan de følger tallene ut til", "flatene, er delvis uavklart."]),
             ("Utenfor SSB", ["Andre høster, gjengir og tolker", "tallene. Det påvirker vi, men", "styrer det ikke."])],
            [("flate", "Flate eller tjeneste"), ("data", "Hva den bærer"), ("rolle", "Brukere"), ("utenfor", "Utenfor SSB"),
             ("uavklart", "Uavklart"), ("line:grey:5 4", "Uavklart grenseflate")])

    # brukere
    G = "users"
    f.text(G, 155, 206, "Brukere", 20, C["ink"], 700, "middle")
    for cy, lab in [(292, "Allmennheten"), (412, "Journalister"), (532, "Analytikere"), (652, "Forskere")]:
        f.person(G, 155, cy, 0.95, C["purple"])
        f.text(G, 155, cy + 52, lab, 16, PT, 600, "middle")
    f.rect(G, 76, 760, 158, 120, C["white"], C["grey"], 1.5, 8, dash=U)
    f.lines(G, 155, 794, ["Hvem bruker", "hvilken flate?", "Må kartlegges"], 14, C["grey"], 600, "middle", 20)

    # SSB-sone
    G = "ssb"
    f.rect(G, 272, 180, 832, 806, C["white"], C["dark"], 2.5, 14)
    f.text(G, 292, 210, "SSB", 20, C["ink"], 700)
    # åpent
    G = "openband"
    f.rect(G, 288, 226, 800, 500, "#f8fbfb", C["line"], 1.5, 10)
    label(f, 304, 250, "ÅPENT TILGJENGELIG", C["dark"], size=14, weight=700)
    gx = [304, 564, 824]
    heads = ["Publisert statistikk", "Metadata og katalog", "Kode og forskning"]
    for x, h in zip(gx, heads):
        f.text(G, x, 282, h, 15, C["grey"], 700)
    W = 248
    G = "pub"
    flate(f, gx[0], 296, W, 118, "ssb.no", ["artikler og nøkkeltall,", "lenker til Statistikkbanken"], ["Om statistikken"])
    flate(f, gx[0], 432, W, 118, "Statistikkbanken", ["tabeller for alle", "publiserte statistikker"], ["statistikk"])
    flate(f, gx[0], 568, W, 118, "API", ["Statistikkbankens API,", "maskinlesbar tilgang"], ["statistikk"])
    G = "meta"
    flate(f, gx[1], 296, W, 118, "SSB Dataportal", ["datakatalog"], ["metadata"], unclear="rolle uavklart")
    flate(f, gx[1], 432, W, 118, "Klass", ["klassifikasjoner og", "kodelister"], ["metadata"])
    flate(f, gx[1], 568, W, 118, "Vardef", ["variabeldefinisjoner"], ["metadata"])
    G = "code"
    flate(f, gx[2], 296, 248, 118, "GitHub", ["kode og metode"], ["kode"], unclear="omfang uavklart")
    flate(f, gx[2], 432, 248, 118, "Forskning", ["artikler og rapporter"], ["analyser"])
    # grenseflate: metadata inn i Dataportalen
    G = "meta"
    f.arrow(G, [(688, 432), (688, 416)], C["grey"], 2, dash=U, hs=8)
    label(f, 698, 427, "inngår i?", size=12)

    # juridisk skille
    G = "skille"
    f.add(f'<line x1="288" y1="740" x2="1088" y2="740" stroke="{f.col(G,"stroke",C["purple"])}" stroke-width="3" stroke-dasharray="10 6"/>')
    f.rect(G, 560, 728, 256, 26, C["white"], C["purple"], 1.5, 13)
    f.text(G, 688, 746, "juridisk og faglig skille", 14, PT, 700, "middle")
    # tilgangsstyrt
    G = "restricted"
    f.rect(G, 288, 758, 800, 212, "#faf9ff", C["purplel"], 1.5, 10)
    label(f, 304, 784, "TILGANGSSTYRT · KREVER AVTALE ELLER SØKNAD", PT, size=14, weight=700)
    flate(f, gx[0], 800, W, 150, "microdata.no", ["analyse av registerdata", "for godkjente brukere"], ["mikrodata"])
    flate(f, gx[1], 800, W, 150, "Forskertilgang", ["søknad om mikrodata", "til forskning"], ["mikrodata"])
    f.rect(G, gx[2], 800, 248, 150, C["white"], C["grey"], 1.5, 8, dash=U)
    f.lines(G, gx[2] + 14, 828, ["Søknadsportal og", "avtaler"], 18, C["grey"], 700, lh=22)
    f.text(G, gx[2] + 14, 880, "hvordan dette henger", 14, C["grey"])
    f.text(G, gx[2] + 14, 899, "sammen, må beskrives", 14, C["grey"])

    # utenfor SSB
    G = "out"
    f.rect(G, 1124, 180, 280, 806, GREYF, GREYS, 2, 14)
    f.text(G, 1144, 210, "Utenfor SSB", 20, C["ink"], 700)
    outs = [(240, "Eksterne kataloger", ["data.norge.no, Eurostat"]), (372, "KI-verktøy", ["gjengir og tolker tall"]),
            (504, "Medier", ["formidler videre"]), (636, "Andre produsenter", ["for eksempel NAV"])]
    for y, t, s in outs:
        f.rect(G, 1140, y, 248, 112, C["white"], GREYS, 1.5, 8)
        f.text(G, 1154, y + 30, t, 18, C["ink"], 700)
        f.text(G, 1154, y + 54, s[0], 14, C["grey"])
    # grenseflater ut
    G = "lines"
    f.arrow(G, [(428, 686), (428, 710), (1112, 710), (1112, 428), (1138, 428)], C["grey"], 2.2, dash=U, hs=9)
    label(f, 940, 703, "høstes og gjengis", size=12)
    f.arrow(G, [(790, 296), (790, 258), (1114, 258), (1114, 296), (1138, 296)], C["grey"], 2.2, dash=U, hs=9)
    label(f, 940, 251, "høstes? (uavklart)", size=12)
    for k, (bx, by) in enumerate(v.get("badges", []) if v else []):
        f.badge(bx, by, k + 1)
    G = "_"
    save(f, v["file"] if v else "ff-F2-okosystem.svg")




# ---------- F3 Autoritetskjeden bak et tall ----------
def f3():
    f = Fig(None)
    frame(f, "Autoritetskjeden bak et tall", "Hva et publisert tall må kunne spores tilbake til, og hvor hvert ledd har sitt hjem", "Oversikt",
          "Slik leses figuren",
          [("Autoritet er en kjede", ["Tallet er bare så troverdig som", "det svakeste leddet bak det."]),
           ("Fem spørsmål", ["Leddene er gruppert etter hva en", "bruker lurer på, ikke etter", "hvilket system de ligger i."]),
           ("Hvert ledd har et hjem", ["Under hvert ledd står hvor det", "ligger i dag. Stiplet betyr at", "hjemmet ikke er avklart."]),
           ("Status er ikke vurdert", ["Om leddet er koblet maskinelt,", "manuelt eller ikke i det hele", "tatt, fylles ut med metadata-", "miljøet."])],
          [("data", "Ledd i kjeden"), ("rolle", "Ansvar"), ("flate", "Hvor det ligger"), ("uavklart", "Uavklart hjem")])

    # publisert tall
    f.rect("_", 60, 300, 230, 380, C["white"], C["green"], 2.5, 12)
    f.text("_", 175, 336, "Publisert tall", 20, C["ink"], 700, "middle")
    # liten tabell
    tx, ty = 86, 360
    for r in range(4):
        for c in range(3):
            fill = C["green"] if (r, c) == (2, 1) else (C["greenp"] if r == 0 else C["white"])
            f.rect("_", tx + c * 60, ty + r * 34, 58, 32, fill, C["green"], 1, 2)
    f.text("_", tx + 90, ty + 2 * 34 + 22, "x,x", 15, C["white"], 700, "middle")
    f.lines("_", 175, 530, ["i Statistikkbanken,", "på ssb.no eller", "gjengitt av andre"], 15, C["dark"], 400, "middle", 21)
    f.lines("_", 175, 620, ["Hva må følge med", "for at det kan brukes", "trygt?"], 14, C["grey"], 600, "middle", 19)

    groups = [
        ("Hva er tallet?", "data", [("Tabell", "Statistikkbanken"), ("Statistikkprodukt", "Statistikkregisteret")]),
        ("Hva betyr det?", "data", [("Begrep", None), ("Variabeldefinisjon", "Vardef"), ("Klassifikasjon", "Klass")]),
        ("Hvordan er det laget?", "data", [("Datasett", "Datadoc"), ("Datagrunnlag og kilder", "Kudoc"), ("Metode", "Om statistikken"), ("Kode", "GitHub")]),
        ("Hvor godt og trygt?", "data", [("Kvalitet", "kvalitetsindikatorer*"), ("Usikkerhet og forbehold", "Om statistikken"), ("Konfidensialitet og personvern", None)]),
        ("Hvem står bak?", "rolle", [("Ansvarlig seksjon", "Statistikkregisteret"), ("Kontaktperson", "Statistikkregisteret")]),
    ]
    X0, GW, GG = 320, 206, 10
    # sporingslinje
    f.add(f'<line x1="290" y1="276" x2="{X0 + 5*GW + 4*GG - 20}" y2="276" stroke="{C["dark"]}" stroke-width="2.5"/>')
    f.add(f'<line x1="290" y1="276" x2="290" y2="300" stroke="{C["dark"]}" stroke-width="2.5"/>')
    label(f, 300, 268, "sporbart tilbake til", C["dark"], size=13, weight=700)
    for gi, (q, kind, links) in enumerate(groups):
        x = X0 + gi * (GW + GG)
        f.rect("_", x, 184, GW, 64, C["dark"] if kind == "data" else C["purple"], C["dark"] if kind == "data" else C["purple"], 0, 10)
        f.text("_", x + 14, 222, q, 16.5, C["white"], 700)
        f.arrow("_", [(x + GW / 2, 276), (x + GW / 2, 298)], C["dark"], 2, hs=8)
        y = 300
        for name, home in links:
            fill, st = (C["greenp"], C["green"]) if kind == "data" else (C["purplep"], C["purple"])
            f.rect("_", x, y, GW, 124, fill, st, 1.8, 8)
            words = name.split(" ")
            ln = [name] if len(name) <= 20 else [" ".join(words[:-1]), words[-1]] if len(" ".join(words[:-1])) <= 20 else [" ".join(words[:2]), " ".join(words[2:])]
            f.lines("_", x + 12, y + 28, ln, 16, C["ink"], 700, lh=20)
            # status (ikke vurdert)
            f.add(f'<circle cx="{x+GW-18}" cy="{y+20}" r="9" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="1.6" stroke-dasharray="3 2"/>')
            f.text("_", x + GW - 18, y + 25, "?", 12, C["grey"], 700, "middle")
            label(f, x + 12, y + 84, "ligger i", size=12)
            if home:
                w = len(home) * 7 + 20
                f.rect("_", x + 12, y + 92, min(w, GW - 24), 24, C["tealp"], C["dark"], 1.3, 5)
                f.text("_", x + 12 + min(w, GW - 24) / 2, y + 109, home, 12.5, C["dark"], 700, "middle")
            else:
                f.rect("_", x + 12, y + 92, 110, 24, C["white"], C["grey"], 1.3, 5, dash=U)
                f.text("_", x + 67, y + 109, "ikke avklart", 12.5, C["grey"], 700, "middle")
            y += 134

    # statusbånd
    f.rect("_", 60, 850, 1340, 134, C["white"], C["dark"], 1.5, 12)
    f.text("_", 84, 884, "Status per ledd: ikke vurdert ennå", 19, C["ink"], 700)
    f.text("_", 84, 912, "Fylles ut med metadatamiljøet. Tre verdier:", 15, C["dark"])
    sx = 84
    for kind, lab in [("solid", "koblet maskinelt"), ("manual", "koblet manuelt"), ("none", "mangler kobling")]:
        if kind == "solid":
            f.add(f'<circle cx="{sx+10}" cy="{944}" r="9" fill="{C["green"]}"/>')
        elif kind == "manual":
            f.add(f'<circle cx="{sx+10}" cy="{944}" r="9" fill="{C["white"]}" stroke="{C["green"]}" stroke-width="3"/>')
        else:
            f.add(f'<circle cx="{sx+10}" cy="{944}" r="9" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="1.6" stroke-dasharray="3 2"/>')
        f.text("_", sx + 28, 950, lab, 16, C["dark"])
        sx += 28 + len(lab) * 8.6 + 40
    f.text("_", 760, 884, "Spørsmålet som avgjør rekkefølgen", 16, C["ink"], 700)
    f.lines("_", 760, 910, ["Hvilke ledd må en maskin kunne følge for at tallet", "kan siteres trygt av andre, også av KI?"], 15, C["dark"], lh=21)
    label(f, 1400 - 12, 976, "* under arbeid", size=12, anchor="end")
    save(f, "ff-F3-autoritetskjede.svg")


# ---------- F1 Fra spørsmål til autoritativt svar ----------
def step_head(f, x, n, text):
    f.badge(x + 19, 206, n)
    f.text("_", x + 48, 213, text, 19, C["ink"], 700)


def f1():
    f = Fig(None)
    frame(f, "Fra spørsmål til autoritativt svar", "Hva som må følge med for at et enkelt spørsmål får et SSB-svar, ikke bare et tall", "Oversikt",
          "Slik leses figuren",
          [("Brukerens ord er ikke begrepet", ["«Arbeidsledighet» kan bety to", "ulike statistikker fra to ulike", "kilder. Svaret må si hvilken."]),
           ("Svaret har lag", ["Tallet øverst. Under det: hva det", "betyr, hvor sikkert det er, og", "hvor det kommer fra."]),
           ("Forbehold hører til svaret", ["Usikkerhet, sesongjustering og", "revisjoner er ikke fotnoter. De", "er en del av autoriteten."]),
           ("Svaret peker videre", ["Til tabell, nærliggende statistikk,", "andre kilder og dypere analyse."])],
          [("rolle", "Bruker"), ("data", "Innhold i svaret"), ("flate", "Hvor det hentes"), ("utenfor", "Utenfor SSB"), ("uavklart", "Uavklart")],
          status="Utkast til diskusjon · eksempelet må kvalitetssikres av fagseksjonen")

    # 1 spørsmål
    step_head(f, 60, 1, "Spørsmålet")
    f.person("_", 110, 300, 1.0, C["purple"])
    f.rect("_", 60, 350, 240, 150, C["purplep"], C["purple"], 2, 14)
    f.add(f'<polygon points="96,350 116,350 104,332" fill="{C["purplep"]}" stroke="{C["purple"]}" stroke-width="2"/>')
    f.add(f'<line x1="97" y1="350" x2="115" y2="350" stroke="{C["purplep"]}" stroke-width="3"/>')
    f.lines("_", 80, 392, ["«Hva var", "arbeidsledigheten", "forrige måned?»"], 20, PT, 700, lh=28)
    label(f, 80, 528, "brukerens egne ord", size=14)
    f.rect("_", 60, 560, 240, 88, C["white"], C["grey"], 1.5, 8, dash=U)
    f.lines("_", 76, 590, ["Uavklart: betyr «forrige", "måned» referanseperiode", "eller siste publisering?"], 14, C["grey"], 600, lh=19)

    # 2 tolkning
    step_head(f, 330, 2, "Tolkningen")
    f.rect("_", 330, 290, 260, 120, C["greenp"], C["green"], 3, 10)
    f.text("_", 346, 322, "Arbeidsledighet", 18, C["ink"], 700)
    f.text("_", 346, 346, "Arbeidskraftundersøkelsen", 14, C["dark"])
    chip_x = 346
    f.rect("_", chip_x, 366, 50, 26, C["tealp"], C["dark"], 1.3, 5)
    f.text("_", chip_x + 25, 384, "SSB", 13, C["dark"], 700, "middle")
    f.rect("_", 330, 440, 260, 110, GREYF, GREYS, 1.8, 10)
    f.text("_", 346, 472, "Registrert ledighet", 18, C["ink"], 700)
    f.text("_", 346, 496, "helt ledige hos NAV", 14, C["dark"])
    f.rect("_", 346, 512, 50, 26, C["white"], GREYS, 1.3, 5)
    f.text("_", 371, 530, "NAV", 13, C["grey"], 700, "middle")
    f.arrow("_", [(300, 425), (316, 425), (316, 350), (328, 350)], C["dark"], 2.5, hs=9)
    f.arrow("_", [(316, 425), (316, 495), (328, 495)], C["grey"], 2, dash=U, hs=9)
    f.lines("_", 330, 590, ["To begreper, to kilder,", "to tall. Svaret må si hvilket", "det er, og nevne det andre."], 15, C["dark"], lh=21)
    f.rect("_", 330, 668, 260, 34, C["white"], C["dark"], 1.3, 17)
    f.text("_", 460, 690, "brukerord → begrep (se F4)", 13, C["dark"], 700, "middle")

    # 3 svaret i lag
    step_head(f, 630, 3, "Svaret, i lag")
    label(f, 630, 250, "det brukeren ser først, står øverst", size=13)
    layers = [("Tallet", [("nøkkeltall x,x %", "data"), ("referanseperiode", "data")], "ssb.no", True),
              ("Hva det betyr", [("definisjon", "data"), ("statistikkprodukt", "data")], "Om statistikken", True),
              ("Hvor sikkert", [("usikkerhet", "data"), ("sesongjustering", "data"), ("revisjoner", "data")], "Om statistikken", True),
              ("Hvor det kommer fra", [("metode", "data"), ("tabell og API", "data")], "Statistikkbanken", True)]
    y = 264
    for i, (name, chips_, src, sure) in enumerate(layers):
        h = 128
        f.rect("_", 630, y, 470, h, C["white"], C["green"], 1.8, 10)
        f.rect("_", 630, y, 10, h, C["green"] if i == 0 else C["greenl"], C["green"], 0, 0)
        f.text("_", 656, y + 32, f"{i+1}  {name}", 18, C["ink"], 700)
        cx = 656
        for c, k in chips_:
            cx += chip(f, cx, y + 50, c, k) + 8
        f.text("_", 656, y + 106, "hentes fra", 12, C["grey"], 600)
        w = len(src) * 7.2 + 22
        f.rect("_", 726, y + 90, w, 24, C["tealp"], C["dark"], 1.3, 5)
        f.text("_", 726 + w / 2, y + 107, src, 12.5, C["dark"], 700, "middle")
        y += h + 10
    f.arrow("_", [(590, 350), (628, 350)], C["green"], 3, hs=10)

    # 4 videre
    step_head(f, 1130, 4, "Videre")
    nexts = [("Tidsserie og tabell", "Statistikkbanken", "flate"), ("Nærliggende statistikk", "for eksempel sysselsetting", "data"),
             ("Registrert ledighet", "NAV", "utenfor"), ("Dypere analyse", "microdata.no, tilgangsstyrt", "rolle")]
    y = 264
    for t, s, k in nexts:
        fill, st = {"flate": (C["tealp"], C["dark"]), "data": (C["greenp"], C["green"]), "utenfor": (GREYF, GREYS),
                    "rolle": (C["purplep"], C["purple"])}[k]
        f.rect("_", 1130, y, 270, 100, fill, st, 1.8, 10)
        f.text("_", 1146, y + 34, t, 17, C["ink"], 700)
        f.text("_", 1146, y + 60, s, 14, C["dark"])
        f.arrow("_", [(1100, y + 50), (1128, y + 50)], C["dark"], 2, hs=8)
        y += 138

    # uavklart bunnbånd
    f.rect("_", 60, 830, 530, 150, C["white"], C["grey"], 1.5, 12, dash=U)
    f.text("_", 80, 864, "Uavklart", 18, C["ink"], 700)
    f.lines("_", 80, 892, ["Hvilken flate gir svaret: ssb.no, søk eller assistent?", "Finnes usikkerhet og forbehold maskinlesbart?",
                           "Hva er minstekravet for et SSB-svar?"], 15, C["dark"], lh=24)
    save(f, "ff-F1-sporsmal-til-svar.svg")


# ---------- F9 Strategisk avklaringskart ----------
def qnode(f, x, y, w, h, q, tags):
    f.rect("_", x, y, w, h, C["white"], C["dark"], 1.8, 10)
    ql = q.split("|")
    f.lines("_", x + 16, y + 34, ql, 19, C["ink"], 700, lh=24)
    cx = x + 16
    y += (len(ql) - 1) * 24
    for t in tags:
        style = {"flate": (C["tealp"], C["dark"], C["dark"]), "ansvar": (C["purplep"], C["purple"], PT),
                 "juridisk": (C["purplep"], C["purple"], PT), "metadata": (C["greenp"], C["green"], C["green"]),
                 "KI": (C["white"], C["dark"], C["dark"])}[t]
        wv = len(t) * 7.4 + 22
        f.rect("_", cx, y + 50, wv, 24, style[0], style[1], 1.3, 12)
        f.text("_", cx + wv / 2, y + 67, t, 12.5, style[2], 700, "middle")
        cx += wv + 8
    # status og beslutter
    y -= (len(ql) - 1) * 24
    f.add(f'<circle cx="{x+26}" cy="{y+h-24}" r="9" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="1.6" stroke-dasharray="3 2"/>')
    f.text("_", x + 26, y + h - 19, "?", 12, C["grey"], 700, "middle")
    f.text("_", x + 44, y + h - 19, "status  ·  beslutter: ?", 13, C["grey"], 600)


def f9():
    f = Fig(None)
    frame(f, "Hva må avklares først?", "Spørsmålene som må ha svar før framtidens løsning kan tegnes, i foreslått rekkefølge", "Diskusjon",
          "Slik leses figuren",
          [("Rolle før løsning", ["De viktigste valgene handler om", "roller og ansvar, ikke om", "teknologi."]),
           ("Tre trinn", ["Flatenes rolle, så ansvar og", "eierskap, så nye kanaler.", "Rekkefølgen er et forslag."]),
           ("Hver beslutning trenger en eier", ["Uten en beslutter blir svarene", "anbefalinger som ingen står bak."]),
           ("Status fylles ut", ["Om spørsmålet er avklart, delvis", "avklart eller åpent, avgjør", "prosjektet. Figuren gjetter ikke."])],
          [("flate", "Flate"), ("rolle", "Ansvar eller juridisk"), ("data", "Metadata"), ("forslag", "Foreslått rekkefølge"), ("uavklart", "Ikke vurdert")])

    stages = [(60, 360, "1  Flatenes rolle", [("Hva er ssb.no?", ["flate"]), ("Hva er Statistikkbanken?", ["flate"]),
                                                ("Hva er Dataportalen?", ["flate", "metadata"]), ("Hva er mikrodatatilgang?", ["flate", "juridisk"])]),
              (470, 360, "2  Ansvar og eierskap", [("Hva er metadataforvaltning?", ["metadata", "ansvar"]), ("Hvem eier hva?", ["ansvar"])]),
              (880, 330, "3  Nye kanaler", [("Hva er KI-assistentens|ansvar?", ["KI", "ansvar", "juridisk"])])]
    for x, w, head, qs in stages:
        f.rect("_", x, 184, w, 802, "#f8fbfb", C["line"], 1.5, 12)
        f.text("_", x + 18, 218, head, 20, C["ink"], 700)
        n = len(qs)
        h = 150
        total = n * h + (n - 1) * 22
        y = 240 + (740 - total) / 2 if n < 4 else 250
        for q, tags in qs:
            ww = w - 36
            qnode(f, x + 18, y, ww, h, q if len(q) < 26 else q, tags)
            y += h + 22
    # pil mellom trinn
    for x1, x2 in [(422, 470), (832, 880), (1212, 1240)]:
        f.arrow("_", [(x1, 585), (x2 - 2, 585)], C["purple"], 3.5, dash="8 5", hs=13)
    label(f, 446, 572, "før", PT, "middle", 13, 700)
    label(f, 856, 572, "før", PT, "middle", 13, 700)
    # så: tegne løsningen
    f.rect("_", 1242, 470, 158, 230, C["white"], C["grey"], 1.8, 12, dash=U)
    f.lines("_", 1321, 548, ["Så:", "tegne", "framtidens", "løsning"], 17, C["grey"], 700, "middle", 24)
    save(f, "ff-F9-avklaringskart.svg")


# ---------- F11 Hva SSB styrer, påvirker og ikke styrer ----------
def pill(f, cx, cy, text, fill, stroke, tc, size=13.5, dash=None):
    w = len(text) * (size * 0.56) + 24
    f.rect("_", cx - w / 2, cy - 14, w, 28, fill, stroke, 1.4, 14, dash=dash)
    f.text("_", cx, cy + 5, text, size, tc, 700, "middle")


def f11():
    f = Fig(None)
    frame(f, "Hva SSB styrer, påvirker og ikke styrer", "Hvor vi har kontroll, hvor vi kan påvirke, og hva andre gjør uansett", "Oversikt",
          "Slik leses figuren",
          [("Tre sirkler", ["Innerst det SSB bestemmer selv.", "Så det vi kan påvirke. Ytterst", "det andre avgjør."]),
           ("KI-svarene styrer vi ikke", ["Generelle KI-verktøy velger selv", "kilder og formuleringer."]),
           ("Det innerste virker utover", ["Maskinlesbare begreper, forbehold", "og siterbare tall gjør gode svar", "enklest å gi, også for andre."]),
           ("Brukerens behov er likt", ["Brukeren vil ha et raskt svar", "å stole på, uansett hvor", "spørsmålet stilles."])],
          [("flate", "Styrer"), ("rolle", "Påvirker"), ("utenfor", "Styrer ikke"), ("forslag", "Foreslåtte tiltak"), ("uavklart", "Uavklart")])

    cx, cy = 520, 598
    f.add(f'<circle cx="{cx}" cy="{cy}" r="400" fill="{GREYF}" stroke="{GREYS}" stroke-width="2"/>')
    f.add(f'<circle cx="{cx}" cy="{cy}" r="275" fill="{C["purplep"]}" stroke="{C["purple"]}" stroke-width="2"/>')
    f.add(f'<circle cx="{cx}" cy="{cy}" r="150" fill="{C["tealp"]}" stroke="{C["dark"]}" stroke-width="2.5"/>')
    f.text("_", cx, cy - 400 + 34, "STYRER IKKE", 15, C["grey"], 700, "middle")
    f.text("_", cx, cy - 275 + 32, "PÅVIRKER", 15, PT, 700, "middle")
    f.text("_", cx, cy - 150 + 34, "STYRER", 15, C["dark"], 700, "middle")
    # innerst
    for i, t in enumerate(["ssb.no og Dataportalen", "Statistikkbanken og API", "Klass og Vardef", "Om statistikken", "Lisens og sitering"]):
        pill(f, cx, 510 + i * 38, t, C["white"], C["dark"], C["dark"], 12.5)
    # påvirker
    pill(f, cx, 380, "Eksterne kataloger", C["white"], C["purple"], PT)
    pill(f, cx, 818, "Internasjonale standarder", C["white"], C["purple"], PT)
    pill(f, 308, cy, "Medier", C["white"], C["purple"], PT)
    pill(f, 690, 462, "KI-leverandører", C["white"], C["purple"], PT, 12.5)
    # styrer ikke
    pill(f, cx, 262, "Hvordan KI-verktøy svarer", C["white"], GREYS, C["grey"])
    pill(f, cx, 900, "Hvilke kilder de velger", C["white"], GREYS, C["grey"])
    pill(f, cx, 944, "Brukernes forventning om raske svar", C["white"], GREYS, C["grey"])

    # høyre side
    X = 968
    f.rect("_", X, 184, 432, 236, C["purplep"], C["purple"], 2, 12)
    f.person("_", X + 40, 232, 0.8, C["purple"])
    f.text("_", X + 80, 232, "Brukeren ønsker", 20, PT, 700)
    for i, t in enumerate(["et raskt svar", "å kunne stole på svaret", "å forstå hva tallet betyr", "å finne veien videre"]):
        f.text("_", X + 26, 284 + i * 32, "·  " + t, 17, C["ink"])
    f.rect("_", X, 446, 432, 290, C["white"], C["purple"], 2, 12, dash="7 5")
    f.text("_", X + 22, 482, "Det som virker utover", 20, C["ink"], 700)
    f.text("_", X + 22, 508, "tiltak innerst, foreslått", 14, C["grey"])
    for i, t in enumerate(["Maskinlesbare begreper og forbehold", "Stabile lenker og siterbare tall", "API-er som leverer metadata med tallene", "Tydelig lisens for maskinell bruk"]):
        f.rect("_", X + 22, 528 + i * 50, 388, 38, C["greenp"], C["green"], 1.3, 8)
        f.text("_", X + 36, 553 + i * 50, t, 15, C["green"], 700)
    f.arrow("_", [(cx + 150, cy), (X - 4, cy)], C["purple"], 3.5, dash="8 5", hs=13)
    f.rect("_", 836, cy - 44, 108, 26, C["white"], C["purple"], 1.3, 13)
    f.text("_", 890, cy - 26, "virker utover", 13, PT, 700, "middle")
    f.rect("_", X, 762, 432, 222, C["white"], C["grey"], 1.5, 12, dash=U)
    f.text("_", X + 22, 798, "Uavklart", 19, C["ink"], 700)
    f.lines("_", X + 22, 828, ["Hvor mye kan SSB påvirke KI-leverandører", "i praksis?", "Hva gjør vi når et KI-verktøy gjengir", "et SSB-tall feil?", "Er lisensen tilpasset maskinell bruk?"], 15, C["dark"], lh=24)
    save(f, "ff-F11-styrer-pavirker.svg")


# ---------- Introduksjon: matrise og figuroversikt ----------
FIG = {1: "Fra spørsmål til svar", 2: "Formidlings-|økosystemet", 3: "Autoritetskjeden", 4: "Søk som|veivisning",
       5: "KI-assistent|som veiviser", 6: "Fleksibilitet|innenfor rammer", 7: "Dataportalen:|sandkasse?", 8: "Brukerreise|før og etter",
       9: "Avklaringskart", 10: "To scenarioer|for 2050", 11: "Styrer, påvirker,|styrer ikke", 12: "Startpunkter|og piloter"}
DRAWN = set(range(1, 13))
FULL = {1: "Fra spørsmål til autoritativt svar", 2: "SSBs formidlingsøkosystem", 3: "Autoritetskjeden bak et tall",
        4: "Bedre søk er mer enn treffliste", 5: "KI-assistent som veiviser", 6: "Fleksibilitet innenfor faglige rammer",
        7: "Dataportalen: sandkasse eller autoritativ", 8: "Brukerreise i dag og framover", 9: "Strategisk avklaringskart",
        10: "To scenarioer for 2050", 11: "Hva SSB styrer, påvirker, ikke styrer", 12: "Startpunkter og piloter"}


def fchip(f, x, y, n, primary=True, small=False):
    w = 30 if small else 46
    h = 20 if small else 26
    if primary:
        fill, st, tc = (C["green"], C["green"], C["white"]) if n in DRAWN else (C["white"], C["dark"], C["dark"])
    else:
        fill, st, tc = C["white"], GREYS, C["grey"]
    f.rect("_", x, y, w, h, fill, st, 1.5 if primary else 1.2, h / 2)
    f.text("_", x + w / 2, y + h - (6 if small else 8), f"F{n}", 11 if small else 14, tc, 700, "middle")
    return w


def intro():
    f = Fig(None)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    f.text("_", 60, 92, "Tolv figurer for Bedre faktaformidling", 46, C["ink"], 700)
    f.text("_", 60, 136, "Én figur, ett spørsmål, én primær målgruppe", 24, C["grey"])
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, "Introduksjon", 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')
    f.lines("_", 60, 196, ["Mange miljøer ser hver sin del av samme sak. Figursamlingen gir hver målgruppe figurer som svarer på ett spørsmål",
                           "om gangen. Tolv figurer dekker de viktigste cellene. Tomme celler er bevisste."], 18, C["dark"], lh=26)

    persp = ["Verdi og bruker-|opplevelse", "Autoritet og|faglig ansvar", "Informasjons-|økosystem", "Metadata og|sporbarhet",
             "Flyt og|grenseflater", "KI og maskin-|lesbarhet", "Risiko og|avgrensning", "Startpunkter|og piloter"]
    aud = ["Strategisk|ledelse", "Prosjektgruppen", "Fagmiljøer", "Formidling og|kommunikasjon", "IT-arkitektur|og plattform",
           "Metadata- og|dataforvaltning", "Personvern, juridisk,|informasjonssikkerhet", "Profesjonelle|eksterne brukere"]
    # (rad, kol): (primær, [sekundære], merknad)
    M = {(0, 1): (10, [], None), (0, 2): (None, [2], None), (0, 5): (5, [], None), (0, 6): (9, [], None), (0, 7): (None, [12], None),
         (1, 0): (1, [], None), (1, 2): (None, [9], None), (1, 5): (11, [], None), (1, 7): (12, [], None),
         (2, 1): (6, [10], None), (2, 3): (None, [3], None),
         (3, 0): (4, [1, 8], None), (3, 5): (None, [11], None),
         (4, 2): (2, [], None), (4, 4): (None, [2, 3], None), (4, 6): (None, [7], None),
         (5, 2): (None, [2], None), (5, 3): (3, [], None), (5, 4): (None, [3], None), (5, 6): (7, [], None),
         (6, 1): (None, [6], None), (6, 4): (2, [], "fokus:|tilgangsregimer"), (6, 5): (None, [5], None),
         (7, 0): (8, [4], None)}
    RX, RW = 60, 222
    CX0, CW, CG = 290, 133, 6
    YH, HH = 244, 72
    RY, RH, RG = 324, 76, 4
    for j, p in enumerate(persp):
        x = CX0 + j * (CW + CG)
        f.rect("_", x, YH, CW, HH, C["dark"], C["dark"], 0, 8)
        f.lines("_", x + 12, YH + 30, p.split("|"), 14, C["white"], 700, lh=19)
    for i, a in enumerate(aud):
        y = RY + i * (RH + RG)
        f.rect("_", RX, y, RW, RH, C["purplep"], C["purplep"], 0, 8)
        al = a.split("|")
        f.lines("_", RX + 14, y + (RH / 2 + 5 if len(al) == 1 else RH / 2 - 5), al, 15, PT, 700, lh=20)
        for j in range(8):
            x = CX0 + j * (CW + CG)
            cell = M.get((i, j))
            if not cell:
                f.rect("_", x, y, CW, RH, "#f7f9f9", "#e8eded", 1, 6)
                continue
            prim, secs, note = cell
            f.rect("_", x, y, CW, RH, C["white"], C["dark"] if prim else "#dfe5e5", 1.8 if prim else 1.2, 6)
            cx = x + 10
            if prim:
                cx += fchip(f, cx, y + 8, prim) + 6
            for s in secs:
                cx += fchip(f, cx, y + 11, s, primary=False, small=True) + 4
            if prim:
                t = (note or FIG[prim]).split("|")
                f.lines("_", x + 10, y + 50, t, 11.5, C["ink"] if not note else C["grey"], 600, lh=15)
    # sidepanel: figuroversikt
    f.rect("_", 1440, 244, 420, 740, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 288, "Figurene", 24, C["ink"], 700)
    y = 330
    for n in range(1, 13):
        fchip(f, 1466, y - 18, n)
        f.text("_", 1524, y, FULL[n], 16, C["ink"] if n in DRAWN else C["dark"], 700 if n in DRAWN else 400)
        y += 52
    f.add(f'<line x1="1466" y1="{y-18}" x2="1834" y2="{y-18}" stroke="{C["line"]}" stroke-width="1"/>')
    f.text("_", 1466, y + 10, "Alle tolv er tegnet som utkast.", 15, C["grey"], 600)
    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    yb = 1046
    fchip(f, 60, yb - 20, 1); f.text("_", 116, yb - 2, "Primær figur, utkast tegnet", 16, C["dark"])
    DRAWN_backup = set(DRAWN)
    f.rect("_", 600, yb - 17, 30, 20, C["white"], GREYS, 1.2, 10); f.text("_", 615, yb - 3, "F2", 11, C["grey"], 700, "middle")
    f.text("_", 640, yb - 2, "Sekundær bruk", 16, C["dark"])
    f.rect("_", 790, yb - 20, 26, 24, "#f7f9f9", "#e8eded", 1, 5); f.text("_", 826, yb - 2, "Bevisst tom", 16, C["dark"])
    f.text("_", 1860, yb, f"{DATO} · Utkast · Kilde: storyboard for figursamlingen", 15, C["grey"], 400, "end")
    save(f, "ff-00-introduksjon.svg")


# ---------- F4 Bedre søk er mer enn treffliste ----------
def f4():
    f = Fig(None)
    frame(f, "Bedre søk er mer enn treffliste", "Fra dokumenttreff til faglig veivisning, vist med ett søkeord gjennom fem trinn", "Oversikt",
          "Slik leses figuren",
          [("Samme ord, fem trinn", ["Hvert trinn gjør mer av jobben", "for brukeren. Trinn 1 finnes", "i dag, resten er forslag."]),
           ("Trinn 2 er nøkkelen", ["Å koble brukerens ord til SSBs", "begrep åpner alle trinnene over."]),
           ("Innhold, ikke bare teknikk", ["Ordlister, relasjoner og", "forklaringer må lages og", "vedlikeholdes av noen."]),
           ("Maskinelt eller redaksjonelt", ["Jo høyere trinn, jo mer faglig", "skjønn. Fordelingen nederst er", "et forslag til diskusjon."])],
          [("rolle", "Det brukeren ser"), ("data", "Må finnes bak"), ("flate", "Finnes i dag"), ("forslag", "Forslag"), ("uavklart", "Uavklart")])

    # søkefelt
    f.rect("_", 60, 186, 420, 52, C["white"], C["dark"], 2, 26)
    f.add(f'<circle cx="92" cy="210" r="10" fill="none" stroke="{C["dark"]}" stroke-width="3"/>')
    f.add(f'<line x1="99" y1="217" x2="108" y2="226" stroke="{C["dark"]}" stroke-width="3" stroke-linecap="round"/>')
    f.text("_", 124, 219, "ledighet", 20, C["ink"], 700)
    label(f, 500, 219, "brukerens søkeord, likt gjennom alle trinn", size=14)

    steps = [
        ("Treffliste", True, ["Artikler og tabeller", "som inneholder ordet"], [("søkeindeks", "flate")], 0.1),
        ("Ord til begrep", False, ["«Mente du arbeidsledighet", "(AKU, SSB) eller registrert", "ledighet (NAV)?»"], [("brukerord-liste", "uavklart"), ("begrepsdefinisjoner", "data")], 0.45),
        ("Nærliggende statistikk", False, ["Sysselsetting, arbeids-", "styrken, permitterte"], [("relasjoner", "uavklart"), ("hvor de ligger?", "uavklart")], 0.3),
        ("Forklare forskjeller", False, ["«Derfor er tallene", "ulike, og slik velger", "du riktig»"], [("forklaringer", "data"), ("skrevet av fag", "data")], 0.8),
        ("Anbefalt inngang", False, ["«For utvikling måned", "for måned: start her»"], [("faglig vurdering", "data"), ("brukerbehov", "uavklart")], 0.9),
    ]
    W, G = 256, 15
    tops = [560, 490, 420, 350, 280]
    for i, (name, today, sees, behind, mech) in enumerate(steps):
        x = 60 + i * (W + G)
        top = tops[i]
        dash = None if today else "7 5"
        f.rect("_", x, top, W, 860 - top, C["white"], C["dark"] if today else C["purple"], 2, 10, dash=dash)
        f.rect("_", x, top, W, 50, C["dark"] if today else C["purplep"], C["dark"] if today else C["purplep"], 0, 10)
        f.badge(x + 26, top + 25, i + 1)
        f.text("_", x + 52, top + 32, name, 17, C["white"] if today else PT, 700)
        y = top + 76
        label(f, x + 16, y, "BRUKEREN SER", C["grey"], size=12, weight=700)
        f.lines("_", x + 16, y + 22, sees, 14.5, PT, 600, lh=19)
        y += 22 + len(sees) * 19 + 16
        label(f, x + 16, y, "MÅ FINNES BAK", C["grey"], size=12, weight=700)
        y += 10
        for t, k in behind:
            if k == "flate":
                w = len(t) * 7.2 + 22
                f.rect("_", x + 16, y, w, 24, C["tealp"], C["dark"], 1.3, 5)
                f.text("_", x + 16 + w / 2, y + 17, t, 12.5, C["dark"], 700, "middle")
            else:
                chip(f, x + 16, y, t, "data" if k == "data" else "uavklart")
            y += 30
        if today:
            f.rect("_", x + W - 84, top + 60, 70, 22, C["white"], C["dark"], 1.3, 11)
            f.text("_", x + W - 49, top + 75, "i dag", 12, C["dark"], 700, "middle")
        # skala maskinelt–redaksjonelt
        sy = 830
        f.add(f'<line x1="{x+16}" y1="{sy}" x2="{x+W-16}" y2="{sy}" stroke="{C["line"]}" stroke-width="4" stroke-linecap="round"/>')
        f.add(f'<circle cx="{x+16+(W-32)*mech}" cy="{sy}" r="9" fill="{C["purple"]}"/>')
    # akse-forklaring under
    f.rect("_", 60, 878, 1340, 104, "#f8fbfb", C["line"], 1.2, 10)
    f.text("_", 80, 910, "Maskinelt eller redaksjonelt?", 17, C["ink"], 700)
    f.text("_", 80, 936, "Punktet på linjen i hvert trinn: venstre = kan gjøres maskinelt, høyre = krever faglig og redaksjonelt skjønn.", 15, C["dark"])
    f.text("_", 80, 962, "Plasseringen er et forslag. Hvem som vedlikeholder ordlister, relasjoner og forklaringer, er uavklart.", 15, C["grey"], 600)
    # pil opp trappa
    f.arrow("_", [(80, 470), (1120, 250)], C["purple"], 2.5, dash="8 6", hs=12)
    f.rect("_", 420, 318, 240, 28, C["white"], C["purple"], 1.3, 14)
    f.text("_", 540, 337, "fra treff til veivisning", 14, PT, 700, "middle")
    save(f, "ff-F4-sok.svg")


# ---------- F6 Fleksibilitet innenfor faglige rammer ----------
def f6():
    f = Fig(None)
    frame(f, "Fleksibilitet innenfor faglige rammer", "Forskjellen på det som teknisk kan krysses, og det SSB kan stå inne for", "Oversikt",
          "Slik leses figuren",
          [("Mulig er ikke forsvarlig", ["At data kan krysses, betyr ikke", "at resultatet er statistikk SSB", "kan stå inne for."]),
           ("Seks faglige filtre", ["Hver kombinasjon må gjennom", "metode, populasjon, enhet,", "konfidensialitet, kvalitet og", "publiseringsansvar."]),
           ("Det som faller ut, har et sted", ["Noe må avvises, noe hører", "hjemme i mikrodatatilgang, noe", "kan kanskje publiseres med", "forbehold."]),
           ("Skjønn eller maskin?", ["Hvilke filtre som kan", "automatiseres, er uavklart."])],
          [("data", "Statistikk"), ("rolle", "Faglig filter"), ("flate", "Tilgang via flate"), ("utenfor", "Avvises"), ("uavklart", "Uavklart")])

    x0, x1 = 330, 1170
    t0, b0, t1, b1 = 250, 750, 440, 560
    f.add(f'<polygon points="{x0},{t0} {x1},{t1} {x1},{b1} {x0},{b0}" fill="{C["greenp"]}" stroke="{C["green"]}" stroke-width="2"/>')
    def top(x): return t0 + (t1 - t0) * (x - x0) / (x1 - x0)
    def bot(x): return b0 - (b0 - b1) * (x - x0) / (x1 - x0)
    gates = [("Metode", ["Er det beregnet", "slik?"]), ("Populasjon", ["Samme", "populasjon?"]), ("Enhet", ["Person, husholdning", "eller foretak?"]),
             ("Konfidensialitet", ["Kan noen", "identifiseres?"]), ("Kvalitet", ["Er usikkerheten", "akseptabel?"]), ("Ansvar", ["Kan SSB stå", "inne for det?"])]
    gx = [400 + k * 140 for k in range(6)]
    for (name, q), x in zip(gates, gx):
        f.add(f'<line x1="{x}" y1="{top(x)}" x2="{x}" y2="{bot(x)}" stroke="{C["purple"]}" stroke-width="5"/>')
        f.text("_", x, 190, name, 15.5, PT, 700, "middle")
        f.lines("_", x, 210, q, 12.5, C["dark"], 400, "middle", 16)
        f.add(f'<line x1="{x}" y1="236" x2="{x}" y2="{top(x)-4}" stroke="{C["purplel"]}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    # venstre: teknisk mulig
    f.rect("_", 60, 250, 250, 500, C["white"], C["grey"], 1.8, 12)
    f.text("_", 80, 286, "Teknisk mulig", 20, C["ink"], 700)
    f.lines("_", 80, 316, ["Alle variabler kan", "krysses med alle"], 15, C["dark"], lh=21)
    for i, t in enumerate(["arbeidsledighet", "× kommune", "× alder", "× måned"]):
        chip(f, 80, 390 + i * 34, t)
    f.lines("_", 80, 560, ["Datamengden og", "verktøyene setter", "ingen grense"], 14, C["grey"], 600, lh=19)
    f.arrow("_", [(310, 500), (328, 500)], C["green"], 3, hs=10)
    # innholdspiler i trakten
    f.text("_", 470, 505, "kombinasjoner", 14, C["green"], 700, "middle")
    # høyre: kan stå inne for
    f.arrow("_", [(1170, 500), (1188, 500)], C["green"], 3.5, hs=11)
    f.rect("_", 1190, 400, 210, 200, C["green"], C["green"], 0, 12)
    f.lines("_", 1208, 436, ["Det SSB kan", "stå inne for"], 19, C["white"], 700, lh=24)
    f.lines("_", 1208, 500, ["statistikk med", "definisjon, metode", "og forbehold"], 14, C["white"], 400, lh=19)
    # utganger
    exits = [(gx[1], 360, 620, "Avvises eller", "omformuleres", "utenfor"), (gx[3], 690, 940, "Krever mikro-", "datatilgang", "flate"),
             (gx[4], 960, 1200, "Publiseres med", "forbehold?", "uavklart")]
    for gxx, ex0, ex1, l1, l2, k in exits:
        fill, st, da = {"utenfor": (GREYF, GREYS, None), "flate": (C["tealp"], C["dark"], None), "uavklart": (C["white"], C["grey"], U)}[k]
        f.arrow("_", [(gxx, bot(gxx)), (gxx, 818)], C["purple"] if k != "uavklart" else C["grey"], 2.5, dash=None if k != "uavklart" else U, hs=10)
        f.rect("_", ex0, 820, ex1 - ex0, 112, fill, st, 1.8, 10, dash=da)
        f.lines("_", ex0 + 18, 856, [l1, l2], 17, C["ink"] if k != "uavklart" else C["grey"], 700, lh=22)
        if k == "flate":
            f.text("_", ex0 + 18, 912, "microdata.no eller forskertilgang", 13, C["dark"])
        if k == "utenfor":
            f.text("_", ex0 + 18, 912, "feil metode, populasjon eller enhet", 13, C["dark"])
        if k == "uavklart":
            f.text("_", ex0 + 18, 912, "finnes kategorien?", 13, C["grey"], 600)
    label(f, 60, 972, "Filtrene og utgangene er et forslag til struktur. Terskler og ansvar for kombinasjoner brukeren lager selv, er uavklart.", size=14)
    save(f, "ff-F6-fleksibilitet.svg")


# ---------- F7 Dataportalen: sandkasse eller autoritativ tjeneste ----------
def f7():
    f = Fig(None)
    frame(f, "Dataportalen: sandkasse eller autoritativ tjeneste?", "Hva som må være avklart før Dataportalen kan framstå som autoritativ for brukere utenfor SSB", "Diskusjon",
          "Slik leses figuren",
          [("Fire trinn", ["Fra utforsking til en flate SSB", "står inne for. Hvert trinn gir", "et større løfte til brukeren."]),
           ("Portene er avklaringer", ["Mellom trinnene ligger spørsmål", "om ansvar og rolle, ikke om", "mer innhold eller teknologi."]),
           ("Alle porter er åpne", ["Ingen av avklaringene er tatt.", "Figuren sier hva som må", "avgjøres, ikke hva svaret er."]),
           ("Dagens plassering", ["Hvor Dataportalen står i dag,", "må bekreftes av dem som", "forvalter den."])],
          [("flate", "Trinn"), ("rolle", "Port: avklaring"), ("uavklart", "Ikke avklart"), ("forslag", "Modellen er et forslag")])

    SW, GW = 220, 153
    names = [("Utforsking", ["Samle og prøve ut", "metadata"], "Interne", "Ingen garanti"),
             ("Intern samling", ["Felles oversikt", "for SSB"], "Interne", "Oppdatert etter", "beste evne"),
             ("Kvalitetssikret katalog", ["Innholdet oppfyller", "avtalte krav"], "Interne og utvalgte", "Innholdet er", "kontrollert"),
             ("Autoritativ brukerflate", ["SSB står inne for", "innholdet"], "Alle", "Offisiell kilde med", "ansvar og støtte")]
    tops = [560, 470, 380, 290]
    for i, n in enumerate(names):
        x = 60 + i * (SW + GW)
        top = tops[i]
        title, what, who = n[0], n[1], n[2]
        promise = list(n[3:])
        shade = [C["tealp"], C["tealp"], C["teal"], C["teal"]][i]
        f.rect("_", x, top, SW, 800 - top, shade, C["dark"], 1.8, 10)
        f.badge(x + 24, top + 28, i + 1)
        tl = title.split(" ") if len(title) > 16 else [title]
        if len(tl) > 1:
            tl = [tl[0], " ".join(tl[1:])]
        f.lines("_", x + 48, top + 34, tl, 17, C["ink"], 700, lh=21)
        y = top + 34 + len(tl) * 21 + 14
        f.lines("_", x + 16, y, what, 14.5, C["dark"], lh=19)
        y += len(what) * 19 + 14
        label(f, x + 16, y, "BRUKERE", C["grey"], size=11.5, weight=700)
        f.text("_", x + 16, y + 20, who, 14.5, PT, 700)
        y += 44
        label(f, x + 16, y, "LØFTE", C["grey"], size=11.5, weight=700)
        f.lines("_", x + 16, y + 20, promise, 14.5, C["green"], 700, lh=19)
    ports = [["Eierskap og|forvaltnings-|ansvar"], ["Krav til innhold|og kvalitet", "Ansvar for|oppdatering"],
             ["Juridiske|rammer for hva|som vises", "Forholdet til|ssb.no og|eksterne|kataloger", "Brukerstøtte"]]
    for k, items in enumerate(ports):
        x = 60 + SW + k * (SW + GW) + 10
        w = GW - 20
        f.rect("_", x, 196, w, 604, "#faf9ff", C["purple"], 2, 10, dash="7 5")
        f.text("_", x + w / 2, 226, f"Port {k+1}", 16, PT, 700, "middle")
        y = 246
        for it in items:
            ln = it.split("|")
            h = 18 * len(ln) + 42
            f.rect("_", x + 8, y, w - 16, h, C["white"], C["grey"], 1.3, 8, dash=U)
            f.lines("_", x + 18, y + 22, ln, 13, C["ink"], 700, lh=18)
            f.add(f'<circle cx="{x+w-26}" cy="{y+h-16}" r="8" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="1.4" stroke-dasharray="3 2"/>')
            f.text("_", x + w - 26, y + h - 12, "?", 11, C["grey"], 700, "middle")
            y += h + 10
        f.arrow("_", [(x - 10, 740), (x + w + 8, 740)], C["purple"], 2.5, hs=10)
    # dagens plassering
    f.rect("_", 60, 300, SW, 110, C["white"], C["grey"], 1.8, 10, dash=U)
    f.lines("_", 76, 332, ["Hvor står", "Dataportalen i dag?"], 16, C["ink"], 700, lh=21)
    f.text("_", 76, 388, "må bekreftes", 14, C["grey"], 600)
    # diskusjonsbånd
    f.rect("_", 60, 828, 1340, 156, C["white"], C["dark"], 1.5, 12)
    f.text("_", 84, 864, "Spørsmål før noen port åpnes", 18, C["ink"], 700)
    qs = ["Ønsker vi at Dataportalen blir autoritativ, og i så fall for hvem?",
          "Hva skjer med innhold som er synlig for andre før portene er passert?",
          "Hvem har mandat til å si at en port er passert?"]
    for i, q in enumerate(qs):
        f.text("_", 84, 898 + i * 28, "·  " + q, 16, C["dark"])
    save(f, "ff-F7-dataportalen.svg")


# ---------- F5 KI-assistent som veiviser ----------
def f5():
    f = Fig(None)
    frame(f, "KI-assistent som veiviser, ikke fri svarmaskin", "Hva en SSB-assistent bør kunne, hva den ikke skal gjøre, og hva den forutsetter", "Diskusjon",
          "Slik leses figuren",
          [("Veiviser, ikke orakel", ["Assistenten peker på autoritative", "kilder. Den lager ikke egne", "sannheter."]),
           ("«Jeg vet ikke» er en funksjon", ["Å avstå eller henvise videre er", "riktig oppførsel når kilden", "ikke holder."]),
           ("Forutsetningene er metadata", ["Uten maskinlesbare begreper,", "metode og forbehold (F3) blir", "assistenten en gjetter."]),
           ("Alt her er forslag", ["Ingen assistent er besluttet.", "Ansvar og regelverk er uavklart."])],
          [("flate", "Skal kunne"), ("utenfor", "Skal ikke"), ("data", "Forutsetter"), ("uavklart", "Uavklart"), ("forslag", "Forslag")])
    cols = [("Skal kunne", "flate", ["Finne riktig statistikk", "Forklare begreper", "Vise kilde og tabell", "Peke på metode", "Advare mot feil sammenligning", "Si fra når den ikke kan svare trygt"]),
            ("Skal ikke", "utenfor", ["Lage egne beregninger uten kilde", "Krysse data SSB ikke har publisert", "Gi politiske tolkninger", "Svare om enkeltpersoner eller foretak"]),
            ("Forutsetter", "data", ["Maskinlesbare begreper og metode (F3)", "Relasjoner mellom statistikker (F4)", "Kvalitet og usikkerhet som data", "Logging og evaluering av svar"]),
            ("Uavklart", "uavklart", ["Hvem har ansvaret for feil svar?", "Hvilken modell og plattform?", "Hvilke krav i KI-forordningen gjelder?", "Intern først, eller rett ut?"])]
    W, G = 325, 13
    for i, (h, k, items) in enumerate(cols):
        x = 60 + i * (W + G)
        fill, st, tc, da = {"flate": (C["tealp"], C["dark"], C["ink"], None), "utenfor": (GREYF, GREYS, C["ink"], None),
                            "data": (C["greenp"], C["green"], C["ink"], None), "uavklart": (C["white"], C["grey"], C["grey"], U)}[k]
        f.rect("_", x, 186, W, 500, fill, st, 1.8, 12, dash=da)
        f.text("_", x + 20, 222, h, 21, tc, 700)
        for j, it in enumerate(items):
            y = 246 + j * 72
            f.rect("_", x + 16, y, W - 32, 60, C["white"], st, 1.3, 8, dash=da)
            words = it.split(" ")
            ln, cur = [], ""
            for wd in words:
                if len(cur + " " + wd) > 30:
                    ln.append(cur); cur = wd
                else:
                    cur = (cur + " " + wd).strip()
            ln.append(cur)
            f.lines("_", x + 30, y + (36 if len(ln) == 1 else 26), ln, 15, tc, 600, lh=19)
    # svaroppførsel
    f.text("_", 60, 728, "Når assistenten er usikker: fire mulige svar", 19, C["ink"], 700)
    outs = [("Trygt svar", ["kilden finnes og", "begrepet er entydig"], C["green"], C["green"], C["white"]),
            ("Svar med forbehold", ["kilden finnes, men med", "usikkerhet eller brudd"], C["greenp"], C["green"], C["ink"]),
            ("Henvis videre", ["en annen kilde eller", "flate er riktig"], C["tealp"], C["dark"], C["ink"]),
            ("Avstå", ["ingen autoritativ kilde,", "eller det krever tolkning"], GREYF, GREYS, C["ink"])]
    W2 = 318
    for i, (t, d, fi, st, tc) in enumerate(outs):
        x = 60 + i * (W2 + 22)
        f.rect("_", x, 748, W2, 130, fi, st, 1.8, 10)
        f.text("_", x + 18, 786, t, 19, tc, 700)
        f.lines("_", x + 18, 814, d, 15, tc, lh=20)
        if i < 3:
            f.arrow("_", [(x + W2 + 2, 813), (x + W2 + 20, 813)], C["dark"], 2, hs=8)
    f.add(f'<line x1="60" y1="906" x2="1400" y2="906" stroke="{C["line"]}" stroke-width="4" stroke-linecap="round"/>')
    f.arrow("_", [(1300, 906), (1400, 906)], C["grey"], 4, hs=12)
    label(f, 60, 934, "økende usikkerhet i kilden eller spørsmålet →", size=14)
    label(f, 60, 962, "Alle fire er riktig oppførsel. Feil oppførsel er å gi et trygt svar når kilden ikke holder.", C["dark"], size=14)
    save(f, "ff-F5-ki-assistent.svg")


# ---------- F8 Brukerreise i dag, nær framtid og målbilde ----------
def f8():
    f = Fig(None)
    frame(f, "Brukerreisen i dag og framover", "En journalist med tidsfrist: fra spørsmål til sitert tall, i tre tidsbilder", "Oversikt",
          "Slik leses figuren",
          [("Samme reise, tre tidsbilder", ["Stegene er de samme. Det som", "endres, er hvor brukeren må", "lete og hva som følger med."]),
           ("I dag: hopp mellom flater", ["Friksjonspunktene er antatt og", "må bekreftes med brukerunder-", "søkelser."]),
           ("Sammenheng, ikke sømløshet", ["Målet er gode overganger, ikke", "å skjule at reglene endrer seg."]),
           ("Andre personas", ["Analytiker via API og forsker", "med mikrodata er fokusvarianter."])],
          [("flate", "Flate"), ("data", "Det som følger med"), ("rolle", "Markert overgang"), ("uavklart", "Antatt friksjon"), ("forslag", "Forslag")],
          status="Utkast til diskusjon · friksjon er antatt, ikke målt")
    steps = ["Finne", "Forstå", "Hente", "Bruke", "Sitere"]
    X0, CW = 250, 230
    for j, s in enumerate(steps):
        x = X0 + j * CW
        f.rect("_", x + 4, 186, CW - 8, 44, C["dark"], C["dark"], 0, 8)
        f.text("_", x + CW / 2, 215, f"{j+1}  {s}", 17, C["white"], 700, "middle")
        if j < 4:
            f.add(f'<polygon points="{x+CW-6},{200} {x+CW+4},{208} {x+CW-6},{216}" fill="{C["dark"]}"/>')
    rows = [("I dag", "finnes", 246),
            ("Nær framtid", "forslag", 486),
            ("Målbilde", "forslag", 726)]
    cells = {
        0: [[("søk på ssb.no", "flate"), ("eller søkemotor", "flate")], [("Om statistikken", "flate"), ("egen side", "note")],
            [("Statistikkbanken", "flate"), ("API", "flate")], [("egen tolkning", "note")], [("manuell kilde-", "note"), ("henvisning", "note")]],
        1: [[("søk med begreps-", "data"), ("veiviser (F4)", "data")], [("definisjon og", "data"), ("forbehold ved tallet", "data")],
            [("tabell med metadata", "data")], [("advarsel mot feil", "data"), ("sammenligning", "data")], [("siteringsforslag", "data")]],
        2: [[("veiviser eller", "data"), ("assistent (F5)", "data")], [("autoritetskjeden", "data"), ("synlig (F3)", "data")],
            [("samme tall i alle", "data"), ("flater og API", "data")], [("markert overgang", "rolle"), ("til mikrodata", "rolle")], [("stabil lenke og", "data"), ("sitering", "data")]],
    }
    frictions = {0: [(1, "hopper mellom flater"), (2, "hvilket begrep?"), (4, "hvilken versjon?")]}
    for r, (name, st, y) in enumerate(rows):
        dash = None if st == "finnes" else "7 5"
        f.rect("_", 60, y, 180, 224, C["white"] if st == "finnes" else "#faf9ff", C["dark"] if st == "finnes" else C["purple"], 1.8, 10, dash=dash)
        f.text("_", 76, y + 34, name, 19, C["ink"] if st == "finnes" else PT, 700)
        f.text("_", 76, y + 58, "finnes i dag" if st == "finnes" else "forslag", 14, C["grey"], 600)
        for j in range(5):
            x = X0 + j * CW
            f.rect("_", x + 4, y, CW - 8, 224, C["white"], C["line"], 1.2, 8)
            cy = y + 22
            items = cells[r][j]
            kind = items[0][1]
            if kind == "note":
                f.lines("_", x + 20, cy + 18, [t for t, _ in items], 15, C["dark"], lh=20)
            else:
                fill, stc, tc = {"flate": (C["tealp"], C["dark"], C["dark"]), "data": (C["greenp"], C["green"], C["green"]),
                                 "rolle": (C["purplep"], C["purple"], PT)}[kind]
                if kind == "flate":
                    for k, (t, _) in enumerate(items):
                        w = len(t) * 7.4 + 24
                        f.rect("_", x + 18, cy + k * 36, w, 28, fill, stc, 1.4, 6)
                        f.text("_", x + 18 + w / 2, cy + k * 36 + 19, t, 13.5, tc, 700, "middle")
                else:
                    f.rect("_", x + 18, cy, CW - 44, 20 * len(items) + 22, fill, stc, 1.4, 8, dash=None if kind != "rolle" else "6 4")
                    f.lines("_", x + 30, cy + 24, [t for t, _ in items], 14, tc, 700, lh=20)
        for j, t in frictions.get(r, []):
            x = X0 + j * CW
            f.rect("_", x + 18, y + 160, CW - 44, 44, C["white"], C["grey"], 1.4, 8, dash=U)
            f.text("_", x + 34, y + 187, "! " + t, 14, C["grey"], 700)
    save(f, "ff-F8-brukerreise.svg")


# ---------- F10 To scenarioer for 2050 ----------
def f10():
    f = Fig(None)
    frame(f, "To scenarioer for 2050", "SSB som dataplattform eller som autoritativ statistikkfaglig institusjon", "Scenario",
          "Slik leses figuren",
          [("To ytterpunkter", ["Ikke to planer. Scenarioene", "gjør forskjellen synlig, slik at", "valgene kan diskuteres."]),
           ("Begge gir data", ["Forskjellen er hva som gjør SSB", "uerstattelig når andre også har", "data og KI."]),
           ("Begge har risiko", ["Plattformen kan bli én kilde blant", "mange. Institusjonen kan bli", "for treg og lukket."]),
           ("Hvor er vi i dag?", ["Plasseringen på skalaen nederst", "er bevisst tom. Den er", "diskusjonens startpunkt."])],
          [("flate", "Dataplattform"), ("data", "Statistikkfaglig institusjon"), ("uavklart", "Ikke plassert")],
          status="Scenario til diskusjon, ikke vedtatt retning")
    dims = [("Verdiløfte", "Mest mulig data, raskest mulig", "Tall man kan stå inne for, med begreper og forbehold"),
            ("Hva brukeren får", "Datasett og API-er", "Svar med definisjon, metode og usikkerhet"),
            ("Kompetansesatsing", "Dataingeniører og plattform", "Fagkunnskap gjort maskinlesbar"),
            ("KIs rolle", "Konsumerer SSB-data", "Bruker SSBs begreper og forbehold"),
            ("Styrke", "Skala, fart, lav terskel", "Tillit, sporbarhet, faglig særpreg"),
            ("Risiko", "Blir én datakilde blant mange", "Kan oppleves som tregt og lukket")]
    LX, LW, CW = 60, 250, 535
    xA, xB = LX + LW + 10, LX + LW + 10 + CW + 10
    f.rect("_", xA, 186, CW, 66, C["dark"], C["dark"], 0, 10)
    f.text("_", xA + 22, 228, "SSB som dataplattform", 21, C["white"], 700)
    f.rect("_", xB, 186, CW, 66, C["green"], C["green"], 0, 10)
    f.text("_", xB + 22, 228, "SSB som autoritativ institusjon", 21, C["white"], 700)
    y = 266
    for d, a, b in dims:
        f.rect("_", LX, y, LW, 82, C["white"], C["line"], 1.2, 8)
        f.text("_", LX + 16, y + 48, d, 17, C["ink"], 700)
        for x, t, fill, st in [(xA, a, C["tealp"], C["dark"]), (xB, b, C["greenp"], C["green"])]:
            f.rect("_", x, y, CW, 82, fill, st, 1.3, 8)
            ln = [t] if len(t) < 44 else [t[:t.rfind(" ", 0, 44)], t[t.rfind(" ", 0, 44) + 1:]]
            f.lines("_", x + 20, y + (48 if len(ln) == 1 else 36), ln, 17, C["ink"], 400, lh=22)
        y += 92
    # skala
    sy = 890
    f.text("_", LX, 846, "Hvor ligger SSB i dag, og hvor peker valgene de neste tre årene?", 18, C["ink"], 700)
    f.add(f'<line x1="{xA}" y1="{sy}" x2="{xB+CW}" y2="{sy}" stroke="{C["line"]}" stroke-width="8" stroke-linecap="round"/>')
    f.text("_", xA, sy + 36, "dataplattform", 15, C["dark"], 700)
    f.text("_", xB + CW, sy + 36, "autoritativ institusjon", 15, C["green"], 700, "end")
    mx = (xA + xB + CW) / 2
    f.add(f'<circle cx="{mx}" cy="{sy}" r="18" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="2" stroke-dasharray="4 3"/>')
    f.text("_", mx, sy + 6, "?", 16, C["grey"], 700, "middle")
    f.text("_", mx, sy + 42, "ikke plassert", 14, C["grey"], 600, "middle")
    save(f, "ff-F10-scenarioer.svg")


# ---------- F12 Startpunkter og piloter ----------
def f12():
    f = Fig(None)
    frame(f, "Startpunkter og piloter", "Hva prosjektet kan begynne med, uten å låse valg som ikke er tatt", "Diskusjon",
          "Slik brukes figuren",
          [("En arbeidsflate", ["Kandidatene til venstre plasseres", "i rutenettet sammen, i et møte.", "Figuren plasserer dem ikke."]),
           ("To spørsmål per kandidat", ["Hvor mye verdi gir den brukerne?", "Hvor uavhengig er den av de", "store avklaringene i F9?"]),
           ("Start øverst til høyre", ["Høy verdi og lite avhengighet", "gir læring uten å låse valg."]),
           ("Alle kandidater er forslag", ["Listen kan utvides. Hver", "kandidat peker på figuren", "den bygger på."])],
          [("data", "Kandidat"), ("forslag", "Forslag"), ("rolle", "Avhenger av avklaring"), ("uavklart", "Ikke plassert")])
    cands = [("Brukerord til begrep", "ett tema, f.eks. arbeidsmarked", "F4", "ingen store"),
             ("Autoritetskjede", "for én statistikk", "F3", "metadataforvaltning"),
             ("Maskinlesbar «Om statistikken»", "for noen få statistikker", "F3", "metadataforvaltning"),
             ("Intern assistentprototype", "på ett tema", "F5", "KI-assistentens ansvar"),
             ("Avklare Dataportalens rolle", "port 1 i F7", "F7", "Hva er Dataportalen?")]
    f.text("_", 60, 206, "Kandidater, ikke plassert", 18, C["ink"], 700)
    y = 222
    for t, s, fig, dep in cands:
        f.rect("_", 60, y, 340, 138, C["white"], C["purple"], 1.8, 10, dash="7 5")
        f.rect("_", 72, y + 14, 44, 24, C["greenp"], C["green"], 1.3, 12)
        f.text("_", 94, y + 31, fig, 13, C["green"], 700, "middle")
        tl = [t] if len(t) <= 26 else [t[:t.rfind(" ", 0, 26)], t[t.rfind(" ", 0, 26) + 1:]]
        f.lines("_", 128, y + 32, tl, 16, C["ink"], 700, lh=20)
        yy = y + 32 + len(tl) * 20 + 4
        f.text("_", 128, yy, s, 14, C["dark"])
        f.text("_", 72, y + 122, "avhenger av: " + dep, 13, PT if dep != "ingen store" else C["green"], 700)
        y += 150
    # 2x2
    gx, gy, gw, gh = 500, 206, 880, 690
    f.rect("_", gx, gy, gw, gh, C["white"], C["dark"], 2, 8)
    f.add(f'<line x1="{gx+gw/2}" y1="{gy}" x2="{gx+gw/2}" y2="{gy+gh}" stroke="{C["line"]}" stroke-width="2"/>')
    f.add(f'<line x1="{gx}" y1="{gy+gh/2}" x2="{gx+gw}" y2="{gy+gh/2}" stroke="{C["line"]}" stroke-width="2"/>')
    f.rect("_", gx + gw / 2 + 2, gy + 2, gw / 2 - 4, gh / 2 - 4, C["greenp"], C["greenp"], 0, 6)
    quads = [(gx + gw * 0.75, gy + 60, "Start her", "høy verdi, lite avhengig", C["green"]),
             (gx + gw * 0.25, gy + 60, "Forbered", "høy verdi, venter på avklaring", C["dark"]),
             (gx + gw * 0.75, gy + gh / 2 + 60, "Lær billig", "lav verdi, lite avhengig", C["dark"]),
             (gx + gw * 0.25, gy + gh / 2 + 60, "Vent", "lav verdi, venter på avklaring", C["grey"])]
    for x, y, t, s, c in quads:
        f.text("_", x, y, t, 22, c, 700, "middle")
        f.text("_", x, y + 26, s, 14, C["grey"], 600, "middle")
    f.arrow("_", [(gx, gy + gh + 30), (gx + gw, gy + gh + 30)], C["dark"], 2.5, hs=11)
    f.text("_", gx + gw / 2, gy + gh + 60, "uavhengighet av uavklarte spørsmål (F9) →", 15, C["dark"], 700, "middle")
    f.arrow("_", [(gx - 30, gy + gh), (gx - 30, gy)], C["dark"], 2.5, hs=11)
    f.text("_", gx - 44, gy + gh / 2, "", 1)
    f.add(f'<text x="{gx-42}" y="{gy+gh/2}" font-family="{FONT}" font-size="15" font-weight="700" fill="{C["dark"]}" text-anchor="middle" transform="rotate(-90 {gx-42} {gy+gh/2})">brukerverdi →</text>')
    save(f, "ff-F12-piloter.svg")


F2C = dict(
    file="ff-F2c-tilgangsregimer.svg", hi={"ssb", "pub", "skille", "restricted"},
    title="Tilgangsregimer: hvem får se hva",
    sub="Fokus på F2: det juridiske skillet mellom publisert statistikk og mikrodata", tag="Fokus F2c",
    panel="For personvern og juridisk",
    items=[("Åpent publisert", ["Statistikk som er vurdert for", "konfidensialitet før publisering.", "Alle kan bruke den."]),
           ("Skillet er juridisk", ["Over linjen gjelder publiserings-", "regler, under gjelder tilgangs-", "regler. Grensen må synes."]),
           ("microdata.no", ["Tilgang for godkjente brukere via", "institusjonen. Vilkår og kontroll", "må beskrives for brukeren."]),
           ("Forskertilgang", ["Søknad og avtale per prosjekt.", "Hvem som vurderer, og etter", "hvilket regelverk, må framgå."]),
           ("Uavklart", ["Hvordan søknad og avtaler henger", "sammen, og hvordan regelverket", "forklares for brukerne."])],
    legend=[("flate", "Flate i fokus"), ("data", "Hva den bærer"), ("rolle", "Tilgangsstyrt sone"), ("uavklart", "Uavklart")],
    badges=[(552, 296), (560, 741), (552, 800), (812, 800), (1072, 800)])


# ---------- F4a Søk med KI-støtte: forutsetninger og tidshorisont ----------
def f4a():
    f = Fig(None)
    frame(f, "Søk med KI-støtte: hva endres, og når?", "Fokus på F4: hvordan KI flytter arbeid fra redaksjonelt til maskinelt, trinn for trinn", "Fokus F4a",
          "Slik leses figuren",
          [("Forutsetning først, tid etterpå", ["Hver horisont starter når", "forutsetningen er på plass.", "Årstallene er antatt."]),
           ("KI flytter arbeid, ikke ansvar", ["Punktet i hver celle glir mot", "maskinelt. I trinn 4 og 5 stopper", "det ved grensen for faglig ansvar."]),
           ("Størst gevinst i trinn 2 og 3", ["Fra brukerord til begrep og", "nærliggende statistikk kan KI", "gjøre mye, og tidlig."]),
           ("Her møtes søk og assistent", ["På lang sikt glir søk over i", "dialog. Da gjelder rammene i F5."]),
           ("Alt er forslag", ["Horisontene er et diskusjons-", "grunnlag, ikke en plan."])],
          [("forslag", "Horisont, forslag"), ("uavklart", "Tidshorisont antatt")],
          status="Forslag til diskusjon, ikke kvalitetssikret")
    X0, CW = 300, 220
    steps = ["Treffliste", "Ord til begrep", "Nærliggende statistikk", "Forklare forskjeller", "Anbefalt inngang"]
    for j, s_ in enumerate(steps):
        x = X0 + j * CW
        f.rect("_", x + 4, 184, CW - 8, 52, C["purplep"], C["purplep"], 0, 8)
        f.badge(x + 26, 210, j + 1)
        ln = [s_] if len(s_) <= 16 else s_.split(" ", 1)
        f.lines("_", x + 50, 206 if len(ln) == 2 else 216, ln, 15, PT, 700, lh=18)
    # rader
    rows = [("I dag", None, None, 250, 58),
            ("Kort sikt", ["Krever: dagens innhold,", "godt indeksert"], "typisk 0–1 år · antatt", 318, 170),
            ("Mellomlang sikt", ["Krever: maskinlesbare", "begreper og relasjoner (F3)"], "typisk 1–3 år · antatt", 498, 170),
            ("Lang sikt", ["Krever: hele autoritets-", "kjeden maskinlesbar"], "typisk 3+ år · antatt", 678, 170)]
    pos = {0: [0.10, 0.45, 0.30, 0.80, 0.90], 1: [0.08, 0.28, 0.25, 0.80, 0.90],
           2: [0.08, 0.14, 0.12, 0.62, 0.72], 3: [0.06, 0.08, 0.08, 0.50, 0.50]}
    txt = {1: [["Bedre rangering", "av treff"], ["Semantisk søk foreslår", "begrep for brukerens ord"], ["Enkle forslag fra", "eksisterende lenker"], ["Ingen endring"], ["Ingen endring"]],
           2: [["Som før"], ["Forslag kontrolleres", "mot begrepsregisteret"], ["Nærliggende statistikk", "fra maskinlesbare", "relasjoner"], ["KI skriver utkast til", "forklaringer, fag", "godkjenner"], ["Forslag til inngang,", "fag godkjenner"]],
           3: [["Glir inn i dialog"], ["Løses i dialog med", "oppfølgingsspørsmål"], ["Assistenten viser", "sammenhenger"], ["Forklaringer i dialog,", "bygget på godkjent", "innhold"], ["Anbefaling i dialog,", "innenfor faglig ansvar"]]}
    for r, (name, req, tid, y, h) in enumerate(rows):
        today = r == 0
        f.rect("_", 60, y, 232, h, C["white"] if today else "#faf9ff", C["dark"] if today else C["purple"], 1.8, 10, dash=None if today else "7 5")
        f.text("_", 76, y + (36 if today else 32), name, 18, C["ink"] if today else PT, 700)
        if req:
            f.lines("_", 76, y + 58, req, 13.5, C["dark"], 600, lh=18)
            w = len(tid) * 6.9 + 22
            f.rect("_", 76, y + h - 42, w, 26, C["white"], C["grey"], 1.3, 13, dash=U)
            f.text("_", 76 + w / 2, y + h - 24, tid, 12.5, C["grey"], 700, "middle")
        for j in range(5):
            x = X0 + j * CW
            f.rect("_", x + 4, y, CW - 8, h, C["white"], C["line"] if today else "#e3dcfb", 1.2, 8)
            if not today:
                t = txt[r][j]
                muted = t[0] in ("Ingen endring", "Som før")
                f.lines("_", x + 18, y + 30, t, 13.5, C["grey"] if muted else C["ink"], 600 if not muted else 400, lh=18)
            # skala
            sy = y + h - 22 if not today else y + 30
            x1, x2 = x + 18, x + CW - 22
            f.add(f'<line x1="{x1}" y1="{sy}" x2="{x2}" y2="{sy}" stroke="{C["line"]}" stroke-width="4" stroke-linecap="round"/>')
            px = x1 + (x2 - x1) * pos[r][j]
            if today:
                f.add(f'<circle cx="{px}" cy="{sy}" r="8" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="2.5"/>')
            else:
                px0 = x1 + (x2 - x1) * pos[r - 1][j]
                if abs(px0 - px) > 12:
                    f.arrow("_", [(px0, sy), (px + 10, sy)], C["purplel"], 2.5, hs=8)
                f.add(f'<circle cx="{px}" cy="{sy}" r="8" fill="{C["purple"]}"/>')
    # grense for faglig ansvar i trinn 4 og 5
    for j in (3, 4):
        x = X0 + j * CW
        gx = x + 18 + (CW - 40) * 0.5
        for yy in (280, 466, 646, 826):
            f.add(f'<line x1="{gx}" y1="{yy-18}" x2="{gx}" y2="{yy+18}" stroke="{C["purple"]}" stroke-width="3"/>')
        f.add(f'<line x1="{gx}" y1="844" x2="{gx}" y2="858" stroke="{C["purple"]}" stroke-width="2" stroke-dasharray="3 3"/>')
    f.rect("_", X0 + 3 * CW + 40, 858, 2 * CW - 80, 28, C["white"], C["purple"], 1.4, 14)
    f.text("_", X0 + 4 * CW, 877, "grense for faglig ansvar", 14, PT, 700, "middle")
    # møtepunkt med F5
    f.rect("_", X0 + 4, 858, 3 * CW - 48, 28, C["white"], C["dark"], 1.3, 14)
    f.text("_", X0 + (3 * CW - 40) / 2, 877, "lang sikt: her møtes søk og assistent (se F5)", 14, C["dark"], 700, "middle")
    # forklaring skala
    f.rect("_", 60, 904, 1340, 80, "#f8fbfb", C["line"], 1.2, 10)
    f.add(f'<circle cx="{90}" cy="{944}" r="8" fill="{C["white"]}" stroke="{C["grey"]}" stroke-width="2.5"/>')
    f.text("_", 106, 950, "i dag (fra F4)", 15, C["dark"])
    f.add(f'<circle cx="{250}" cy="{944}" r="8" fill="{C["purple"]}"/>')
    f.text("_", 266, 950, "horisonten", 15, C["dark"])
    f.text("_", 380, 940, "Punktet på linjen: venstre = kan gjøres maskinelt, høyre = krever faglig og redaksjonelt skjønn.", 15, C["dark"])
    f.text("_", 380, 964, "Plasseringene er et forslag til diskusjon, ikke en vurdering av verktøy.", 15, C["grey"], 600)
    save(f, "ff-F4a-sok-med-ki.svg")


if __name__ == "__main__":
    for fn in (intro, f1, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12):
        fn()
    f2()
    f2(F2C)
    f4a()
    print("ok")
