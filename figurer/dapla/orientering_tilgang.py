"""Dapla · Orientering × Ansvar og tilgang (SCB-serien)."""
import os
from konseptfigurer.fig import Fig, C, W, H, FONT, PURPLE_TXT, DIM, esc
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

# ---------- grunnfigur ----------
def base(f: Fig):
    add = f.add
    add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["white"]}"/>')

    # --- Ansatte ---
    f.text("persons", 165, 212, "Ansatte i SSB", 24, C["dark"], 700, "middle")
    ppl = [(330, "Seksjonsleder"), (490, "Statistiker"), (628, "Statistiker"), (748, "Utvikler")]
    for cy, lab in ppl:
        f.person("persons", 165, cy - 14, 0.9)
        f.text("persons", 165, cy + 40, lab, 20, C["ink"], 400, "middle")

    # --- Team-ramme ---
    f.rect("team", 320, 180, 790, 700, C["purplep"], C["purple"], 3, 16)
    f.text("team", 346, 226, "Dapla-team «Skatt næring»", 28, PURPLE_TXT, 700)
    f.text("team", 346, 258, "Tilhører én seksjon · finnes i test og prod", 20, C["grey"], 400)

    # Roller
    f.rect("ta", 346, 292, 262, 84, C["white"], C["purple"], 2)
    f.text("ta", 364, 326, "Teamansvarlig", 23, PURPLE_TXT, 700)
    f.lines("ta", 364, 354, ["Styrer medlemskap"], 19, C["grey"])

    f.rect("da", 346, 440, 262, 104, C["purplel"], C["purple"], 2)
    f.text("da", 364, 474, "Data-admins", 23, PURPLE_TXT, 700)
    f.lines("da", 364, 502, ["2–3 personer", "Godkjenner og kan få JIT"], 19, C["ink"])

    f.rect("dev", 346, 590, 262, 190, C["purplel"], C["purple"], 2)
    f.text("dev", 364, 624, "Developers", 23, PURPLE_TXT, 700)
    f.lines("dev", 364, 652, ["Alle som jobber", "med data i teamet"], 19, C["ink"])

    # Medlemskap-piler
    for cy in (330, 490, 628, 748):
        f.arrow("member", [(210, cy - 10), (346, cy - 10)], C["dark"], 2, hs=10)

    # --- Kildeprosjekt ---
    f.rect("kilde", 680, 292, 400, 222, C["white"], C["green"], 2, 12)
    f.text("kilde", 1060, 326, "Kildeprosjekt", 23, C["green"], 700, "end")
    f.lock("kilde", 868, 300, C["green"])
    f.cyl("kilde", 730, 348, 180, 110, C["green"], C["green"])
    f.text("kilde", 820, 405, "Kildedata", 21, C["white"], 700, "middle")
    f.lines("kilde", 820, 430, ["i klartekst"], 17, C["white"], 400, "middle")
    f.lines("kilde", 1060, 496, ["Ingen fast tilgang"], 18, C["grey"], 400, "end")

    # --- Standardprosjekt ---
    f.rect("std", 680, 562, 400, 296, C["white"], C["green"], 2, 12)
    f.text("std", 1060, 596, "Standardprosjekt", 23, C["green"], 700, "end")
    f.cyl("prod", 700, 618, 210, 150, C["greenl"], C["green"])
    f.text("prod", 805, 668, "Produktbøtte", 21, C["ink"], 700, "middle")
    f.lines("prod", 805, 696, ["inndata", "klargjorte · statistikk", "utdata"], 16, C["ink"], 400, "middle", 20)
    f.cyl("delt", 940, 632, 120, 100, C["greenp"], C["green"], 2)
    f.text("delt", 1000, 690, "Delt-bøtte", 18, C["ink"], 700, "middle")
    f.lines("std", 700, 836, ["Teamets daglige arbeidsområde"], 18, C["grey"])

    # Kildomaten (kilde -> produkt)
    f.arrow("kildomaten", [(820, 472), (820, 616)], C["green"], 4, hs=14)
    f.rect("kildomaten", 745, 520, 150, 34, C["white"], C["green"], 2, 17)
    f.text("kildomaten", 820, 544, "Kildomaten", 18, C["green"], 700, "middle")

    # Tilgang
    f.arrow("acc_da", [(608, 492), (680, 440)], C["purple"], 3, dash="9 7", hs=12)
    f.text("acc_da", 640, 424, "JIT", 17, PURPLE_TXT, 700, "middle")
    f.arrow("acc_dev", [(608, 690), (700, 690)], C["purple"], 5, hs=14)

    # --- Andre team og Dataportal ---
    f.rect("dp", 1160, 292, 240, 126, C["tealp"], C["dark"], 2)
    f.text("dp", 1180, 328, "SSB Dataportal", 22, C["dark"], 700)
    f.lines("dp", 1180, 356, ["Datakatalog: finne", "data på tvers av team"], 18, C["ink"])

    f.text("others", 1280, 580, "Andre Dapla-team", 21, C["dark"], 700, "middle")
    f.rect("others", 1160, 600, 240, 70, C["purplep"], C["purple"], 2)
    f.text("others", 1280, 643, "«Arbeidsmarked»", 20, PURPLE_TXT, 600, "middle")
    f.rect("others", 1160, 690, 240, 70, C["purplep"], C["purple"], 2)
    f.text("others", 1280, 733, "«Nasjonalregnskap»", 20, PURPLE_TXT, 600, "middle")

    f.arrow("share", [(1060, 682), (1128, 682), (1128, 635), (1160, 635)], C["green"], 3, dash="10 6", hs=12)
    f.arrow("share", [(1128, 682), (1128, 725), (1160, 725)], C["green"], 3, dash="10 6", hs=12)
    f.text("share", 1280, 796, "Lesetilgang etter avtale", 18, C["green"], 700, "middle")

    f.arrow("dp_arr", [(1040, 562), (1040, 540), (1280, 540), (1280, 418)], C["dark"], 2, dash="3 6", hs=11)
    f.text("dp_arr", 1140, 530, "metadata", 17, C["dark"], 400, "middle", italic=True) if False else None
    f.text("dp_arr", 1160, 530, "metadata", 17, C["grey"], 600, "middle")

    # --- Plattformbånd (selvbetjening) ---
    f.rect("platform", 60, 906, 1340, 84, C["tealp"], C["teal"], 2, 12)
    f.lines("platform", 80, 940, ["Felles plattform", "på Google Cloud"], 19, C["dark"], 700)
    chips = [("lab", "Dapla Lab", "arbeidsflate"),
             ("ctrl", "Dapla Ctrl", "team og medlemmer"),
             ("iac", "Team-repo (IaC)", "bøtter og deling"),
             ("kchip", "Kildomaten", "automatisering"),
             ("dpchip", "Dataportal", "datakatalog")]
    x0, cw, gap = 260, 214, 13
    for i, (gid, a, b) in enumerate(chips):
        x = x0 + i * (cw + gap)
        f.rect(gid, x, 918, cw, 60, C["white"], C["dark"], 2, 8)
        f.text(gid, x + cw / 2, 944, a, 19, C["dark"], 700, "middle")
        f.text(gid, x + cw / 2, 968, b, 16, C["grey"], 400, "middle")


