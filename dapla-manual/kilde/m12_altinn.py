from lib import *

def stacked(f, x, y, w, h, title, body, kind="plat", n=2):
    fill, stroke, _ = KIND[kind]
    for k in range(n, 0, -1):
        f.rect(x + 6*k, y - 6*k, w, h, fill, stroke, 1.3, 8)
    f.box(x, y, w, h, kind, title, body, pad=10)

def m12():
    f = Fig("m12-altinn3-fra-skjema-til-botte", 800)
    # Del A: utsending
    f.text(30, 30, "Utsending", 18, 700)
    f.text(30 + tw("Utsending", 18, 700) + 10, 30, "administreres av teamet som eier skjemaet", 16, 400, C["grey"])
    lv = [("Skjema", "en skjemaversjon i skjemakatalogen", 1),
          ("Periode", "et skjema kan ha flere", 2),
          ("Pulje", "en periode kan ha flere", 2),
          ("Utsending", "en pulje kan ha flere", 2)]
    bw, gap, y = 190, 52, 62
    for i, (t, b, n) in enumerate(lv):
        x = 30 + i*(bw + gap)
        if n > 1: stacked(f, x, y + 12, bw, 82, t, b)
        else: f.box(x, y + 12, bw, 82, "plat", t, b, pad=10)
        if i < 3: f.step([(x + bw, y + 53), (x + bw + gap - 4, y + 53)], hs=9)
    f.marker(30 + bw - 4, y + 12, 1)
    # utsendingstyper
    ty = y + 142
    f.text(30, ty, "Utsendingstyper:", 16, 700, C["grey"])
    cx = 30 + tw("Utsendingstyper:", 16, 700) + 10
    row = 0
    for s in ["Instansiering", "Informasjon om skjema", "Vedtak opplysningsplikt", "Hovedutsending brev",
              "Påminnelse", "Vedtak tvangsmulkt"]:
        w = tw(s, 16, 600) + 18
        if cx + w > 970:
            cx = 30 + tw("Utsendingstyper:", 16, 700) + 10; row += 1
        f.chip(cx, ty - 19 + row*36, s, "white")
        cx += w + 8
    f.para(30, ty + 36*(row + 1) + 10, "Verktøy: SU-Vs grafiske grensesnitt eller Python-pakken dapla-suv-tools. "
           "Krever developers eller data-admins i teamet som eier skjemaet", 940, 16, 400, C["grey"])

    # Del B: innsending og data
    y0 = ty + 36*(row + 1) + 64
    f.line(30, y0 - 22, 970, y0 - 22, C["line"], 1)
    f.text(30, y0 + 8, "Innsending og data", 18, 700)
    X = [30, 214, 452, 652, 830]
    W = [164, 218, 180, 158, 140]
    yb = y0 + 30
    f.box(X[0], yb, W[0], 120, "out", "Oppgavegiver", "fyller ut og sender inn i Altinn 3", pad=10)
    f.box(X[1], yb, W[1], 120, "role", "Team SU-V", "henter inn og lagrer hvert skjema som xml, med en json-fil "
          "med metadata, i egne delt-bøtter", pad=10)
    f.box(X[2], yb, W[2], 120, "plat", "Transfer Service", "I prod får bare teamets Transfer Service tilgang, aldri "
          "personer", pad=10, bsize=16)
    f.bucket(X[3], yb + 4, W[3], 112, "kilde", "én mappe per skjema", "datas")
    f.box(X[4], yb, W[4], 120, "plat", "Kildomaten", "for eksempel fra xml til et annet format", pad=10)
    for i in range(4):
        f.flow([(X[i] + W[i], yb + 60), (X[i+1], yb + 60)], hs=9)
    f.marker(X[1] + W[1] - 4, yb, 2)
    f.marker(X[2] + W[2] - 4, yb, 3)
    f.marker(X[3] + W[3] - 4, yb + 4, 4)
    # Ansvar
    ya = yb + 140
    f.path(f"M{X[0]},{ya} L{X[0]},{ya+8} L{X[1]+W[1]},{ya+8} L{X[1]+W[1]},{ya}", "none", C["lil"], 2)
    f.text(X[0], ya + 32, "SU-V har ansvaret for datafangsten", 16, 700, C["liltxt"])
    f.path(f"M{X[2]},{ya} L{X[2]},{ya+8} L{X[4]+W[4]},{ya+8} L{X[4]+W[4]},{ya}", "none", C["lil"], 2)
    f.text(X[2], ya + 32, "Statistikkteamet har ansvaret for sine kildedata", 16, 700, C["liltxt"])

    yn = ya + 76
    f.rect(30, yn - 22, 940, 58, C["out2"], "none", rx=8)
    f.para(46, yn, "Bli kjent med skjemadataene i testmiljøet først. Der er dataene fiktive og tilgangen mindre "
           "restriktiv. Tilgang i test og prod søkes om hver for seg.", 908, 16, 400, C["ink"])
    f.h = int(yn + 50 + 92)
    f.frame(["out", "role", "plat", "data", "flow", "step", "marker"],
            "Altinn 3: Oversikt · Administrasjon av skjema · Utsending")
    return f

if __name__ == "__main__":
    print(m12().save("out"))
