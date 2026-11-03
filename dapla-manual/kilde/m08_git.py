from lib import *

def m08():
    f = Fig("m08-git-arbeidsflyt", 800)
    dark, grey = C["dark"], C["grey"]
    # Baner
    f.rect(30, 16, 940, 160, C["plat"], C["plat2"], 1.5, 12)
    f.text(44, 42, "GitHub", 18, 700, C["ink"])
    f.text(44 + tw("GitHub", 18, 700) + 10, 42, "origin", 16, 400, grey)
    f.rect(30, 192, 940, 170, C["white"], C["line"], 1.5, 12)
    sub = "for eksempel i en tjeneste i Dapla Lab"
    f.text(44, 348, "Ditt lokale repo", 18, 700, C["ink"])
    f.text(44 + tw("Ditt lokale repo", 18, 700) + 10, 348, sub, 16, 400, grey)

    YM, YG = 74, 132        # GitHub: main, gren
    YLM, YLG = 252, 308     # lokalt: main, gren

    def node(x, y, col=dark, r=8):
        f.el.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["white"]}" stroke="{col}" stroke-width="3"/>')

    # Linjer
    f.line(60, YM, 950, YM, dark, 4)
    f.text(950, YM - 12, "main", 16, 700, dark, "end")
    f.line(430, YG, 820, YG, grey, 3)
    f.text(700, YG + 26, "grenen på GitHub", 16, 400, grey)
    f.line(60, YLM, 200, YLM, dark, 4)
    f.text(60, YLM - 12, "main", 16, 700, dark)
    f.path(f"M180,{YLM} C205,{YLM} 205,{YLG} 235,{YLG} L700,{YLG}", "none", grey, 3)
    f.text(710, YLG + 6, "din gren", 16, 400, grey)

    # 1 oppdater main
    node(130, YM); node(130, YLM)
    f.ctrl([(130, YM + 10), (130, YLM - 10)])
    f.label_on(160, 160, "pull", 16)
    # 2 ny gren
    node(180, YLM)
    # 3 endre, commit, push
    for x in (290, 360, 430):
        node(x, YLG, grey)
    f.ctrl([(430, YLG - 10), (430, YG + 10)])
    node(430, YG, grey)
    f.label_on(470, 232, "push", 16)
    # 4 hent main inn i grenen
    node(560, YM)
    f.ctrl([(560, YM + 10), (560, YLG - 10)])
    node(560, YLG, grey)
    f.ctrl([(640, YLG - 10), (640, YG + 10)])
    node(640, YLG, grey); node(640, YG, grey)
    f.label_on(600, 232, "fetch og merge", 16)
    # 5 pull request og merge
    f.ctrl([(820, YG), (870, YM + 10)])
    node(820, YG, grey); node(870, YM)
    f.label_on(770, 102, "pull request", 16)

    # markører i grafen
    f.marker(130, YLM + 34, 1)
    f.marker(180, YLM + 34, 2)
    f.marker(360, YLG - 28, 3)
    f.marker(600, YLG - 28, 4)
    f.marker(870, YM - 30, 5)

    # Kommandoer per steg
    y = 398
    steps = [
        ("Oppdater main", ["git switch main", "git pull"], None),
        ("Lag ny gren", ["git switch -c ‹gren›"], None),
        ("Endre og lagre", ["git status", "git add ‹fil›", 'git commit -m "…"', "git push"],
         "Gjentas til oppgaven er ferdig"),
        ("Sjekk for konflikt", ["git fetch", "git merge origin/main", "git push"],
         "Lettere å løse lokalt enn på GitHub"),
        ("Pull request", [], "Be en kollega se over. Merge og slett grenen"),
    ]
    mono = lambda s: len(s) * 16 * 0.6
    widths = []
    for t, cmds, note in steps:
        widths.append(max([tw(t, 17, 700) + 24] + [mono(c) + 22 for c in cmds]))
    rest = 940 - sum(widths[:4]) - 4*6
    widths[4] = rest
    x = 30
    boxes, hmax = [], 0
    for (t, cmds, note), w in zip(steps, widths):
        h = 50 + len(cmds)*24 + (len(wrap(note, w - 20, 16)) * 21 + 6 if note else 0)
        boxes.append((x, w, t, cmds, note)); hmax = max(hmax, h); x += w + 6
    for i, (x, w, t, cmds, note) in enumerate(boxes):
        f.rect(x, y, w, hmax, C["white"], C["line"], 1.4, 8)
        f.marker(x + 4, y, i + 1)
        f.text(x + 11, y + 34, t, 17, 700)
        cy = y + 64
        if cmds:
            f.text(x + 11, cy, cmds, 16, 400, C["ink"], family=MONO, lh=24)
            cy += len(cmds)*24 + 2
        if note:
            f.para(x + 11, cy, note, w - 20, 16, 400, C["grey"], lh=21)

    f.h = int(y + hmax + 24 + 92)
    f.frame([("ctrl", "Git-operasjon"), "marker"], "Anbefalt arbeidsflyt med Git")
    return f

if __name__ == "__main__":
    print(m08().save("out"))
