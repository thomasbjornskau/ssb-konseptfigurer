from lib import *

def m10():
    f = Fig("m10-en-tjeneste-i-dapla-lab", 800)
    top = 20
    # 1 Tjenestekatalog
    h1 = f.box(30, top, 190, None, "plat", "Tjenestekatalog",
               "Velg tjeneste, for eksempel Jupyter, VS Code, RStudio eller Datadoc-editor")
    f.marker(216, top, 1)
    # 2 Konfigurasjon
    h2 = f.box(246, top, 220, None, "plat", "Tjenestekonfigurasjon",
               "Velg team og tilgangsgruppe, ressurser (CPU, RAM, GPU, disk), Git og GitHub, og versjon")
    f.marker(462, top, 2)
    f.para(246, top + h2 + 26, "Kan lagres, men bare i nettleseren din. Kan deles med andre som har samme "
           "tilganger", 220, 16, 400, C["grey"])
    f.step([(220, top + 50), (246, top + 50)], hs=8)
    f.step([(466, top + 50), (496, top + 50)], hs=8)

    # 3 Kjørende tjeneste
    sx, sw, sh = 496, 290, 320
    f.rect(sx, top, sw, sh, C["white"], C["plat2"], 2, 10)
    f.text(sx + 14, top + 28, "Kjørende tjeneste", 18, 700)
    f.text(sx + 14, top + 50, "under Mine tjenester", 16, 400, C["grey"])
    f.marker(sx + sw - 4, top, 3)
    f.box(sx + 14, top + 66, sw - 28, None, "data", "/buckets/",
          "Teamets bøtter som mapper, for eksempel /buckets/produkt/")
    f.box(sx + 14, top + 166, sw - 28, None, "plat", "$HOME/work",
          "Kode du jobber med nå. Bevares når tjenesten pauses")
    f.text(sx + 14, top + 278, ["Resten av filsystemet slettes", "når tjenesten pauses"], 16, 400, C["grey"], lh=20)

    # 4 Pause og avslutt
    px = 812
    hp = f.box(px, top, 158, None, "white", "Pause",
               "$HOME/work bevares. Skjer automatisk hver hele time kl. 17–05")
    f.marker(px + 154, top, 4)
    ha = f.box(px, top + hp + 16, 158, None, "white", "Avslutt", "Alt i tjenesten slettes")
    f.step([(sx + sw, top + 60), (px, top + 60)], hs=8)
    f.step([(sx + sw, top + hp + 16 + 40), (px, top + hp + 16 + 40)], hs=8)
    f.para(px, top + hp + ha + 52, "Unntak fra automatisk pause: legg til [nosuspend] i navnet", 158, 16, 400,
           C["grey"])

    # Bøtter under tjenesten
    by = 392
    f.text(sx, by - 8, "Teamets bøtter", 16, 700, C["grey"])
    f.bucket(sx, by + 4, 90, 76, "produkt", None, "data", lsize=16)
    f.bucket(sx + 100, by + 4, 90, 76, "delt", None, "data", lsize=16)
    f.bucket(sx + 200, by + 4, 90, 76, "kilde", None, "datas", lsize=16, dash="5 4")
    f.flow([(sx + 140, by + 4), (sx + 140, top + sh)], start=True, end=True, hs=9)
    f.para(sx + 200, by + 104, "kilde bare som data-admins, med begrunnelse og maks 8 timer", 200, 16, 400, C["grey"])
    f.para(sx, by + 104, "delt-bøtter fra andre team velges i konfigurasjonen", 186, 16, 400, C["grey"])

    # GitHub
    gy = 420
    f.box(246, gy, 220, None, "plat", "GitHub", "Her lagres koden permanent, ikke i tjenesten")
    f.arrow([(sx + 14, top + 208), (481, top + 208), (481, gy + 40), (466, gy + 40)], C["dark"], 1.8,
            start=True, hs=9)
    f.label_on(356, gy - 14, "push og pull", 16)

    # Miljø
    ey = 580
    f.rect(30, ey, 940, 58, C["out2"], "none", rx=8)
    f.para(46, ey + 24, "Prodbøttene nås fra Dapla Lab i prod (lab.dapla.ssb.no). Teamets testbøtter nås fra "
           "testmiljøet til Dapla Lab. Pause eller avslutt tjenester du ikke bruker: de reserverer ressurser "
           "SSB betaler for.", 908, 16, 400, C["ink"])
    f.h = ey + 58 + 30 + 92
    f.frame(["plat", "data", "flow", ("ctrl", "Kode lagres og hentes"), "step", ("dash", "Valgfritt"), "marker"],
            "Dapla Lab · Hva er bøtter? · Jupyter")
    return f

if __name__ == "__main__":
    print(m10().save("out"))
