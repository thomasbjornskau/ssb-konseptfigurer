"""Dapla · Orientering × Ansvar og tilgang · 00 Spørsmålsfoil.
Samme geometri som oversikten: spørsmålene står der svarene kommer."""
import os
from konseptfigurer.fig import Fig
from konseptfigurer.sekvens import topp, sone, sporsmal, plassholderpanel, grunnbegreper
from konseptfigurer.sti import utdata

DATO = "30.09.2026"


def build():
    f = Fig(None)
    topp(f, "Hvem får se hvilke data på Dapla?", "Fire spørsmål som de neste bildene svarer på", "Spørsmål")

    # svake konturer av oversiktens soner (samme geometri)
    sone(f, 60, 180, 220, 700)        # ansatte
    sone(f, 320, 180, 790, 700, 16)   # teamet
    sone(f, 680, 292, 400, 222, 12)   # kildeprosjekt
    sone(f, 680, 562, 400, 296, 12)   # standardprosjekt
    sone(f, 1160, 290, 240, 470)      # andre team / dataportal
    sone(f, 60, 906, 1340, 84, 12)    # felles plattform

    # spørsmålene står der svarene kommer
    for cy in (330, 490, 628, 748):
        f.person("_", 120, cy, 0.9, "#cfd8d8")
    sporsmal(f, 1, 380, 360, ["Får du tilgang", "som person?"])
    sporsmal(f, 2, 380, 640, ["Hvem eier", "dataene?"])
    sporsmal(f, 3, 740, 400, ["Hva er ekstra", "beskyttet?"])
    sporsmal(f, 4, 1220, 500, ["Hvordan", "deles data", "med andre?"])

    plassholderpanel(f, 4)
    grunnbegreper(f, [("person", "Person"), ("team", "Team"), ("data", "Data")], f"{DATO} · Utkast")
    return f


if __name__ == "__main__":
    open(os.path.join(utdata("dapla"), "orientering-tilgang-00-sporsmal.svg"), "w", encoding="utf-8").write(build().svg())
    print("ok")
