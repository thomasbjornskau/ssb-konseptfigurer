"""Teknisk × Kapabilitet: realiseringskart.
Rader = de ni kapabilitetene (samme rekkefølge som kapabilitetskartet).
Kolonner = sonene fra Teknisk × Struktur. Celler = komponenter som realiserer kapabiliteten.
Varianter: oversikt (nøytral), linse 1 modenhet, linse 2 hull og overlapp."""
import os
from collections import Counter
from konseptfigurer.fig import Fig, C
from konseptfigurer.sti import utdata

DATO = "28.09.2026"

PT = "#4b2fb0"
U = "5 4"
ZONES = [("Arbeidsflate", "Dapla Lab"), ("Per team", "prosjekter og bøtter"), ("Felles tjenester", "driftes én gang"),
         ("Grunnmur", "Google Cloud"), ("Utenfor GCP", "GitHub, on-prem, eksterne")]
# status: d = i drift, w = under arbeid, p = forslag, u = ukjent/ubekreftet
LAYERS = [
    ("Kjerne", [
        ("Hente inn data", [[], [("Kildebøtte", "d"), ("Kildomaten", "d")],
                            [("Transfer Service", "d"), ("SUV-API", "d"), ("Kudoc", "d")], [("GCS", "d")],
                            [("Altinn 3", "d"), ("On-prem (ORDS)", "d")]]),
        ("Bearbeide og produsere", [[("Dapla Lab", "d"), ("Jupyter-pyspark", "d")], [("Produktbøtte", "d")],
                                    [("ssb-fagfunksjoner", "d"), ("Metodebiblioteket", "d")], [("Kubernetes", "d")],
                                    [("PyPI / CRAN", "d")]]),
        ("Dele og formidle", [[], [("Delt-bøtte", "d")], [("Delomaten", "d"), ("statbank-client", "d")], [],
                              [("Statistikkbanken", "u"), ("Microdata.no", "u")]]),
    ]),
    ("Styring", [
        ("Beskrive og finne data", [[("Datadoc-editor", "d")], [], [("Vardef", "d"), ("Datadoc-API", "u"), ("Klass", "d"), ("Dataportal", "d")],
                                    [("Databaser", "u")], []]),
        ("Automatisere og overvåke", [[], [("Kildomaten", "d"), ("Container-jobber", "p")], [("Orkestrator", "p"), ("Pub/Sub", "u")],
                                      [("Cloud Run Jobs", "p"), ("Cloud Logging", "u")], []]),
        ("Dokumentere kvalitet", [[], [("Prosessdata", "w")], [("Kvalitetsindikatorer", "w"), ("StatDoc", "u")], [],
                                  [("GitHub", "d")]]),
    ]),
    ("Fundament", [
        ("Beskytte og styre tilgang", [[("Teamvalg", "d")], [("Teamgrupper", "d"), ("JIT", "d")],
                                       [("toolbelt-pseudo", "d"), ("Dapla Ctrl", "d"), ("Nøkler", "u")],
                                       [("IAM", "d"), ("Secret Manager", "u")], [("Identitetsløsning", "u")]]),
        ("Lagre og beregne i skala", [[("Onyxia", "d"), ("/buckets", "d")], [("Teamets bøtter", "d")], [],
                                      [("GCS", "d"), ("Kubernetes", "d"), ("NAIS", "u")], []]),
        ("Utvikle og dele kode", [[], [("Team-repo (IaC)", "d")], [("ssb-project", "d"), ("Atlantis", "d"), ("Artifact Registry", "p")],
                                  [], [("GitHub", "d"), ("GitHub Actions", "d"), ("PyPI / CRAN", "d")]]),
    ]),
]

LX, LW = 60, 96          # lagkolonne
KX, KW = 164, 196        # kapabilitetskolonne
ZX, ZW, ZG = 368, 202, 6  # sonekolonner
Y0, RH, RG, LG = 262, 74, 4, 12


def chip_w(t):
    return len(t) * 7.1 + 20


def style(kind, lens):
    """returnerer fyll, strek, tekstfarge, stiplet"""
    if lens != "maturity":
        return C["white"], C["dark"], C["dark"], None
    return {"d": (C["green"], C["green"], C["white"], None),
            "w": (C["greenp"], C["green"], C["green"], U),
            "p": (C["white"], C["purple"], PT, "5 3"),
            "u": (C["white"], C["grey"], C["grey"], U)}[kind]


