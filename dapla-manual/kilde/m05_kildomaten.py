from lib import *

def m05():
    f = Fig("m05-kildomaten", 800)
    # Bane: data
    f.rect(30, 16, 940, 270, C["white"], C["line"], 1.2, 10)
    f.text(46, 44, "Data", 18, 700, C["green"])
    f.text(46 + tw("Data", 18, 700) + 10, 44, "skjer automatisk for hver ny fil", 16, 400, C["grey"])

    f.chip(46, 140, "Ny fil kommer inn", "white")
    f.flow([(46 + tw("Ny fil kommer inn", 16, 600) + 18, 156), (214, 156)])
    f.bucket(214, 92, 180, 128, "kilde", "ssb-‹team›-data- kilde-prod/altinn/", "datas")
    f.marker(394, 92, 1)
    f.flow([(394, 156), (444, 156)])
    h = f.box(444, 88, 250, None, "plat", "Kildomaten, kilden «altinn»",
              "Trigges av nye filer i stien som er satt i config.yaml. Kjører process_source_data.py på én og én fil")
    f.marker(694, 88, 2)
    f.flow([(694, 156), (744, 156)])
    f.bucket(744, 92, 210, 128, "produkt", "inndata, med et unikt filnavn per fil", "data")
    f.marker(954, 92, 3)
    f.text(46, 262, "Anbefalt i skriptet: dataminimering og pseudonymisering", 16, 400, C["grey"])

    # Bane: oppsett og kontroll
    y0 = 306
    f.rect(30, y0, 940, 250, C["white"], C["line"], 1.2, 10)
    f.text(46, y0 + 28, "Oppsett og endringer", 18, 700, C["dark"])
    f.text(46 + tw("Oppsett og endringer", 18, 700) + 10, y0 + 28, "i teamets IaC-repo", 16, 400, C["grey"])

    # Mappestruktur
    fx, fy = 46, y0 + 50
    f.rect(fx, fy, 330, 140, C["plat"], C["plat2"], 1.4, 8)
    lines = ["automation/source-data/", "  ‹team›-prod/", "    altinn/", "      config.yaml", "      process_source_data.py"]
    f.text(fx + 14, fy + 28, lines, 16, 400, C["ink"], family=MONO, lh=23)
    f.text(fx, fy + 166, ["Én mappe per kilde, rett under ‹team›-prod.", "Ingen undermapper."], 16, 400,
           C["grey"], lh=20)

    steps = [("Lag gren", "Legg til eller endre filene. Alle på teamet kan gjøre dette"),
             ("Pull request", "Push grenen til GitHub og opprett en PR"),
             ("data-admins godkjenner", "Sjekk at tester og planer er grønne, og merge")]
    bw, gap, sx = 168, 18, 404
    hs = max(f.box_h(bw, t, b) for t, b in steps)
    for i, (t, b) in enumerate(steps):
        x = sx + i*(bw + gap)
        f.box(x, fy, bw, hs, "role" if i == 2 else "white", t, b)
        if i < 2: f.step([(x + bw, fy + hs/2), (x + bw + gap, fy + hs/2)], hs=8)
    f.marker(sx + 2*(bw + gap) + bw - 2, fy, 4)
    # Utrulling styrer Kildomaten
    ux = sx + 2*(bw + gap) + bw/2
    kx = 569
    f.ctrl([(ux, fy), (ux, 296), (kx, 296), (kx, 88 + h)])
    f.label_on(kx + 60, 300, "rulles ut", 16)

    # Merknad
    f.para(sx, fy + hs + 34, "En endring i Python-skriptet krever ikke at tjenesten rulles ut på nytt. En endring i "
           "config.yaml gjør det.", 940 - sx + 20, 16, 400, C["grey"])

    f.h = int(y0 + 250 + 18 + 92)
    f.frame(["data", "plat", "role", "flow", "ctrl", "step", "marker"], "Kildomaten · Features")
    return f

if __name__ == "__main__":
    print(m05().save("out"))
