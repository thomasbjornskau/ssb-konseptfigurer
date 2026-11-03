from lib import *

def m09():
    f = Fig("m09-metadata-pa-dapla", 800)
    X, W = [30, 360, 690], 280
    sys = [("Datadoc", "Datasett og variabelforekomster",
            "Ansvar: teamet som eier datasettet. Obligatorisk for klargjorte data, statistikk og utdata"),
           ("Vardef", "Variabeldefinisjoner",
            "Ansvar: ansvarlig Dapla-team. Dokumenteres ett sted og gjenbrukes av alle"),
           ("Klass", "Kodeverk: klassifikasjoner og kodelister",
            "Ansvar: eierseksjonen. Brukes fra Dapla. Ikke besluttet om den skal flyttes")]
    hs = max(f.box_h(W, a + "\n" + b, c) for a, b, c in sys)
    for i, (t, d, o) in enumerate(sys):
        x = X[i]
        f.rect(x, 20, W, hs, C["plat"], C["plat2"], 1.5, 8)
        f.text(x + 12, 46, t, 20, 700)
        f.para(x + 12, 72, d, W - 24, 17, 600, C["green"])
        f.para(x + 12, 72 + 26*len(wrap(d, W - 24, 17, 600)) + 4, o, W - 24, 16, 400, C["grey"])
        f.marker(x + W - 4, 20, i + 1)
    # refererer til
    yr = 20 + hs/2
    f.ctrl([(X[0] + W, yr), (X[1], yr)])
    f.ctrl([(X[1] + W, yr), (X[2], yr)])
    f.ctrl([(X[0] + W/2, 20 + hs), (X[0] + W/2, 20 + hs + 22), (X[2] + W/2, 20 + hs + 22), (X[2] + W/2, 20 + hs)])
    f.label_on(X[1] + W/2, 20 + hs + 28, "Datadoc kan også referere direkte til Klass", 16)

    # Eksempel
    y = 20 + hs + 70
    f.text(30, y, "Eksempel: sivilstand", 18, 700)
    y += 16
    # Datadoc: datasett med kolonner
    f.rect(X[0], y, W, 184, C["white"], C["line"], 1.4, 8)
    f.text(X[0] + 12, y + 28, "Et datasett", 17, 700)
    cols = ["fnr", "alder", "sivst", "inntekt"]
    cx = X[0] + 12
    for c in cols:
        w = f.chip(cx, y + 44, c, "data" if c == "sivst" else "white")
        if c == "sivst": sx, sw = cx, w
        cx += w + 6
    f.para(X[0] + 12, y + 110, "Beskrivelse, eier, datatilstand og personopplysninger for datasettet. "
           "For hver kolonne: lenke til Vardef", W - 24, 16, 400, C["grey"])
    # Vardef
    f.rect(X[1], y, W, 184, C["white"], C["line"], 1.4, 8)
    f.text(X[1] + 12, y + 28, "Sivilstand", 17, 700)
    f.para(X[1] + 12, y + 56, "«Variabelen viser en persons stilling ihht ekteskapslovgivningen»", W - 24, 16, 400,
           C["ink"])
    f.para(X[1] + 12, y + 130, "Datadoc kan presisere definisjonen for det enkelte datasettet", W - 24, 16, 400,
           C["grey"])
    # Klass
    f.rect(X[2], y, W, 184, C["white"], C["line"], 1.4, 8)
    f.text(X[2] + 12, y + 28, "Standard for sivilstand", 17, 700)
    f.para(X[2] + 12, y + 56, "Kategoriene og kodene variabelen kan ha", W - 24, 16, 400, C["ink"])
    f.para(X[2] + 12, y + 130, "Kan hentes via API eller lastes ned som csv", W - 24, 16, 400, C["grey"])
    f.ctrl([(X[0] + W, y + 60), (X[1], y + 60)])
    f.label_on((X[0] + W + X[1]) / 2, y + 90, "sivst", 16)
    f.ctrl([(X[1] + W, y + 60), (X[2], y + 60)])

    # Planlagt og utfaset
    y2 = y + 214
    hb = f.box_h(W, "Vardok og Datadok", "Kan ikke brukes på Dapla. Relevante variabler fra Vardok flyttes til Vardef")
    f.box(X[0], y2, W*2 + 50, hb, "out", "Datakatalog · planlagt",
          "En portal for å søke i alle metadataene. Skal implementeres etter hvert", dash="6 4")
    f.box(X[2], y2, W, hb, "out", "Vardok og Datadok",
          "Kan ikke brukes på Dapla. Relevante variabler fra Vardok flyttes til Vardef")
    f.h = int(y2 + hb + 30 + 92)
    f.frame(["plat", "data", ("out", "Utfaset eller utenfor Dapla"), ("ctrl", "Refererer til"), "plan", "marker"],
            "Metadata · Datadoc · Vardef · Klass")
    return f

if __name__ == "__main__":
    print(m09().save("out"))
