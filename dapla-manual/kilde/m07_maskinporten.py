from lib import *

def m07():
    f = Fig("m07-maskinporten-guardian", 860)
    # Soner
    f.zone(30, 16, 560, 470, "SSB", "plat")
    f.zone(620, 16, 350, 210, "Digdir", "out")
    f.zone(620, 256, 350, 230, "Ekstern virksomhet", "out")

    # Komponenter i SSB
    f.box(50, 66, 180, 84, "white", "Secret Manager", "Keycloak client secret", pad=10)
    f.box(50, 360, 180, 84, "white", "Keycloak", "SSBs innlogging", pad=10)
    ak = f.box(240, 214, 190, None, "role", "API-konsument", "Teamets kode eller tjeneste", pad=10)
    g = f.box(330, 66, 230, None, "white", "Maskinporten Guardian",
              "Har tilgang til SSBs virksomhets­sertifikat", pad=10)
    f.bucket(276, 370, 120, 96, "kilde", "teamets kildebøtte", "datas")

    # Digdir og ekstern
    f.box(640, 66, 310, 70, "white", "Maskinporten", "Utsteder sikkerhetstoken", pad=10)
    f.box(640, 148, 310, 62, "white", "Samarbeidsportalen", None, pad=10)
    f.box(640, 330, 310, 84, "white", "API-tilbyder", "Deler data via API scopes", pad=10)

    # 1 Secret Manager -> konsument
    f.ctrl([(140, 150), (140, 240), (240, 240)])
    f.marker(140, 190, 1)
    # 2 Keycloak -> konsument
    f.ctrl([(140, 360), (140, 280), (240, 280)])
    f.marker(140, 320, 2)
    # 3 konsument -> Guardian
    f.ctrl([(390, 66 + g), (390, 214)])
    f.marker(366, 66 + g + 22, 3)
    # 4 Guardian -> Maskinporten
    f.ctrl([(640, 100), (560, 100)])
    f.marker(600, 76, 4)
    # 5 konsument henter data hos API-tilbyder
    f.flow([(640, 372), (500, 372), (500, 262), (430, 262)])
    f.marker(570, 348, 5)
    # konsument skriver til kildebøtta
    f.flow([(336, 214 + ak), (336, 370)])

    # Før du starter
    y = 520
    f.text(30, y, "Før du starter", 18, 700)
    pre = [("A", "API-tilbyderen gir SSB tilgang til et API scope i Samarbeidsportalen"),
           ("B", "M2M-teamet i SSB oppretter Maskinporten-klienter, én per miljø"),
           ("C", "En Keycloak-bruker for Guardian opprettes. Client ID og secret ligger i Secret Manager")]
    bw, gap = 296, 26
    hh = max(f.box_h(bw - 32, None, s) for _, s in pre) + 8
    for i, (n, s) in enumerate(pre):
        x = 30 + i*(bw + gap)
        f.rect(x, y + 14, bw, hh, C["white"], C["line"], 1.4, 8)
        f.marker(x + 20, y + 14 + 22, n)
        f.para(x + 44, y + 14 + 12 + 16*0.85, s, bw - 56, 16, 400, C["ink"])
        if i < 2: f.step([(x + bw, y + 14 + hh/2), (x + bw + gap, y + 14 + hh/2)], hs=8)

    yn = y + 14 + hh + 38
    f.notebox(30, yn - 22, 940, 58)
    f.para(50, yn, "Med personlig bruker faller steg 1 og 2 bort: Keycloak-tokenet hentes for eksempel med AuthClient "
           "i dapla-toolbelt, og personen må være autorisert i Guardian på forhånd.", 908, 16, 400, C["ink"])

    f.h = int(yn + 50 + 92)
    f.frame(["plat", "out", "role", "data", ("ctrl", "Token eller hemmelighet hentes, i nummerert rekkefølge"), "flow", "step"],
            "Maskinporten · Data Collector")
    return f

if __name__ == "__main__":
    print(m07().save("out"))
