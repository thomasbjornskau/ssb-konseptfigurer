"""Dapla · Orientering × Ansvar og tilgang · 01 Konseptfoil.
Få elementer, direkte merket, samme geometri som oversikten (klar for Morph i PowerPoint)."""
import os
from konseptfigurer.fig import Fig, C
from konseptfigurer.sekvens import topp, svarpanel, grunnbegreper
from konseptfigurer.sti import utdata

DATO = "30.09.2026"
PT = "#4b2fb0"


def build():
    f = Fig(None)
    topp(f, "Tilgang følger teamet", "Det enkle bildet", "Konsept")

    # ansatte (samme plass som i oversikten)
    f.text("_", 165, 212, "Ansatte", 24, C["dark"], 700, "middle")
    for cy in (330, 490, 628, 748):
        f.person("_", 165, cy - 14, 0.9)
    # medlemskap
    f.arrow("_", [(215, 540), (318, 540)], C["dark"], 4, hs=14)
    f.text("_", 262, 522, "medlem av", 17, C["dark"], 700, "middle")
    f.badge(266, 578, 1)

    # teamet
    f.rect("_", 320, 180, 790, 700, C["purplep"], C["purple"], 3, 16)
    f.text("_", 350, 234, "Dapla-team", 34, PT, 700)
    f.text("_", 350, 270, "eier og har ansvar for sine data", 20, PT, 600)
    f.badge(1080, 214, 2)

    # kildedata (skjermet)
    f.cyl("_", 730, 348, 180, 110, C["green"], C["green"])
    f.text("_", 820, 408, "Kildedata", 20, C["white"], 700, "middle")
    f.lock("_", 928, 372, C["green"])
    f.text("_", 966, 392, "skjermet", 20, C["green"], 700)
    f.badge(730, 360, 3)

    # teamets data
    f.cyl("_", 700, 618, 210, 150, C["greenl"], C["green"])
    f.text("_", 805, 690, "Teamets data", 20, C["ink"], 700, "middle")
    f.text("_", 805, 716, "for alle i teamet", 16, C["ink"], 400, "middle")

    # andre team
    f.rect("_", 1160, 600, 240, 160, C["purplep"], C["purple"], 2.5, 12)
    f.text("_", 1280, 688, "Andre team", 22, PT, 700, "middle")
    f.arrow("_", [(912, 690), (1158, 690)], C["green"], 4, dash="12 8", hs=14)
    f.text("_", 1035, 674, "det som deles", 18, C["green"], 700, "middle")
    f.badge(1035, 722, 4)

    svarpanel(f, [("Ikke som person.", "Via teamet."), ("Teamet,", "og seksjonen bak."),
                  ("Kildedata.", "Ingen har fast tilgang."), ("Bare det teamet", "velger å dele.")])
    grunnbegreper(f, [("person", "Person"), ("team", "Team"), ("data", "Data")], f"{DATO} · Utkast · Variant A")
    return f


if __name__ == "__main__":
    open(os.path.join(utdata("dapla"), "orientering-tilgang-01-konsept.svg"), "w", encoding="utf-8").write(build().svg())
    print("ok")
