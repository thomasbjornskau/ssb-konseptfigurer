from lib import *

def m02():
    f = Fig("m02-roller-og-tilgang", 780)
    X = [30, 210, 460, 720]   # kolonner: hvem, rolle, mekanisme, ressurs
    W = [160, 220, 230, 250]
    for x, s in zip(X, ["Hvem", "Rolle eller gruppe", "Slik får de tilgang", "Hva de når"]):
        f.text(x, 30, s, 16, 700, C["grey"])
    f.line(30, 42, 970, 42, C["line"], 1)

    def who(y, lines, n=1, col=None):
        for i in range(n):
            f.person(48 + i*24, y + 22, col or C["ink"])
        f.text(30, y + 62, lines, 16, 400, C["ink"], lh=20)

    # Rad 1: Teamansvarlig
    y = 58
    who(y, ["Seksjonsleder"])
    f.box(X[1], y, W[1], 96, "role", "Teamansvarlig", "Administrativ rolle, ikke en tilgangsgruppe")
    f.box(X[2], y, W[2], 96, "white", None,
          "Godkjenner hvem som skal være i developers og data-admins, og følger med på tilgangene")
    f.box(X[3], y, W[3], 96, "out", None, "Ingen tilgang til data eller tjenester i seg selv", dash="5 4")
    f.ctrl([(X[1] + W[1], y + 48), (X[2], y + 48)])
    f.marker(X[1] + W[1] - 4, y, 1)

    # Rad 2: developers
    y = 190
    who(y, ["Alle som jobber", "operativt med data"], 3)
    f.box(X[1], y, W[1], 112, "role", "developers", "Den vanligste gruppen i et team")
    f.box(X[2], y, W[2], 112, "white", "Fast tilgang", "så lenge man er medlem av gruppen")
    f.access([(X[1] + W[1], y + 56), (X[2], y + 56)])
    f.access([(X[2] + W[2], y + 56), (X[3], y + 56)])
    f.bucket(X[3] + 4, y - 4, 118, 100, "produkt", "inndata til utdata", "data", ssize=16)
    f.bucket(X[3] + 132, y - 4, 118, 100, "delt-bøtter", "teamets egne", "data", lsize=16)
    f.text(X[3] + 4, y + 118, ["og tjenestene som", "behandler dataene"], 16, 400, C["grey"], lh=20)
    f.marker(X[1] + W[1] - 4, y, 2)

    # Rad 3: data-admins
    y = 338
    who(y, ["2–3 personer", "med særskilt behov"], 1)
    f.box(X[1], y, W[1], 172, "role", "data-admins",
          "Normalt også i developers. Godkjenner endringer i automatiske jobber og IaC-repoet, og kan overføre kildedata mellom bakke og sky")
    f.box(X[2], y, W[2], 172, "white", "JIT-tilgang",
          "Aktiveres av personen selv, med skriftlig begrunnelse. Varer maks 8 timer og kan følges av Teamansvarlig")
    f.jit([(X[1] + W[1], y + 86), (X[2], y + 86)])
    f.jit([(X[2] + W[2], y + 86), (X[3], y + 86)])
    f.bucket(X[3] + 4, y + 30, 170, 110, "kilde", "kildedata i klartekst", "datas")
    f.lock(X[3] + 184, y + 34)
    f.marker(X[1] + W[1] - 4, y, 3)

    # Teamansvarlig godkjenner rollene: skinne til venstre for rollekolonnen
    rx = X[1] - 14
    f.path(f"M{X[1]+24},154 L{X[1]+24},170 L{rx},170 L{rx},378", "none", C["dark"], 1.8)
    f.ctrl([(rx, 220), (X[1], 220)], hs=9)
    f.ctrl([(rx, 378), (X[1], 378)], hs=9)

    # Rad 4: automatiske jobber
    y = 548
    f.text(30, y + 26, ["Automatiske", "jobber"], 16, 700, C["ink"], lh=20)
    f.box(X[1], y, W[1], 112, "plat", "Kildomaten", "Kjører teamets skript på hver ny fil i kildebøtta")
    f.box(X[2], y, W[2], 112, "white", "Automatisk",
          "Formålet er at færre trenger tilgang til kildedata")
    f.ctrl([(X[1] + W[1], y + 56), (X[2], y + 56)])
    f.access([(X[2] + W[2], y + 40), (X[3] + 89, y + 40), (X[3] + 89, 338 + 140)])
    f.text(X[3] + 104, y + 56, ["leser fra kilde,", "skriver til produkt"], 16, 400, C["grey"], lh=20)
    f.marker(X[1] + W[1] - 4, y, 4)

    f.frame(["role", "plat", "data", "access", "jit", "ctrl", "marker"],
            "Tilgangsstyring · Hva er Dapla-team? · JIT · Kildomaten")
    return f

if __name__ == "__main__":
    print(m02().save("out"))
