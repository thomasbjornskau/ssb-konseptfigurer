"""Teknisk × Ansvar og tilgang.
Samme logikk som orienteringsfiguren (person → rolle → ressurs), detaljert med
mekanisme (hvordan tilgangen gis) og maskinidentiteter. Oversikt + fire fokus."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"
from teknisk_struktur import box, pill

PT = "#4b2fb0"
U = "5 4"
GREYF = "#f3f5f5"
COLX = [60, 330, 650, 980]   # hvem · gruppe · mekanisme · ressurs


def base(f):
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    heads = [("Hvem", "identitet"), ("Gruppe i teamet", "rolle"), ("Mekanisme", "hvordan tilgangen gis"), ("Ressurs", "hva det gis tilgang til")]
    for x, (h, s) in zip(COLX, heads):
        f.text("hdr", x, 206, h, 20, C["ink"], 700)
        f.text("hdr", x, 230, s, 15, C["grey"])
    f.add(f'<line x1="60" y1="244" x2="1400" y2="244" stroke="{C["line"]}" stroke-width="1.5"/>')

    # identitetskjede (ubekreftet)
    f.rect("idp", 60, 256, 220, 40, C["white"], C["grey"], 1.5, 20, dash=U)
    f.text("idp", 170, 282, "Identitetsløsning → grupper ?", 14, C["grey"], 600, "middle")

    # ---- personer ----
    ppl = [(348, "Seksjonsleder", "ta"), (444, "Statistiker", "da"), (580, "Statistiker", "dev"), (660, "Utvikler", "dev")]
    for cy, lab, g in ppl:
        f.person(f"p_{g}", 96, cy, 0.7)
        f.text(f"p_{g}", 128, cy + 8, lab, 17, C["ink"])

    # ---- grupper ----
    f.rect("ta", 330, 316, 260, 70, C["white"], C["purple"], 2, 8)
    f.text("ta", 346, 344, "Teamansvarlig", 19, PT, 700)
    f.text("ta", 346, 368, "seksjonsleder", 14, C["grey"])
    f.rect("da", 330, 408, 260, 76, C["purplel"], C["purple"], 2, 8)
    f.text("da", 346, 436, "data-admins", 19, PT, 700)
    f.text("da", 346, 460, "2–3 personer", 14, C["ink"])
    f.rect("dev", 330, 540, 260, 150, C["purplel"], C["purple"], 2, 8)
    f.text("dev", 346, 568, "developers", 19, PT, 700)
    f.text("dev", 346, 592, "alle som jobber med data", 14, C["ink"])
    f.rect("oth", 330, 716, 260, 64, C["purplep"], C["purple"], 1.5, 8)
    f.text("oth", 346, 742, "Andre team", 17, PT, 700)
    f.text("oth", 346, 764, "grupper oppført i sharedWith", 13, C["grey"])

    for cy, g in [(348, "ta"), (444, "da"), (580, "dev"), (660, "dev")]:
        f.arrow(f"p_{g}", [(252, cy), (328, cy)], C["dark"], 1.8, hs=9)

    # ---- mekanismer ----
    box(f, "m_ctrl", 650, 316, 270, 70, "Dapla Ctrl", ["legger til og fjerner medlemmer"], tsize=17)
    box(f, "m_jit", 650, 408, 270, 90, "JIT-tilgang", ["tidsavgrenset · begrunnet", "logget og overvåket"], tsize=17)
    box(f, "m_iam", 650, 560, 270, 76, "Fast IAM-binding", ["gruppe → rolle på bøtte"], tsize=17)
    box(f, "m_iac", 650, 708, 270, 90, "IaC i team-repo", ["sharedWith i buckets-shared", "PR · data-admins · Atlantis"], tsize=17)

    f.arrow("ta", [(590, 351), (648, 351)], C["dark"], 2.2, hs=9)
    f.arrow("m_ctrl", [(785, 386), (785, 398), (470, 398), (470, 406)], C["dark"], 1.6, dash="3 4", hs=8) if False else None
    f.arrow("da", [(590, 446), (648, 446)], C["purple"], 3, dash="9 6", hs=11)
    f.arrow("dev", [(590, 620), (648, 620)], C["purple"], 4, hs=12)
    f.arrow("oth", [(590, 748), (648, 748)], C["green"], 3, dash="9 6", hs=11)

    # ---- ressurser ----
    f.text("ta", 980, 357, "Ingen datatilgang", 17, C["grey"], 600)
    f.add(f'<line x1="920" y1="351" x2="968" y2="351" stroke="{f.col("ta","stroke",C["line"])}" stroke-width="2" stroke-dasharray="3 4"/>')

    f.rect("kilde", 980, 392, 420, 128, C["white"], C["green"], 2, 10)
    f.text("kilde", 1000, 420, "Kildeprosjekt", 18, C["green"], 700)
    f.lock("kilde", 1360, 400, C["green"])
    f.cyl("kilde", 1000, 432, 160, 76, C["green"], C["green"])
    f.text("kilde", 1080, 478, "Kildebøtte", 15, C["white"], 700, "middle")
    f.lines("kilde", 1180, 460, ["ingen fast tilgang", "for personer"], 14, C["grey"], lh=18)

    f.rect("std", 980, 540, 420, 250, C["white"], C["green"], 2, 10)
    f.text("std", 1000, 568, "Standardprosjekt", 18, C["green"], 700)
    f.cyl("prod", 1000, 582, 200, 92, C["greenl"], C["green"])
    f.text("prod", 1100, 626, "Produktbøtte", 15, C["ink"], 700, "middle")
    f.text("prod", 1100, 648, "inndata … utdata", 13, C["ink"], 400, "middle")
    f.cyl("delt", 1230, 690, 150, 84, C["greenp"], C["green"])
    f.text("delt", 1305, 738, "Delt-bøtte", 15, C["ink"], 700, "middle")

    f.arrow("m_jit", [(920, 452), (998, 452)], C["purple"], 3, dash="9 6", hs=11)
    f.arrow("m_iam", [(920, 620), (998, 620)], C["purple"], 4, hs=12)
    f.arrow("m_iam", [(956, 620), (956, 700), (1228, 700)], C["purple"], 2.5, hs=10)
    f.text("m_iam", 1110, 692, "lese/skrive", 13, PT, 600, "middle")
    f.arrow("m_iac", [(920, 752), (1228, 752)], C["green"], 3, dash="9 6", hs=11)
    f.text("m_iac", 1080, 744, "kun lese", 13, C["green"], 700, "middle")

    # ---- maskinidentiteter ----
    f.rect("mach", 60, 812, 1340, 172, GREYF, "#b9c5c6", 1.5, 12)
    f.text("mach", 80, 842, "Maskinidentiteter", 19, C["ink"], 700)
    f.text("mach", 80, 864, "tjenestekontoer", 14, C["grey"])
    box(f, "sa_k", 330, 830, 300, 136, "Kildomaten", ["kjører automatisk på nye filer", "leser kildebøtte, skriver produktbøtte", "egen tjenestekonto ?"], sure=False, tsize=17)
    box(f, "sa_a", 650, 830, 270, 136, "Atlantis", ["ruller ut IaC etter", "godkjenning fra data-admins"], tsize=17)
    f.rect("sa_r", 940, 830, 440, 136, C["white"], C["purple"], 2, 8, dash="7 5")
    f.text("sa_r", 956, 858, "Invoker og Runner-SA", 17, PT, 700)
    pill(f, "sa_r", 1280, 840, 88, "forslag", C["purple"], "5 4")
    f.lines("sa_r", 956, 882, ["Invoker: får bare starte en jobb", "Runner-SA per team: bestemmer hvilke", "data jobben kan lese og skrive"], 14, C["grey"], lh=19)


def frame(f, v):
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
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
    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    def ar(x, color, dash, label, sw=3):
        f.arrow("_", [(x, y - 6), (x + 40, y - 6)], color, sw, dash=dash, hs=9)
        f.text("_", x + 50, y, label, 16, C["dark"])
    ar(60, C["dark"], None, "Medlem av / styrer", 2)
    ar(270, C["purple"], None, "Fast tilgang")
    ar(430, C["purple"], "8 6", "Tidsavgrenset tilgang")
    ar(660, C["green"], "8 6", "Deling (lese)")
    f.rect("_", 830, y - 20, 26, 24, C["white"], C["grey"], 1.8, 4, dash=U)
    f.text("_", 866, y, "Ubekreftet", 16, C["dark"])
    f.rect("_", 970, y - 20, 26, 24, C["white"], C["purple"], 2, 4, dash="7 5")
    f.text("_", 1006, y, "Forslag", 16, C["dark"])
    f.text("_", 1860, y, f"Utkast {DATO} · Kilder: Dapla-manualen, notat om orkestrering (forslag)", 15, C["grey"], 400, "end")


PERS = {"idp", "p_ta", "p_da", "p_dev", "ta", "da", "dev", "m_ctrl", "m_iam", "std", "prod"}
V = [
    dict(file="0-oversikt.svg", hi=None, tag="Oversikt",
         title="Tilgang: grupper for personer, kontoer for maskiner",
         sub="Teknisk ansvar og tilgang · detaljert utgave av orienteringsfiguren",
         panel="Fra orientering til teknikk",
         items=[("Samme tre roller", ["Teamansvarlig, data-admins og", "developers, nå vist som grupper", "med konkrete mekanismer."]),
                ("Tilgang via mekanisme", ["Fast IAM-binding, JIT eller IaC.", "Ingen får tilgang direkte som", "enkeltperson."]),
                ("To slags identiteter", ["Personer via grupper. Maskiner", "via tjenestekontoer, som", "Kildomaten og Atlantis."]),
                ("Ubekreftet", ["Identitetskjeden inn til GCP", "og hvilke tjenestekontoer som", "faktisk finnes."])]),
    dict(file="1-personer.svg", tag="Fokus 1 av 4", hi=PERS,
         title="Personer får tilgang gjennom grupper",
         sub="Fokus: medlemskap og fast tilgang",
         panel="Personer og grupper",
         items=[("Identitetskjeden", ["Hvordan en person havner i en", "gruppe i GCP, er ikke bekreftet."]),
                ("Teamansvarlig styrer", ["Legger til og fjerner medlemmer", "i Dapla Ctrl. Har selv ingen", "datatilgang."]),
                ("Developers: fast tilgang", ["Gruppen har IAM-binding til", "produkt- og delt-bøtta. Ingen", "tilgang til kildedata."])],
         badges=[(60, 256), (650, 316), (650, 560)]),
    dict(file="2-kildedata.svg", tag="Fokus 2 av 4",
         hi={"p_da", "da", "m_jit", "kilde", "sa_k", "mach"},
         title="Kildedata: ingen fast tilgang for noen",
         sub="Fokus: JIT for data-admins og automatisk behandling",
         panel="Skjerming av kildedata",
         items=[("data-admins", ["2–3 personer per team. Godkjenner", "jobber og IaC-endringer."]),
                ("JIT-tilgang", ["Tidsavgrenset tilgang til klartekst,", "med skriftlig begrunnelse.", "Tilgangen overvåkes."]),
                ("Maskin, ikke menneske", ["Kildomaten behandler kildedata", "automatisk. Om den kjører med egen", "tjenestekonto, er ikke bekreftet."])],
         badges=[(330, 408), (650, 408), (330, 830)]),
    dict(file="3-deling.svg", tag="Fokus 3 av 4",
         hi={"oth", "m_iac", "std", "delt", "da"},
         title="Deling er konfigurasjon, ikke unntak",
         sub="Fokus: tilgang på tvers av team",
         panel="Deling mellom team",
         items=[("Egen delt-bøtte", ["Bare det som legges der, kan", "deles. Produktbøtta forblir", "teamets."]),
                ("sharedWith i IaC", ["Eierteamet fører opp gruppene", "som skal få lese, i team-repoet.", "Data-admins godkjenner PR-en."]),
                ("Kun lesetilgang", ["Andre team får lese, ikke skrive.", "Personopplysninger deles via", "Delomaten (ikke tegnet)."])],
         badges=[(1230, 690), (650, 708), (330, 716)]),
    dict(file="4-maskiner.svg", tag="Fokus 4 av 4",
         hi={"mach", "sa_k", "sa_a", "sa_r", "da"},
         title="Maskiner har også identitet",
         sub="Fokus: tjenestekontoer i dag og i forslaget",
         panel="Maskinidentiteter",
         items=[("Kildomaten", ["Kjører automatisk på nye filer.", "Tjenestekontoen er min tolkning,", "ikke dokumentert."]),
                ("Atlantis", ["Ruller ut IaC-endringer etter", "godkjenning fra data-admins."]),
                ("Forslag: to identiteter", ["Invoker får bare starte en jobb.", "Runner-SA bestemmer datatilgang.", "Orkestratoren kan da byttes uten", "å endre rettigheter."])],
         badges=[(330, 830), (650, 830), (940, 830)]),
]


def main():
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in V:
        f = Fig(v["hi"])
        base(f)
        frame(f, v)
        open(os.path.join(out, "teknisk-tilgang-" + v["file"]), "w", encoding="utf-8").write(f.svg())
    print("ok")


if __name__ == "__main__":
    main()
