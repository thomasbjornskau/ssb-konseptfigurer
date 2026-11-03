from lib import *

def m11():
    f = Fig("m11-flytte-statistikk-til-dapla", 800)
    top = 52
    # 1 Planlegg
    h1 = f.box(30, top, 196, None, "plat", "Planlegg overgangen",
               "Kartlegg dagens løp (as-is) og ønsket løp (to-be) med Dataflyt-opplegget i Confluence. "
               "Få veiledning fra s831, støtteteamene og Tech Coachene")
    f.marker(222, top, 1)
    f.text(30, 32, "Alltid først", 16, 700, C["grey"])

    # Gruppe: rekkefølgen kan variere
    gx, gw = 256, 714
    f.text(gx, 32, "Deretter, i den rekkefølgen som passer", 16, 700, C["grey"])
    steps = [
        ("Opprett Dapla-team", "Seksjonslederen oppretter teamet i Dapla Ctrl. Ett team per gruppe som jobber "
                               "med de samme dataene"),
        ("Flytt data til Dapla", "Start med inndata, gjerne testdata eller fjorårets data. Følg navnestandarden"),
        ("Lag repo med ssb-project", "Reponavnet skal begynne med stat-. Se stat-eksempel på GitHub"),
        ("Jobb deg gjennom datatilstandene", "Bygg produksjonsløpet én datatilstand om gangen"),
    ]
    bw, gap = 162, 16
    hs = max(f.box_h(bw, t, b) for t, b in steps)
    hs = max(hs, h1 - 32)
    f.rect(gx, top, gw, hs + 32, C["white"], C["grey"], 1.4, 10, "6 4")
    for i, (t, b) in enumerate(steps):
        x = gx + 16 + i*(bw + gap)
        f.box(x, top + 16, bw, hs, "plat", t, b)
        f.marker(x + bw - 4, top + 16, i + 2)
    f.step([(226, top + 60), (gx, top + 60)], hs=9)

    # Slutt
    ye = top + max(h1, hs + 32) + 22
    f.step([(gx + gw/2, top + hs + 32), (gx + gw/2, ye + 6)], hs=9)
    f.box(gx + gw/2 - 170, ye + 6, 340, None, "white", "Ta finpussen til slutt",
          "God dokumentasjon underveis, detaljene til slutt", center=True)

    # Råd
    yr = ye + 120
    f.text(30, yr, "Råd fra manualen", 18, 700)
    tips = [("Bygg i skyen", "Bakken isolerer deg fra ny funksjonalitet, og Jupyter der er ikke skalert for "
                             "produksjonsløp"),
            ("Bruk ssb-fagfunksjoner", "Python-pakke med felles funksjonalitet, blant annet for versjonering"),
            ("Lær standardene tidlig", "Det sparer tid og hodebry senere"),
            ("Be om hjelp", "Støtteteamene, Statistikktjenester og Viva Engage")]
    tw_, tg = 226, 12
    ht = max(f.box_h(tw_, t, b) for t, b in tips)
    for i, (t, b) in enumerate(tips):
        f.box(30 + i*(tw_ + tg), yr + 14, tw_, ht, "white", t, b)

    f.h = int(yr + 14 + ht + 30 + 92)
    f.frame([("plat", "Steg i overgangen"), "step", ("dash", "Rekkefølgen kan variere"), "marker"],
            "Hvordan flytte statistikkproduksjon til Dapla?")
    return f

if __name__ == "__main__":
    print(m11().save("out"))
