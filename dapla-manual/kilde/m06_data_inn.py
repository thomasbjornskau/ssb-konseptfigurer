from lib import *

def m06():
    f = Fig("m06-data-inn-til-dapla", 830)
    X = [30, 236, 496, 736]
    W = [176, 230, 210, 234]
    for x, s in zip(X, ["Hvor data kommer fra", "Via", "Overføres med", "Lander i teamets bøtter"]):
        f.text(x, 30, s, 16, 700, C["grey"])
    f.line(30, 42, 970, 42, C["line"], 1)

    rows = [60, 220, 380, 556]
    RH = 136

    def lanehead(y, n, s):
        f.marker(X[0] + 12, y + 2, n)
        f.text(X[0] + 32, y + 8, s, 17, 700, C["ink"])

    # 1 Altinn 3
    y = rows[0]
    lanehead(y, 1, "Skjema i Altinn 3")
    f.box(X[0], y + 26, W[0], 92, "out", None, "Oppgavegivere sender inn skjema i Altinn 3", pad=10)
    f.box(X[1], y + 26, W[1], 92, "role", "Team SU-V", "Henter inn og lagrer xml og metadata i egne delt-bøtter",
          pad=10, tsize=17)
    f.box(X[2], y + 26, W[2], 92, "plat", "Transfer Service", "SU-V gir tilgang til teamets kildeprosjekt",
          pad=10, tsize=17)
    f.flow([(X[0] + W[0], y + 72), (X[1], y + 72)], hs=9)
    f.flow([(X[1] + W[1], y + 72), (X[2], y + 72)], hs=9)

    # 2 API
    y = rows[1]
    lanehead(y, 2, "API hos ekstern virksomhet")
    f.box(X[0], y + 26, W[0], 92, "out", None, "API-tilbyder, beskyttet av Maskinporten", pad=10)
    f.box(X[1], y + 26, W[1], 92, "plat", "Maskinporten Guardian", "Henter sikkerhetstoken på vegne av SSB",
          pad=10, tsize=17)
    f.box(X[2], y + 26, W[2], 92, "plat", "Teamets kode", "eller Data Collector, som skriver til kildebøtter",
          pad=10, tsize=17)
    f.ctrl([(X[1] + W[1], y + 72), (X[2], y + 72)], hs=9)
    f.flow([(X[0] + W[0]/2, y + 118), (X[0] + W[0]/2, y + 134), (X[2] + W[2]/2, y + 134), (X[2] + W[2]/2, y + 118)],
           hs=9)
    f.label_on((X[1] + X[1] + W[1]) / 2, y + 140, "data hentes med tokenet", 16)

    # 3 MoveIT
    y = rows[2]
    lanehead(y, 3, "Filer fra eksterne leverandører")
    f.box(X[0], y + 26, W[0], 92, "out", None, "Leverandøren laster opp filer i MoveIT", pad=10)
    f.box(X[1], y + 26, W[1], 92, "out", "MoveIT på bakke", "Flytter filene til Cloud_sync-området. Settes opp av s782",
          pad=10, tsize=17)
    f.box(X[2], y + 26, W[2], 92, "plat", "Transfer Service", "Overfører høyst én gang i timen",
          pad=10, tsize=17)
    f.flow([(X[0] + W[0], y + 72), (X[1], y + 72)], hs=9)
    f.flow([(X[1] + W[1], y + 72), (X[2], y + 72)], hs=9)

    # Felles mål: kildebøtta
    ky0, ky1 = rows[0] + 20, rows[2] + 124
    f.bucket(X[3] + 24, ky0, W[3] - 24, ky1 - ky0, "kilde", "kildebøtta i prod. Anbefalt: én mappe per kilde", "datas")
    for y in rows[:3]:
        f.flow([(X[2] + W[2], y + 72), (X[3] + 24, y + 72)], hs=9)
    f.text(X[3] + 24 + (W[3] - 24)/2, ky1 + 26, "Videre med Kildomaten", 16, 400, C["grey"], "middle")

    # 4 Fra bakke
    y = rows[3]
    f.line(30, y - 18, 970, y - 18, C["line"], 1, "4 4")
    lanehead(y, 4, "Data fra bakke (prodsonen)")
    f.box(X[0], y + 26, W[0], 112, "out", None, "Data på Linux i prodsonen. Inndata anbefales lagret som parquet først",
          pad=10)
    f.box(X[1], y + 26, W[1], 112, "out", "Cloud_sync-området", "/ssb/cloud_sync/ ‹team›/…/tilsky/", pad=10, tsize=17)
    f.box(X[2], y + 26, W[2], 112, "plat", "Transfer Service", "Kildedata krever en data-admin med JIT",
          pad=10, tsize=17)
    f.flow([(X[0] + W[0], y + 82), (X[1], y + 82)], hs=9)
    f.flow([(X[1] + W[1], y + 82), (X[2], y + 82)], hs=9)
    f.bucket(X[3] + 24, y + 26, 100, 82, "tilsky", None, "data", lsize=16)
    f.bucket(X[3] + 134, y + 26, 100, 82, "kilde- tilsky", None, "data", lsize=16)
    f.flow([(X[2] + W[2], y + 82), (X[3] + 24, y + 82)], hs=9)
    f.para(X[3] + 24, y + 132, "Mellomstasjoner. Data flyttes så selv til riktig bøtte", 212, 16, 400, C["grey"])

    f.frame(["out", "role", "plat", "data", "flow", "ctrl", "marker"],
            "Altinn 3 · Maskinporten · Data Collector · MoveIT · Transfer Service · Overgang")
    return f

if __name__ == "__main__":
    print(m06().save("out"))
