from lib import *

def m03():
    f = Fig("m03-datatilstander-og-botter", 860)
    LX, CX0, CW, G = 30, 166, 148, 13
    cx = [CX0 + i*(CW + G) for i in range(5)]
    names = ["Kildedata", "Inndata", "Klargjorte data", "Statistikk", "Utdata"]
    optional = [False, True, False, True, False]

    def rowlabel(y, s):
        f.text(LX, y, wrap(s, 120, 16, 700), 16, 700, C["grey"], lh=20)

    # R0: tilstandene
    y0 = 20
    h0 = max(f.box_h(CW, n, None, pad=10) for n in names)
    for i, n in enumerate(names):
        f.box(cx[i], y0, CW, h0, "datas" if i == 0 else "data", n, None, center=True,
              dash="6 4" if optional[i] else None, pad=10, minh=58)
        if optional[i]:
            f.text(cx[i] + CW/2, y0 + h0 + 20, "ikke obligatorisk", 16, 400, C["grey"], "middle")
        if i < 4:
            f.flow([(cx[i] + CW, y0 + h0/2), (cx[i+1], y0 + h0/2)], hs=9, sw=2.2)
    f.marker(cx[1] + CW - 2, y0, 1)

    # R1: hva det er
    y1 = y0 + h0 + 34
    rowlabel(y1 + 18, "Hva det er")
    what = ["Slik dataene ble levert fra dataeier",
            "Kildedata i SSBs standard lagringsformat",
            "Beregnet, koblet og editert. Oftest enkelt\u00adobservasjoner",
            "Ofte aggregert eller estimert. Kan være konfidensiell",
            "Statistikk der konfidensialiteten er ivaretatt. Det som publiseres"]
    h1 = max(f.box_h(CW, None, s, pad=10) for s in what)
    for i, s in enumerate(what):
        f.box(cx[i], y1, CW, h1, "white", None, s, pad=10)

    # R2: lagres i
    y2 = y1 + h1 + 22
    rowlabel(y2 + 40, "Lagres i")
    f.bucket(cx[0], y2, CW, 96, "kilde", "ssb-‹team›-data- kilde-prod", "datas", ssize=16)
    w4 = 4*CW + 3*G
    f.bucket(cx[1], y2, w4, 96, "produkt", "ssb-‹team›-data-produkt-prod, i mapper per statistikkprodukt og datatilstand", "data")
    f.marker(cx[1] + w4 - 4, y2 + 4, 2)

    # R3: hvem har tilgang
    y3 = y2 + 118
    rowlabel(y3 + 26, "Hvem har tilgang")
    f.box(cx[0], y3, CW, 44, "role", None, "data-admins, med JIT", pad=10, bfill=C["liltxt"])
    f.box(cx[1], y3, w4, 44, "role", None, "developers, fast tilgang (data-admins er normalt også developers)",
          pad=10, bfill=C["liltxt"])
    f.marker(cx[0] + CW - 2, y3, 3)

    # R4: hva flytter dataene
    y4 = y3 + 70
    rowlabel(y4 + 26, "Hva flytter dataene")
    # Kildomaten: kilde -> inndata
    f.box(cx[0] + CW/2, y4, CW + G, 74, "plat", "Kildomaten", "dataminimering og pseudonymisering", pad=8,
          tsize=16, bsize=16)
    f.box(cx[1] + CW/2 + G + 18, y4, w4 - CW/2 - G - 18, 74, "plat", "Teamets egen kode",
          "for eksempel i Dapla Lab, med koden lagret på GitHub", pad=8, tsize=16, bsize=16)
    f.marker(cx[0] + CW*1.5 + G - 2, y4, 4)

    # R5: metadata
    y5 = y4 + 104
    rowlabel(y5 + 18, "Metadata som forventes")
    meta = ["Dataeier, område og tid. Om variabler: bare det dataeier leverer",
            "Som for kildedata",
            "Variabel\u00addefinisjoner og tiltak som har forbedret nøyaktigheten",
            "Variabel\u00addefinisjoner, og metoder og kode som er brukt",
            "Som for statistikk"]
    h5 = max(f.box_h(CW, None, s, pad=10) for s in meta)
    for i, s in enumerate(meta):
        f.box(cx[i], y5, CW, h5, "white", None, s, pad=10)
    # Datadoc obligatorisk over klargjorte, statistikk, utdata
    yb = y5 + h5 + 14
    xa, xb = cx[2], cx[4] + CW
    f.path(f"M{xa},{yb} L{xa},{yb+8} L{xb},{yb+8} L{xb},{yb}", "none", C["green"], 2)
    f.text((xa + xb)/2, yb + 32, "Dokumenteres i Datadoc (obligatorisk)", 16, 700, C["green"], "middle")
    f.marker(xb + 2, yb + 26, 5)

    f.h = int(yb + 50 + 92)
    f.frame(["data", "plat", "role", "flow", ("dash", "Ikke obligatorisk"), "marker"],
            "Datatilstander · Hva er bøtter? · Kildomaten · Datadoc")
    return f

if __name__ == "__main__":
    print(m03().save("out"))
