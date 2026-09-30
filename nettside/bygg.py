"""Bygger nettsider med stegvis visning av presentasjonssekvenser
(Spørsmål → Konsept → Oversikt → Fokus) til nettside/site/.

Hvert steg tegnes med de samme Python-skriptene som lager SVG-ene. Siden sammenligner
elementene fra steg til steg: det som er likt, blir stående; det som bare skifter farge
(for eksempel nedtoning i fokus), glir over; det som er nytt, tones inn; resten tones ut.
Det virker fordi alle stegene deler samme geometri.

Kjør:  make nettside   (eller: PYTHONPATH=. python3 nettside/bygg.py)
"""
import html, importlib, json, os, sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UT = os.path.join(ROT, "nettside", "site")
FARGER = ("fill", "stroke")


def modul(serie, navn):
    sti = os.path.join(ROT, "figurer", serie)
    if sti not in sys.path:
        sys.path.insert(0, sti)
    return importlib.import_module(navn)


# ---------- sekvenser ----------
def dapla_orientering_tilgang():
    sp = modul("dapla", "orientering_tilgang_sporsmal")
    ka = modul("dapla", "orientering_tilgang_konsept")
    kb = modul("dapla", "orientering_tilgang_konsept_b")
    ov = modul("dapla", "orientering_tilgang")
    V = ov.V
    kort_fokus = ["Tilgang", "Eierskap", "Deling", "Selvbetjening"]
    steg = [
        dict(type="Spørsmål", kort="Spørsmål", tekst="Fire spørsmål. Svarene kommer på det stedet der spørsmålet står.",
             fig=sp.build()),
        dict(type="Konsept", kort="Konsept", tekst="Det enkle bildet: tilgang følger teamet, ikke personen.",
             varianter={"A": ka.build(), "B": kb.build()}),
        dict(type="Oversikt", kort="Oversikt", tekst="Hele bildet: roller, prosjekter, bøtter og felles plattform.",
             fig=ov.tegn(V[0])),
    ]
    for i, v in enumerate(V[1:]):
        steg.append(dict(type=f"Fokus {i + 1}", kort=kort_fokus[i], tekst=v["title"] + ".", fig=ov.tegn(v)))
    return dict(
        fil="dapla/orientering-tilgang/index.html",
        serie="Dapla", celle="Orientering × Ansvar og tilgang",
        tittel="Hvem får se hvilke data på Dapla?",
        beskrivelse="For ledere, eksterne og samarbeidspartnere. Fra spørsmål via det enkle bildet til hele oversikten og fire fokus.",
        konsept_varianter={"A": "nedskalert oversikt", "B": "innenfor/utenfor"},
        status="Utkast til diskusjon, ikke kvalitetssikret",
        steg=steg)


SEKVENSER = [dapla_orientering_tilgang]


# ---------- SVG → elementliste ----------
def elementer(fig):
    """Gjør en Fig om til en liste av {k: nøkkel, t: tagg, a: attributter, c: farger, i: innhold}.
    Nøkkelen er alt unntatt farger, så samme form med ny farge regnes som samme element."""
    rot = ET.fromstring(fig.svg().replace('xmlns="http://www.w3.org/2000/svg" ', ""))
    ut, sett = [], {}
    for el in rot:
        attr = {k: v for k, v in el.attrib.items() if k not in FARGER}
        farge = {k: v for k, v in el.attrib.items() if k in FARGER}
        inn = escape(el.text or "") + "".join(ET.tostring(b, encoding="unicode") for b in el)
        nokkel = el.tag + "|" + json.dumps(attr, sort_keys=True, ensure_ascii=False) + "|" + inn
        n = sett.get(nokkel, 0)
        sett[nokkel] = n + 1
        ut.append(dict(k=f"{nokkel}#{n}", t=el.tag, a=attr, c=farge, i=inn))
    return ut


def bygg_sekvens(s):
    data = dict(tittel=s["tittel"], celle=s["celle"], serie=s["serie"],
                konsept_varianter=s.get("konsept_varianter"), steg=[])
    for st in s["steg"]:
        d = dict(type=st["type"], kort=st["kort"], tekst=st["tekst"])
        if "varianter" in st:
            d["varianter"] = {n: elementer(f) for n, f in st["varianter"].items()}
        else:
            d["el"] = elementer(st["fig"])
        data["steg"].append(d)
    mal = open(os.path.join(ROT, "nettside", "mal.html"), encoding="utf-8").read()
    side = (mal.replace("{{TITTEL}}", html.escape(s["tittel"]))
               .replace("{{SERIE}}", html.escape(s["serie"]))
               .replace("{{CELLE}}", html.escape(s["celle"]))
               .replace("{{STATUS}}", html.escape(s["status"]))
               .replace("{{DATA}}", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    sti = os.path.join(UT, s["fil"])
    os.makedirs(os.path.dirname(sti), exist_ok=True)
    open(sti, "w", encoding="utf-8").write(side)
    return sti


def bygg_forside(sekvenser):
    kort = "\n".join(
        f'<a class="kort" href="{html.escape(s["fil"].replace("index.html", ""))}">'
        f'<span class="serie">{html.escape(s["serie"])} · {html.escape(s["celle"])}</span>'
        f'<strong>{html.escape(s["tittel"])}</strong>'
        f'<span>{html.escape(s["beskrivelse"])}</span>'
        f'<span class="steg">{len(s["steg"])} steg</span></a>' for s in sekvenser)
    mal = open(os.path.join(ROT, "nettside", "forside.html"), encoding="utf-8").read()
    open(os.path.join(UT, "index.html"), "w", encoding="utf-8").write(mal.replace("{{KORT}}", kort))


def main():
    sekvenser = [f() for f in SEKVENSER]
    for s in sekvenser:
        print("ok", bygg_sekvens(s))
    bygg_forside(sekvenser)
    open(os.path.join(UT, ".nojekyll"), "w").close()
    print("ok", os.path.join(UT, "index.html"))


if __name__ == "__main__":
    main()
