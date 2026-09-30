"""Mal for de to første bildene i presentasjonssekvensen: Spørsmål og Konsept.
Oversikten og fokusvariantene lages som før (se ny_figur.py).

Sonene i JSON-filen skal ha samme koordinater som sonene i oversikten. Da står
spørsmålene der svarene kommer, og PowerPoint Morph kan animere overgangen.

Kjør:  python figurer/_mal/sekvens.py figurer/_mal/sekvens.json"""
import json, os, sys
from konseptfigurer.fig import Fig, C
from konseptfigurer.sekvens import topp, sone, sporsmal, plassholderpanel, svarpanel, grunnbegreper
from konseptfigurer.sti import utdata


def sporsmalsfoil(s):
    f = Fig(None)
    n = len(s["sporsmal"])
    tall = ["Ett", "To", "Tre", "Fire", "Fem"][n - 1] if n <= 5 else str(n)
    topp(f, s["hovedsporsmal"], f"{tall} spørsmål som de neste bildene svarer på", "Spørsmål")
    for z in s["soner"]:
        sone(f, z["x"], z["y"], z["w"], z["h"])
    for i, q in enumerate(s["sporsmal"]):
        sporsmal(f, i + 1, q["x"] + 32, q["y"], q["linjer"])
    plassholderpanel(f, n)
    grunnbegreper(f, s["grunnbegreper"], f'{s["dato"]} · {s["status"]}')
    return f


def konseptfoil(s):
    k = s["konsept"]
    f = Fig(None)
    topp(f, k["tittel"], k["undertittel"], "Konsept")
    for e in k["elementer"]:
        t = e["type"]
        if t == "data":
            f.cyl("_", e["x"], e["y"], e["w"], e["h"], C["greenl"], C["green"])
            f.text("_", e["x"] + e["w"] / 2, e["y"] + e["h"] / 2 + 12, e["tekst"], 22, C["ink"], 700, "middle")
        elif t in ("flate", "team"):
            fi, st, tc = (C["tealp"], C["dark"], C["ink"]) if t == "flate" else (C["purplep"], C["purple"], "#4b2fb0")
            f.rect("_", e["x"], e["y"], e["w"], e["h"], fi, st, 2.5, 12)
            f.text("_", e["x"] + e["w"] / 2, e["y"] + e["h"] / 2 + 8, e["tekst"], 22, tc, 700, "middle")
        elif t == "person":
            f.person("_", e["x"], e["y"], 1.4)
            f.text("_", e["x"], e["y"] + 84, e["tekst"], 22, C["ink"], 700, "middle")
        elif t == "pil":
            p = [tuple(q) for q in e["punkter"]]
            f.arrow("_", p, C[e.get("farge", "dark")], 4, dash="12 8" if e.get("stiplet") else None, hs=14)
            if e.get("tekst"):
                f.text("_", (p[0][0] + p[-1][0]) / 2, p[0][1] - 16, e["tekst"], 18, C["dark"], 700, "middle")
        elif t == "tekst":
            f.lines("_", e["x"], e["y"], e["linjer"], e.get("storrelse", 20), C["dark"], 700)
        elif t == "merke":
            f.badge(e["x"], e["y"], e["n"])
    svarpanel(f, [tuple(x) for x in k["svar"]], regel=k.get("regel"))
    grunnbegreper(f, s["grunnbegreper"], f'{s["dato"]} · {s["status"]}')
    return f


def main(sti):
    s = json.load(open(sti, encoding="utf-8"))
    ut = utdata(s["serie"])
    open(os.path.join(ut, s["fil"] + "-00-sporsmal.svg"), "w", encoding="utf-8").write(sporsmalsfoil(s).svg())
    open(os.path.join(ut, s["fil"] + "-01-konsept.svg"), "w", encoding="utf-8").write(konseptfoil(s).svg())
    print("ok", s["fil"])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "sekvens.json"))
