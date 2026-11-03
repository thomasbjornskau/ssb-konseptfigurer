from lib import *

def m01():
    f = Fig("m01-hva-et-dapla-team-faar", 800)

    def project(x, y, w, h, title, tech, locked=False):
        f.rect(x, y, w, h, C["white"], C["plat2"], 1.4, 8)
        tl = title if isinstance(title, list) else [title]
        te = tech if isinstance(tech, list) else [tech]
        yy = f.text(x + 12, y + 26, tl, 18, 700, lh=22)
        f.text(x + 12, yy + 22, te, 16, 400, C["grey"], lh=20)
        if locked: f.lock(x + w - 28, y + 10)

    # Teamramme
    f.zone(30, 16, 940, 590, "Dapla-team «Skatt næring»", "role", sub="teknisk navn: skatt-naering")
    f.zone(48, 54, 572, 380, "Prodmiljø", "plat", sub="skarpe data")
    f.zone(636, 54, 316, 380, "Testmiljø", "plat", sub="testdata")
    f.marker(626, 54, 1)

    # Prod: kildeprosjekt
    project(64, 92, 270, 326, "Kildeprosjekt", "skatt-naering-kilde-p", locked=True)
    f.bucket(80, 156, 238, 92, "kilde", "kildedata, sensitive", "datas")
    f.bucket(80, 290, 114, 78, "kilde-tilsky", None, "data", lsize=16)
    f.bucket(204, 290, 114, 78, "kilde-frasky", None, "data", lsize=16)
    f.text(199, 398, "mellomstasjoner bakke ↔ sky", 16, 400, C["grey"], "middle")
    f.marker(76, 156, 2)

    # Prod: standardprosjekt
    project(346, 92, 260, 326, "Standardprosjekt", "skatt-naering-p")
    f.bucket(362, 156, 228, 92, "produkt", "inndata til utdata", "data")
    f.bucket(362, 290, 109, 78, "tilsky", None, "data", lsize=16)
    f.bucket(481, 290, 109, 78, "frasky", None, "data", lsize=16)
    f.text(476, 398, "mellomstasjoner bakke ↔ sky", 16, 400, C["grey"], "middle")
    f.marker(594, 290, 3)

    # Test
    project(652, 92, 140, 262, ["Kilde-", "prosjekt"], ["skatt-naering-", "kilde-t"], locked=True)
    project(804, 92, 134, 262, ["Standard-", "prosjekt"], ["skatt-naering-t"])
    f.bucket(664, 214, 116, 92, "kilde", "testdata", "datas")
    f.bucket(816, 214, 110, 92, "produkt", "testdata", "data")
    f.para(794, 384, "Ingen tilsky- og frasky-bøtter i test", 280, 16, 400, C["grey"], "middle")

    # Følger med teamet
    f.text(48, 468, "Følger også med teamet", 18, 700, C["liltxt"])
    f.box(48, 482, 300, 108, "role", "To tilgangsgrupper",
          "skatt-naering-developers og skatt-naering-data-admins (AD-grupper)")
    f.box(362, 482, 256, 108, "role", "GitHub-team", "skatt-naering, med samme medlemmer og grupper")
    f.box(632, 482, 320, 108, "plat", "IaC-repo", "skatt-naering-iac. Definerer alle ressursene i tekstfiler")
    f.marker(952, 482, 4)
    f.ctrl([(794, 482), (794, 434)])
    f.label_on(794, 464, "definerer", 16)

    # Features utenfor rammen
    f.text(30, 646, "Kan skrus på ved behov (features)", 18, 700)
    x = 30
    for s in ["Transfer Service", "Kildomaten", "shared-buckets (delt-bøtter)", "Delomaten"]:
        x += f.chip(x, 660, s, "white", dash="5 4") + 12
    f.marker(x + 10, 674, 5)

    f.frame(["plat", "data", "role", "ctrl", "dash", "marker"], "Hva er Dapla-team? · Features")
    return f

if __name__ == "__main__":
    print(m01().save("out"))
