"""Dapla · Orientering × Ansvar og tilgang · 01 Konseptfoil, variant B.
Én idé: innenfor/utenfor. Samme person vist to ganger, før og etter at den blir med i teamet.
Samme geometri som oversikten (klar for Morph i PowerPoint)."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sekvens import topp, svarpanel, grunnbegreper
from konseptfigurer.sti import utdata

DATO = "30.09.2026"
PT = "#4b2fb0"
GREYS = "#b9c5c6"


def build():
    f = Fig(None)
    topp(f, "Du ser data fordi du er i et team", "Utenfor teamet ser du ingenting. Innenfor ser du det teamet har.", "Konsept")

    # teamet (samme ramme som i oversikten)
    f.rect("_", 320, 180, 790, 700, C["purplep"], C["purple"], 3, 16)
    f.text("_", 350, 234, "Dapla-team", 34, PT, 700)
    f.text("_", 350, 270, "eier dataene sine", 20, PT, 600)
    f.badge(1080, 214, 2)

    # utenfor: samme person, grå
    f.person("_", 165, 540, 1.4, GREYS)
    f.text("_", 165, 624, "Utenfor", 22, C["grey"], 700, "middle")
    f.text("_", 165, 652, "ser ingen data", 18, C["grey"], 400, "middle")

    # overgang: blir medlem
    f.arrow("_", [(222, 540), (398, 540)], C["dark"], 4, hs=14)
    f.lines("_", 268, 488, ["blir", "medlem"], 19, C["dark"], 700, "middle", lh=23)
    f.badge(268, 576, 1)

    # innenfor: samme person, lilla
    f.person("_", 460, 540, 1.4, C["purple"])
    f.text("_", 460, 624, "Innenfor", 22, PT, 700, "middle")
    f.text("_", 460, 652, "ser teamets data", 18, PT, 400, "middle")

    # teamets data og blikket dit
    f.arrow("_", [(515, 560), (690, 650)], C["green"], 3, hs=12)
    f.cyl("_", 700, 590, 240, 180, C["greenl"], C["green"])
    f.text("_", 820, 690, "Teamets data", 24, C["ink"], 700, "middle")

    # kildedata: låst rom i rommet
    f.rect("_", 690, 300, 390, 200, C["white"], C["green"], 2, 12, dash="10 7")
    f.cyl("_", 720, 340, 150, 110, C["green"], C["green"])
    f.text("_", 795, 402, "Kildedata", 19, C["white"], 700, "middle")
    f.lock("_", 900, 356, C["green"])
    f.lines("_", 944, 378, ["låst, også", "for teamet"], 20, C["green"], 700, lh=26)
    f.badge(690, 300, 3)

    # andre team: bare det som deles
    f.rect("_", 1160, 600, 240, 160, C["white"], GREYS, 2.5, 12)
    f.text("_", 1280, 688, "Andre team", 22, C["grey"], 700, "middle")
    f.arrow("_", [(942, 680), (1158, 680)], C["green"], 4, dash="12 8", hs=14)
    f.text("_", 1025, 664, "det som deles", 18, C["green"], 700, "middle")
    f.badge(1135, 646, 4)

    svarpanel(f, [("Via teamet.", "Aldri direkte som person."), ("Teamet eier.", "Seksjonen står bak."),
                  ("Kildedata er låst.", "Ingen har fast tilgang."), ("Bare det som deles,", "ser andre.")],
              regel=["Tilgang følger", "teamet, ikke", "personen."])
    grunnbegreper(f, [("person", "Person"), ("team", "Team"), ("data", "Data")], f"{DATO} · Utkast · Variant B")
    return f


if __name__ == "__main__":
    open(os.path.join(utdata("dapla"), "orientering-tilgang-01-konsept-b.svg"), "w", encoding="utf-8").write(build().svg())
    print("ok")
