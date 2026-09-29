"""Teknisk × Struktur: soner, grenser og byggeklosser i Dapla.
Oversikt + fem fokusvarianter. Stiplet = ubekreftet. Merket INTERN (jf. ADR0026)."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
ONPREM = "#f3f5f5"
U = "5 4"  # stiplet = ubekreftet


def box(f, gid, x, y, w, h, title, subs=(), sure=True, fill=None, tsize=19):
    f.rect(gid, x, y, w, h, fill or C["white"], C["dark"] if sure else C["grey"], 2 if sure else 1.8, 8,
           dash=None if sure else U)
    tc = C["ink"] if sure else C["grey"]
    f.text(gid, x + 14, y + 28, title, tsize, tc, 700)
    for i, s in enumerate(subs):
        f.text(gid, x + 14, y + 50 + i * 20, s, 15, C["grey"])


def pill(f, gid, x, y, w, label, color=None, dash=None):
    color = color or C["dark"]
    f.rect(gid, x, y, w, 26, C["white"], color, 1.5, 13, dash=dash)
    f.text(gid, x + w / 2, y + 18, label, 14, color, 600, "middle")


def base(f):
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')

    # ---------- Google Cloud ----------
    f.rect("gcp", 60, 180, 1020, 810, C["white"], C["dark"], 2.5, 14)
    f.text("gcp", 80, 208, "Google Cloud", 20, C["dark"], 700)

    # Bånd A: arbeidsflate og kjøremiljø
    f.rect("A", 76, 222, 988, 104, C["tealp"], C["tealp"], 0, 10)
    f.text("A", 1026, 244, "Arbeidsflate og kjøremiljø", 15, C["grey"], 700, "end")
    box(f, "lab", 90, 252, 230, 64, "Dapla Lab", ["Jupyter · RStudio · VS Code"])
    box(f, "onyxia", 390, 252, 180, 64, "Onyxia", ["tjenestekatalog"])
    box(f, "k8s", 640, 252, 180, 64, "Kubernetes", ["containere"])
    box(f, "nais", 850, 252, 150, 64, "NAIS", ["applikasjoner"])
    f.arrow("dep1", [(320, 290), (388, 290)], C["grey"], 2, hs=9)
    f.text("dep1", 355, 280, "bygger på", 13, C["grey"], 600, "middle")
    f.arrow("dep2", [(570, 290), (638, 290)], C["grey"], 2, hs=9)
    f.text("dep2", 605, 280, "kjører på", 13, C["grey"], 600, "middle")

    # Bånd C: per team
    f.rect("team", 76, 342, 988, 262, C["purplep"], C["purple"], 2, 10)
    f.text("team", 92, 368, "Per team · × N", 17, PT, 700)
    f.text("team", 1050, 596, "test og prod er like", 14, PT, 600, "end")
    # skygger = gjentas per team/miljø
    for gid, x, w in (("std", 90, 470), ("kilde", 590, 460)):
        f.rect(gid, x + 7, 387, w, 196, C["white"], C["purplel"], 1.5, 10)
    f.rect("std", 90, 380, 470, 196, C["white"], C["green"], 2, 10)
    f.text("std", 110, 406, "Standardprosjekt", 19, C["green"], 700)
    f.cyl("std", 110, 424, 200, 128, C["greenl"], C["green"])
    f.text("std", 210, 480, "Produktbøtte", 18, C["ink"], 700, "middle")
    f.text("std", 210, 504, "inndata … utdata", 15, C["ink"], 400, "middle")
    f.cyl("delt", 380, 470, 150, 90, C["greenp"], C["green"])
    f.text("delt", 455, 522, "Delt-bøtte", 16, C["ink"], 700, "middle")

    f.rect("kilde", 590, 380, 460, 196, C["white"], C["green"], 2, 10)
    f.text("kilde", 610, 406, "Kildeprosjekt", 19, C["green"], 700)
    f.lock("kilde", 1014, 386, C["green"])
    f.cyl("kilde", 850, 424, 180, 128, C["green"], C["green"])
    f.text("kilde", 940, 492, "Kildebøtte", 18, C["white"], 700, "middle")
    box(f, "kdm", 612, 424, 200, 136, "Kildomaten", ["levert av plattformen,", "rulles ut per team"], tsize=18)
    pill(f, "kdm", 626, 522, 172, "+ pseudonymisering", C["green"])
    f.arrow("flow", [(850, 480), (814, 480)], C["green"], 3, hs=10)
    f.arrow("flow", [(612, 448), (312, 448)], C["green"], 3, hs=11)
    # Dapla Lab -> produktbøtte
    f.arrow("labrw", [(290, 316), (290, 432)], C["dark"], 2.5, hs=10)
    f.text("labrw", 300, 372, "leser/skriver", 14, C["dark"], 600)

    # Bånd B: felles plattformtjenester
    f.rect("B", 76, 620, 988, 356, C["tealp"], C["tealp"], 0, 10)
    f.text("B", 92, 646, "Felles plattformtjenester · driftes én gang", 17, C["dark"], 700)
    box(f, "meta", 90, 662, 440, 136, "Metadatatjenester", ["API-er · egne databaser"])
    for i, n in enumerate(["Vardef", "Datadoc", "Klass"]):
        pill(f, "meta", 104 + i * 104, 734, 94, n, C["dark"], None if n != "Klass" else U)
    f.cyl("meta", 440, 690, 72, 84, C["white"], C["dark"])
    f.text("meta", 476, 744, "DB", 15, C["dark"], 700, "middle")
    f.lines("meta", 104, 786, ["Kotlin / Micronaut (ADR0023)"], 13, C["grey"])
    box(f, "dp", 560, 662, 220, 136, "SSB Dataportal", ["datakatalog"])
    f.arrow("dparr", [(530, 740), (558, 740)], C["dark"], 2, dash="5 4", hs=9)
    box(f, "ctrl", 810, 662, 240, 136, "Dapla Ctrl", ["team og medlemskap"])

    box(f, "keys", 90, 818, 230, 142, "Pseudo-nøkler", ["kryptonøkler", "plassering ?"], sure=False)
    box(f, "gsm", 340, 818, 200, 142, "Secret Manager", ["hemmeligheter"])
    box(f, "pubsub", 560, 818, 180, 142, "Pub/Sub", ["hendelser"])
    box(f, "suv", 760, 818, 290, 142, "Integrasjonstjeneste", ["SUV · API mot on-prem", "via ORDS-klient"])
    pill(f, "suv", 774, 924, 110, "midlertidig", C["grey"])

    # ---------- Utenfor GCP ----------
    box(f, "gh", 1110, 180, 290, 124, "GitHub", ["kode og IaC-repo per team"])
    pill(f, "gh", 1124, 262, 160, "Atlantis ruller ut", C["dark"])
    f.arrow("iac", [(1110, 232), (1040, 232), (1040, 378)], C["dark"], 2.5, hs=10)
    f.text("iac", 1032, 366, "konfigurerer", 14, C["dark"], 600, "end")

    box(f, "idp", 1110, 318, 290, 86, "Identitetsløsning", ["personer → grupper → IAM ?"], sure=False)

    f.rect("onprem", 1110, 420, 290, 432, ONPREM, "#b9c5c6", 2, 12)
    f.text("onprem", 1126, 446, "On-prem SSB", 18, C["dark"], 700)
    box(f, "files", 1122, 458, 266, 96, "Filområder", ["Transfer Service,", "filer, maks 1 gang/time"], fill=C["white"])
    f.arrow("transfer", [(1122, 490), (1032, 490)], C["green"], 3, hs=11)
    box(f, "papis", 1122, 568, 266, 84, "PAPIS", ["pseudonymisering on-prem"], fill=C["white"])
    box(f, "oracle", 1122, 666, 266, 96, "Oracle-databaser", ["eksponert via ORDS"], fill=C["white"])
    f.arrow("ords", [(1122, 714), (1094, 714), (1094, 880), (1052, 880)], C["dark"], 2.5, dash="5 4", hs=10)

    f.rect("ext", 1110, 868, 290, 122, ONPREM, "#b9c5c6", 2, 12)
    f.text("ext", 1126, 896, "Eksterne", 18, C["dark"], 700)
    f.lines("ext", 1126, 926, ["Altinn 3 · Maskinporten"], 16, C["ink"])


def frame(f, v):
    f.text("_", 60, 92, v["title"], 46, C["ink"], 700)
    f.text("_", 60, 136, v["sub"], 24, C["grey"])
    f.rect("_", 1520, 62, 150, 40, C["ink"], C["ink"], 0, 20)
    f.text("_", 1595, 89, "INTERN", 19, C["white"], 700, "middle")
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, v["tag"], 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    f.rect("_", 1440, 180, 420, 810, C["tealp"], C["tealp"], 0, 16)
    f.text("_", 1466, 226, v["panel"], 25, C["ink"], 700)
    y = 276
    num = bool(v.get("badges"))
    for i, (head, body) in enumerate(v["items"]):
        tx = 1516 if num else 1466
        if num:
            f.badge(1485, y - 8, i + 1)
        f.text("_", tx, y, head, 20, C["ink"], 700)
        f.lines("_", tx, y + 27, body, 17, C["dark"], lh=23)
        y += 27 + len(body) * 23 + 24
    for x, yy in v.get("badges", []):
        f.badge(x, yy, v["badges"].index((x, yy)) + 1)

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    y = 1046
    f.rect("_", 60, y - 20, 26, 24, C["white"], C["dark"], 2, 4)
    f.text("_", 96, y, "Bekreftet", 16, C["dark"])
    f.rect("_", 190, y - 20, 26, 24, C["white"], C["grey"], 1.8, 4, dash=U)
    f.text("_", 226, y, "Ubekreftet", 16, C["dark"])
    f.rect("_", 330, y - 20, 26, 24, C["purplep"], C["purple"], 2, 4)
    f.text("_", 366, y, "Per team", 16, C["dark"])
    f.rect("_", 452, y - 20, 26, 24, C["tealp"], C["teal"], 2, 4)
    f.text("_", 488, y, "Felles", 16, C["dark"])
    def ar(x, color, dash, label, sw=2.5):
        f.arrow("_", [(x, y - 6), (x + 40, y - 6)], color, sw, dash=dash, hs=9)
        f.text("_", x + 50, y, label, 16, C["dark"])
    ar(566, C["green"], None, "Dataflyt", 3)
    ar(700, C["dark"], None, "Styrer / konfigurerer")
    ar(920, C["dark"], "5 4", "API-kall")
    ar(1050, C["grey"], None, "Avhengighet", 2)
    f.text("_", 1860, y, f"Utkast {DATO} · Kilder: Dapla-manualen, ADR0015, 0017, 0023, 0026", 15, C["grey"], 400, "end")


ALL = None
V = [
    dict(file="0-oversikt.svg", hi=ALL, tag="Oversikt",
         title="Dapla: soner, grenser og byggeklosser",
         sub="Teknisk struktur · hva kjører hvor, og hva avhenger av hva",
         panel="Slik leses figuren",
         items=[("Soner er grenser", ["Google Cloud, on-prem og eksterne", "er egne soner. Piler over en grense", "er integrasjonspunkter."]),
                ("Lilla gjentas per team", ["Prosjekter, bøtter og Kildomaten", "rulles ut likt for hvert team,", "i både test og prod."]),
                ("Blågrønt driftes én gang", ["Arbeidsflate og plattformtjenester", "er felles for alle team."]),
                ("Stiplet er ubekreftet", ["Må avklares med plattformteamet", "før figuren tas i bruk."])]),
    dict(file="1-kjoremiljo.svg", tag="Fokus 1 av 5",
         hi={"gcp", "A", "lab", "onyxia", "k8s", "nais", "dep1", "dep2", "labrw", "std"},
         title="Arbeidsflate og kjøremiljø",
         sub="Fokus: hva brukerne jobber i, og hva det kjører på",
         panel="Kjøremiljø",
         items=[("Dapla Lab bygger på Onyxia", ["SSBs arbeidsflate er en tilpasset", "Onyxia med tjenestekatalog for", "Jupyter, RStudio og VS Code."]),
                ("Onyxia kjører på Kubernetes", ["Hver bruker starter egne containere", "ved behov."]),
                ("Tilgang via teamet", ["Tjenestene leser og skriver teamets", "bøtter med teamgruppens rettigheter."]),
                ("NAIS for applikasjoner", ["ADR0026 legger opp til NAIS.", "Hvilke tjenester som kjører der,", "er ikke bekreftet."])],
         badges=[(90, 252), (640, 252), (290, 372), (850, 252)]),
    dict(file="2-data.svg", tag="Fokus 2 av 5",
         hi={"gcp", "team", "std", "delt", "kilde", "kdm", "flow", "transfer", "files", "onprem", "keys"},
         title="Data og lagring",
         sub="Fokus: teamets prosjekter, bøtter og veien fra kildedata",
         panel="Data per team",
         items=[("Samme mønster for alle team", ["Kildeprosjekt og standardprosjekt,", "i både test og prod."]),
                ("Kildeprosjektet er isolert", ["Kildebøtta har ingen fast tilgang.", "Data kommer inn via Transfer", "Service eller integrasjoner."]),
                ("Kildomaten rulles ut per team", ["Levert av plattformen, men kjører", "i teamets kildeprosjekt med", "teamets egen kode."]),
                ("Pseudonymisering er krypto", ["Ingen sentral koblingstabell. Nøkler", "er fellesleddet (ADR0015, foreslått).", "Hvor nøklene ligger: ubekreftet."])],
         badges=[(76, 342), (590, 380), (612, 424), (90, 818)]),
    dict(file="3-konfig-identitet.svg", tag="Fokus 3 av 5",
         hi={"gh", "iac", "idp", "ctrl", "gsm", "team", "std", "kilde"},
         title="Konfigurasjon og identitet",
         sub="Fokus: hvordan team, tilganger og ressurser blir til",
         panel="Styring som kode",
         items=[("Team-repo med IaC", ["Bøtter, deling og tjenester", "defineres i teamets repo. Data-", "admins godkjenner, Atlantis", "ruller ut."]),
                ("Dapla Ctrl", ["Oppretter team og styrer", "medlemskap i teamgruppene."]),
                ("Identitet", ["Hvordan personer og grupper når", "IAM i GCP, er ikke bekreftet."]),
                ("Secret Manager", ["Hemmeligheter ligger utenfor Git,", "med tilgang via IAM og grupper", "(ADR0026, foreslått)."])],
         badges=[(1110, 180), (810, 662), (1110, 318), (340, 818)]),
    dict(file="4-metadata.svg", tag="Fokus 4 av 5",
         hi={"meta", "dp", "dparr", "B"},
         title="Metadatatjenester",
         sub="Fokus: tjenestene som beskriver data, og katalogen over dem",
         panel="Metadata som tjenester",
         items=[("Backend-tjenester med API", ["Team Metadata bygger tjenestene i", "Kotlin/Micronaut som containere", "(ADR0023, akseptert)."]),
                ("Egne databaser", ["Metadata lagres i tjenestenes egne", "databaser, ikke i teamenes bøtter."]),
                ("Dataportalen leser", ["SSB Dataportal viser metadata på", "tvers som datakatalog."]),
                ("Åpne spørsmål", ["Hvilke tjenester ADR0023 gjelder,", "om Klass følger samme mønster,", "og hvor brukerflatene kjører."])],
         badges=[(90, 662), (440, 690), (560, 662), (290, 734)]),
    dict(file="5-integrasjoner.svg", tag="Fokus 5 av 5",
         hi={"onprem", "files", "papis", "oracle", "transfer", "ords", "suv", "ext", "keys", "kilde"},
         title="Integrasjoner over grensen",
         sub="Fokus: der data og avhengigheter krysser ut av Google Cloud",
         panel="Integrasjonspunkter",
         items=[("Transfer Service", ["Filer fra on-prem til teamets", "kildebøtte. Maks én gang i timen."]),
                ("ORDS via SUV-tjenesten", ["Nær sanntid mot Oracle on-prem,", "bak ett API. Midlertidig, med exit-", "strategi (ADR0017, vedtatt 2023).", "Status i dag: ubekreftet."]),
                ("PAPIS-kompatibilitet", ["Stabil ID pseudonymiseres med FPE", "for å kunne kobles mot on-prem."]),
                ("Eksterne kilder", ["Altinn 3 og Maskinporten. Hvordan", "de kobles til, er ikke tegnet ennå."])],
         badges=[(1388, 458), (1050, 818), (1388, 568), (1400, 868)]),
]


def main():
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for v in V:
        hi = v["hi"]
        f = Fig(hi)
        base(f)
        frame(f, v)
        open(os.path.join(out, "teknisk-struktur-" + v["file"]), "w", encoding="utf-8").write(f.svg())
    print("ok")


if __name__ == "__main__":
    main()
