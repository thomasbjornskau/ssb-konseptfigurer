"""Mal for nye figurer: leser en JSON-fil og tegner oversikt + fokusvarianter.
Kjør:  python figurer/_mal/ny_figur.py figurer/_mal/ny_figur.json"""
import json, os, sys
from konseptfigurer.fig import Fig, C
from konseptfigurer.komponenter import ramme, flate
from konseptfigurer.sti import utdata


def tegn(spek, fokus=None, variant=None):
    f = Fig(set(fokus) if fokus else None)
    v = variant or {}
    ramme(f, v.get("tittel", spek["tittel"]), spek["undertittel"], v.get("etikett", spek["etikett"]),
          spek["panel"], spek["punkter"], spek["tegnforklaring"], spek["dato"], spek.get("status", "Utkast"), spek.get("kilde"))
    for e in spek["elementer"]:
        if e["type"] == "flate":
            flate(f, e["gruppe"], e["x"], e["y"], e["w"], e["h"], e["tittel"], e.get("linjer", []), e.get("brikker", []),
                  e.get("uavklart"), e.get("stiplet", False))
        elif e["type"] == "pil":
            f.arrow(e["gruppe"], [tuple(p) for p in e["punkter"]], C[e.get("farge", "dark")], 3,
                    dash="5 4" if e.get("stiplet") else None, hs=11)
    return f


def main(sti):
    spek = json.load(open(sti, encoding="utf-8"))
    ut = utdata(spek["serie"])
    open(os.path.join(ut, spek["fil"] + "-oversikt.svg"), "w", encoding="utf-8").write(tegn(spek).svg())
    for v in spek.get("varianter", []):
        open(os.path.join(ut, spek["fil"] + "-" + v["fil"] + ".svg"), "w", encoding="utf-8").write(tegn(spek, v["fokus"], v).svg())
    print("ok", spek["fil"])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "ny_figur.json"))