def frame(f: Fig, title, subtitle, tag, panel_title, items, numbered=True):
    # topptekst
    f.text("_", 60, 92, title, 46, C["ink"], 700)
    f.text("_", 60, 136, subtitle, 24, C["grey"], 400)
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, tag, 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    # sidepanel
    f.rect("_", 1450, 180, 410, 700, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1478, 226, panel_title, 25, C["ink"], 700)
    y = 276
    for i, (head, body) in enumerate(items):
        if numbered:
            f.badge(1497, y - 8, i + 1)
            tx = 1528
        else:
            tx = 1478
        f.text("_", tx, y, head, 21, C["ink"], 700)
        f.lines("_", tx, y + 28, body, 18, C["dark"], 400, lh=24)
        y += 28 + len(body) * 24 + 26

    # bunntekst: tegnforklaring
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    lx = 60
    def sw(fill, stroke, label, x):
        f.add(f'<rect x="{x}" y="{y-18}" width="24" height="24" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        f.text("_", x + 34, y, label, 17, C["dark"])
    f.person("_", lx + 12, y - 4, 0.45)
    f.text("_", lx + 34, y, "Person", 17, C["dark"])
    sw(C["purplel"], C["purple"], "Team og roller", 160)
    sw(C["greenl"], C["green"], "Data", 340)
    sw(C["tealp"], C["dark"], "Plattformtjeneste", 440)
    def ar(x, color, dash, label, sw_=3):
        f.arrow("_", [(x, y - 6), (x + 44, y - 6)], color, sw_, dash=dash, hs=10)
        f.text("_", x + 56, y, label, 17, C["dark"])
    ar(660, C["dark"], None, "Medlem av", 2)
    ar(820, C["purple"], None, "Tilgang")
    ar(960, C["purple"], "8 6", "Tidsavgrenset tilgang")
    ar(1210, C["green"], None, "Dataflyt")
    ar(1350, C["green"], "8 5", "Deling")
    f.text("_", 1860, y, f"Utkast {DATO} · Kilde: manual.dapla.ssb.no", 16, C["grey"], 400, "end")


# ---------- variantene ----------
V = []

V.append(dict(
    file="0-oversikt.svg", hi=None, tag="Oversikt",
    title="Tilgang følger teamet, ikke personen",
    subtitle="Brukere, Dapla-team og data på Dapla",
    panel="Fire grunnprinsipper",
    items=[("Tilgang via team", ["Man jobber på Dapla som medlem", "av et team. Tilgang gis til", "grupper i teamet."]),
           ("Teamet eier sine data", ["Hvert team har egne prosjekter", "og bøtter, og ansvaret ligger", "hos én seksjon."]),
           ("Kildedata er skjermet", ["Sensitive kildedata ligger isolert,", "uten fast tilgang for noen."]),
           ("Deling er eksplisitt", ["Andre team får bare det eier-", "teamet har valgt å dele."])],
    badges=[]))

V.append(dict(
    file="1-tilgang.svg", tag="Fokus 1 av 4",
    hi={"persons", "member", "team", "ta", "da", "dev", "acc_da", "acc_dev", "kilde", "std", "prod", "ctrl"},
    title="Tilgang gis til roller i teamet",
    subtitle="Fokus: hvem får se hva",
    panel="Roller og tilgang",
    items=[("Via gruppe, ikke person", ["Personer legges inn i en gruppe", "i teamet. Tilgangen følger", "gruppen."]),
           ("Developers", ["Leser og skriver alle data fra", "inndata til utdata. Ingen tilgang", "til kildedata."]),
           ("Data-admins", ["2–3 personer. Kan få tidsavgrenset", "tilgang (JIT) til kildedata med", "skriftlig begrunnelse. Logges."]),
           ("Teamansvarlig", ["Seksjonslederen bestemmer hvem", "som er med, men har selv ingen", "tilgang til data."])],
    badges=[(278, 410), (608, 590), (644, 470), (608, 292)]))

V.append(dict(
    file="2-eierskap.svg", tag="Fokus 2 av 4",
    hi={"team", "kilde", "std", "prod", "kildomaten", "da", "kchip"},
    title="Teamet eier sine data, og kildedata er skjermet",
    subtitle="Fokus: eierskap og skjerming",
    panel="Fra kildedata til inndata",
    items=[("Ett team, én seksjon", ["Teamet har egne prosjekter og", "bøtter. Ansvaret ligger hos", "seksjonen."]),
           ("Kildeprosjekt", ["Kildedata ligger isolert.", "Ingen har fast tilgang."]),
           ("Kildomaten", ["Kjører teamets kode automatisk", "på nye kildedata, og pseudo-", "nymiserer før data blir inndata.", "Data-admins godkjenner koden."]),
           ("Standardprosjekt", ["Inndata til utdata i produkt-", "bøtta, der teamet jobber daglig."])],
    badges=[(1080, 214), (680, 292), (728, 537), (680, 562)]))

V.append(dict(
    file="3-deling.svg", tag="Fokus 3 av 4",
    hi={"std", "delt", "others", "share", "dp", "dp_arr", "iac", "dpchip"},
    title="Deling skjer bevisst og eksplisitt",
    subtitle="Fokus: deling mellom team og finnbarhet",
    panel="Slik deles data",
    items=[("Egen delt-bøtte", ["Det som skal deles, legges i en", "egen bøtte. Resten av produkt-", "bøtta forblir teamets."]),
           ("Eierteamet bestemmer", ["Lesetilgang gis til navngitte", "grupper i teamets konfigurasjon.", "Data-admins godkjenner."]),
           ("Finnbart i Dataportalen", ["Metadata gjør datasett synlige", "på tvers, slik at andre vet hva", "som finnes og hvem som eier det."])],
    badges=[(944, 640), (1150, 790), (1400, 292)]))

V.append(dict(
    file="4-selvbetjening.svg", tag="Fokus 4 av 4",
    hi={"platform", "lab", "ctrl", "iac", "kchip", "dpchip", "ta", "da", "team"},
    title="Teamene betjener seg selv",
    subtitle="Fokus: selvbetjening på felles plattform",
    panel="Hva teamet gjør selv",
    items=[("Dapla Ctrl", ["Seksjonslederen oppretter team", "og legger til medlemmer."]),
           ("Team-repo (IaC)", ["Bøtter, deling og tjenester", "konfigureres som kode. Data-", "admins godkjenner, endringen", "rulles ut automatisk."]),
           ("Dapla Lab", ["Hver bruker starter egne arbeids-", "miljøer (Jupyter, RStudio, VS", "Code) ved behov."]),
           ("Plattformteamet", ["Leverer byggeklossene, men", "godkjenner ikke hver enkelt", "tilgang."])],
    badges=[(487, 918), (714, 918), (260, 918), (60, 906)]))


def tegn(v):
    """Tegner én variant (oversikt eller fokus). Brukes også av nettside/bygg.py."""
    f = Fig(v["hi"])
    base(f)
    for x, y in v["badges"]:
        f.badge(x, y, v["badges"].index((x, y)) + 1)
    frame(f, v["title"], v["subtitle"], v["tag"], v["panel"], v["items"], numbered=bool(v["badges"]))
    return f


def main():
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in V:
        open(os.path.join(out, "orientering-tilgang-" + v["file"]), "w", encoding="utf-8").write(tegn(v).svg())
    print("ok")


if __name__ == "__main__":
    main()
