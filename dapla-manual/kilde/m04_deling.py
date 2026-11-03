from lib import *

def m04():
    f = Fig("m04-deling-av-data", 800)
    # Team A
    f.zone(30, 16, 620, 400, "Team A deler", "role", sub="eier delt-bøttene")
    f.bucket(52, 150, 170, 120, "produkt", "pseudonymiserte personopplysninger", "data")
    f.text(52, 138, "Produktbøtta", 16, 700, C["grey"])

    # Standard delt-bøtte
    f.bucket(420, 66, 210, 100, "delt-ameld", "type: standard", "data")
    f.flow([(222, 190), (300, 190), (300, 116), (420, 116)])
    f.label_on(352, 104, "teamet skriver selv", 16)
    f.marker(630, 66, 1)

    # Delomat delt-bøtte
    f.box(256, 262, 140, 0, "plat", "Delomaten", "de-pseudo­nymiserer automatisk", pad=10, tsize=17, bsize=16)
    f.flow([(222, 240), (240, 240), (240, 300), (256, 300)], hs=9)
    f.bucket(420, 250, 210, 100, "delt-ameld-pii", "type: delomat", "data")
    f.flow([(396, 300), (420, 300)], hs=9)
    f.lock(606, 360)
    f.text(600, 374, "Team A har ikke tilgang", 16, 400, C["grey"], "end")
    f.marker(630, 250, 2)

    # Mottakere
    f.zone(700, 56, 270, 120, "Team B", "role")
    f.person(732, 128, C["liltxt"])
    f.text(756, 136, "developers", 16, 600, C["liltxt"])
    f.zone(700, 240, 270, 120, "Team C", "role")
    f.person(732, 312, C["liltxt"])
    f.text(756, 320, "developers", 16, 600, C["liltxt"])
    f.share([(630, 116), (700, 116)], hs=9)
    f.share([(630, 300), (700, 300)], hs=9)
    f.text(835, 200, "Tilgang gis under sharedWith", 16, 400, C["grey"], "middle")
    f.marker(970, 56, 3)

    # Slik settes det opp
    y = 452
    f.text(30, y, "Slik settes det opp, i teamets IaC-repo", 18, 700)
    steps = [
        ("Skru på feature", "shared-buckets i projects.yaml. For Delomaten også delomaten"),
        ("Opprett bøtta", "Kortnavn og type i buckets-shared.yaml"),
        ("Gi tilgang", "Mottakende gruppe under sharedWith i samme fil"),
        ("Godkjenn og rull ut", "data-admins godkjenner PR-en, deretter atlantis plan og apply"),
    ]
    bw, gap = 220, 20
    hs = max(f.box_h(bw, t, b) for t, b in steps)
    for i, (t, b) in enumerate(steps):
        x = 30 + i*(bw + gap)
        f.box(x, y + 16, bw, hs, "plat", t, b)
        f.marker(x + 4, y + 16, i + 4)
        if i < 3: f.step([(x + bw, y + 16 + hs/2), (x + bw + gap, y + 16 + hs/2)], hs=8)

    # Merknad om Delomaten
    yn = y + 16 + hs + 48
    f.rect(30, yn - 22, 940, 58, C["out2"], "none", rx=8)
    f.para(46, yn, "Delomaten brukes unntaksvis. Diskuter formålet med nærmeste leder og rådfør deg gjerne med "
           "personvernombudet. Dataene må være dokumentert i Datadoc, også hvordan de er pseudonymisert.",
           908, 16, 400, C["ink"])

    f.h = int(yn + 50 + 92)
    f.frame(["data", "plat", "role", "flow", "share", "step", "marker"], "Deling av data · Delomaten · Features")
    return f

if __name__ == "__main__":
    print(m04().save("out"))