def build(lens):
    f = Fig(None)
    f.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{C["white"]}"/>')
    titles = {None: ("Hva realiserer kapabilitetene?", "Teknisk kapabilitet · fra kapabilitet til komponent, fordelt på soner", "Oversikt"),
              "maturity": ("Hvor modne er kapabilitetene?", "Linse 1 · status for hver komponent", "Linse 1 av 2"),
              "gaps": ("Hvor er hullene og overlappene?", "Linse 2 · kapabiliteter med lite i drift, og komponenter som går igjen", "Linse 2 av 2")}
    t, s, tag = titles[lens]
    f.text("_", 60, 92, t, 46, C["ink"], 700)
    f.text("_", 60, 136, s, 24, C["grey"])
    f.rect("_", 1520, 62, 150, 40, C["ink"], C["ink"], 0, 20)
    f.text("_", 1595, 89, "INTERN", 19, C["white"], 700, "middle")
    f.rect("_", 1690, 62, 170, 40, C["white"], C["dark"], 2, 20)
    f.text("_", 1775, 89, tag, 19, C["dark"], 700, "middle")
    f.add(f'<line x1="60" y1="160" x2="1860" y2="160" stroke="{C["line"]}" stroke-width="2"/>')

    # telling for linse 2
    names = Counter()
    for _, caps in LAYERS:
        for cap, zones in caps:
            seen = set()
            for z in zones:
                for n, k in z:
                    seen.add(n)
            names.update(seen)
    overlap = {n for n, c in names.items() if c > 1}

    # kolonneoverskrifter
    f.text("_", KX, 212, "Kapabilitet", 18, C["ink"], 700)
    f.text("_", KX, 236, "samme som i kartet", 14, C["grey"])
    for j, (z, sub) in enumerate(ZONES):
        x = ZX + j * (ZW + ZG)
        f.rect("_", x, 180, ZW, 70, C["dark"], C["dark"], 0, 10)
        f.text("_", x + 14, 210, z, 18, C["white"], 700)
        f.text("_", x + 14, 234, sub, 13, "#d6e6e5")

    y = Y0
    stats = Counter()
    uniq = {}
    gaps_rows = []
    for li, (lname, caps) in enumerate(LAYERS):
        ly0 = y
        for cap, zones in caps:
            allk = [k for z in zones for _, k in z]
            share = sum(1 for k in allk if k == "d") / max(1, len(allk))
            weak = share < 0.5
            if weak:
                gaps_rows.append((cap, share, len(allk)))
            hl_row = lens == "gaps" and weak
            f.rect("_", KX, y, KW, RH, C["purplep"] if hl_row else C["tealp"], C["purple"] if hl_row else C["tealp"], 2 if hl_row else 0, 8)
            f.lines("_", KX + 12, y + (RH / 2 + 6 if len(cap) < 22 else RH / 2 - 4), [cap] if len(cap) < 22 else cap.rsplit(" ", 1), 15, C["ink"], 700, lh=19)
            for j, z in enumerate(zones):
                x = ZX + j * (ZW + ZG)
                empty = not z
                f.rect("_", x, y, ZW, RH, "#f7f9f9" if empty else C["white"], "#e3e9e9", 1.2, 6)
                cx, cy = x + 8, y + 10
                for n, k in z:
                    uniq[n] = k
                    w = chip_w(n)
                    if cx + w > x + ZW - 6:
                        cx, cy = x + 8, cy + 30
                    fi, st, tc, da = style(k, lens)
                    if lens == "gaps":
                        if n in overlap:
                            fi, st, tc, da = C["purplel"], C["purple"], PT, None
                        else:
                            fi, st, tc, da = C["white"], "#dfe5e5", "#b9c5c6", None
                    f.rect("_", cx, cy, w, 24, fi, st, 1.4, 12, dash=da)
                    f.text("_", cx + w / 2, cy + 17, n, 12.5, tc, 700, "middle")
                    cx += w + 6
            y += RH + RG
        # lagetikett
        f.rect("_", LX, ly0, LW, y - RG - ly0, C["white"], C["dark"], 0, 0)
        f.add(f'<rect x="{LX}" y="{ly0}" width="6" height="{y-RG-ly0}" fill="{C["dark"]}"/>')
        f.text("_", LX + 14, ly0 + 28, lname, 14.5, C["ink"], 700)
        y += LG - RG + 4

    stats = Counter(uniq.values())
    # sidepanel
    f.rect("_", 1440, 180, 420, 804, C["tealp"], C["tealp"], 0, 16)
    tot = sum(stats.values())
    if lens is None:
        head = "Slik leses figuren"
        items = [("Rader: kapabilitetene", ["De samme ni som i kapabilitets-", "kartet, i samme rekkefølge."]),
                 ("Kolonner: sonene", ["De samme som i strukturfiguren,", "fra arbeidsflate til utenfor GCP."]),
                 ("Brikker: komponenter", ["Det som faktisk realiserer", "kapabiliteten i hver sone."]),
                 ("Linser gir svarene", ["Linse 1 viser modenhet. Linse 2", "viser hull og overlapp. Eierskap", "kommer når det er bekreftet."])]
    elif lens == "maturity":
        head = "Modenhet"
        items = [("Status i tall", [f"{stats['d']} av {tot} unike komponenter i drift,", f"{stats['w']} under arbeid, {stats['p']} forslag,", f"{stats['u']} ubekreftet."]),
                 ("Kjerne og fundament", ["Stort sett i drift. Hullene", "her er leveransen ut og", "identitetskjeden."]),
                 ("Styring er svakest", ["Automatisering og kvalitet er", "preget av forslag og arbeid", "som pågår."]),
                 ("Ubekreftet ≠ mangler", ["Grå betyr at vi ikke vet,", "ikke at det ikke finnes."])]
    else:
        head = "Hull og overlapp"
        g = [f"{c}: {round(s*100)} % i drift" for c, s, n in gaps_rows]
        items = [("Hull", ["Kapabiliteter der under halvparten", "av komponentene er i drift:"] + g),
                 ("Overlapp", ["Komponenter som realiserer flere", "kapabiliteter:", ", ".join(sorted(overlap)[:3]) + ",", ", ".join(sorted(overlap)[3:]) + "."]),
                 ("Hvorfor det betyr noe", ["En endring i en komponent som går", "igjen, treffer flere kapabiliteter.", "De bør ha tydelig eierskap."])]
    f.text("_", 1466, 226, head, 25, C["ink"], 700)
    yy = 276
    for i, (h, b) in enumerate(items):
        f.text("_", 1466, yy, h, 20, C["ink"], 700)
        f.lines("_", 1466, yy + 27, b, 17, C["dark"], lh=23)
        yy += 27 + len(b) * 23 + 24

    # bunntekst
    f.add(f'<line x1="60" y1="1010" x2="1860" y2="1010" stroke="{C["line"]}" stroke-width="1"/>')
    yb = 1046
    if lens == "maturity":
        x = 60
        for k, lab in [("d", "I drift"), ("w", "Under arbeid"), ("p", "Forslag"), ("u", "Ubekreftet")]:
            fi, st, tc, da = style(k, "maturity")
            f.rect("_", x, yb - 20, 70, 24, fi, st, 1.4, 12, dash=da)
            f.text("_", x + 82, yb - 2, lab, 16, C["dark"])
            x += 82 + len(lab) * 9 + 40
    elif lens == "gaps":
        f.rect("_", 60, yb - 20, 70, 24, C["purplel"], C["purple"], 1.4, 12)
        f.text("_", 142, yb - 2, "Går igjen i flere kapabiliteter", 16, C["dark"])
        f.rect("_", 420, yb - 22, 70, 28, C["purplep"], C["purple"], 2, 8)
        f.text("_", 502, yb - 2, "Under halvparten i drift", 16, C["dark"])
    else:
        f.rect("_", 60, yb - 20, 70, 24, C["white"], C["dark"], 1.4, 12)
        f.text("_", 142, yb - 2, "Komponent", 16, C["dark"])
        f.rect("_", 280, yb - 22, 70, 28, "#f7f9f9", "#e3e9e9", 1.2, 6)
        f.text("_", 362, yb - 2, "Ingen komponent i sonen", 16, C["dark"])
    f.text("_", 1860, yb, f"Utkast {DATO} · Kilder: manualen, ADR0015, 0017, 0023, 0026, notat om orkestrering", 15, C["grey"], 400, "end")
    return f


if __name__ == "__main__":
    out = utdata("dapla")
    os.makedirs(out, exist_ok=True)
    for lens, fn in [(None, "0-oversikt"), ("maturity", "1-modenhet"), ("gaps", "2-hull-overlapp")]:
        open(os.path.join(out, f"teknisk-kapabilitet-{fn}.svg"), "w", encoding="utf-8").write(build(lens).svg())
    print("ok")
