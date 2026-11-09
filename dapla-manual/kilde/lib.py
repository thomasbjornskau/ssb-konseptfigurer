"""Komponenter for konseptfigurer i Dapla-manualen (manualformat).

Format: viewBox 1000 bred, fri høyde. Minste tekst 16 px (vises ca. 13 px i en
800 px kolonne). Ingen tittel og ikke noe forklaringspanel i figuren:
bildeteksten og artikkelteksten forklarer. Tegnforklaring og kildelinje er alltid med.

Bare rect, line, polyline, polygon, circle, ellipse, path og text.
Farger som attributter, pilspisser som polygoner, tekst brytes manuelt.
"""
import math, os, subprocess
from xml.sax.saxutils import escape
from PIL import ImageFont

FONT = "Open Sans, Segoe UI, Arial, sans-serif"
HEAD = "Roboto, Arial, sans-serif"            # mellomtitler (profilhåndboken)
MONO = "DejaVu Sans Mono, Consolas, monospace"
TTF = os.path.expanduser("~/.fonts/OpenSans.ttf")
TTF_HEAD = os.path.expanduser("~/.fonts/Roboto.ttf")
DATO = "09.11.2026"

C = dict(
    dark="#274247", ink="#274247", grey="#5e787a", line="#cdd3d4", white="#ffffff",
    plat="#f0f8f9", plat2="#c3dcdc",
    green="#00824d", green2="#b6e8b8", green3="#ecfeed",
    lil="#7e5ee8", lil2="#d2ceff", lil3="#f2f0ff", liltxt="#4b2fb0",
    out="#b9c5c6", out2="#f3f5f5",
)

# Type ting -> (fyll, strek, tekst)
KIND = {
    "plat": (C["plat"], C["plat2"], C["ink"]),      # plattform, tjenester, flater
    "data": (C["green3"], C["green"], C["ink"]),    # data, statistikk, metadata
    "datas": (C["green2"], C["green"], C["ink"]),   # data, sterkere (sensitiv/kilde)
    "role": (C["lil3"], C["lil"], C["liltxt"]),     # roller, team, ansvar
    "out": (C["out2"], C["out"], C["grey"]),        # utenfor SSB / utenfor scope
    "white": (C["white"], C["line"], C["ink"]),
    "dark": (C["dark"], C["dark"], C["white"]),
}

_fonts = {}
def _font(size, weight):
    key = (size, weight)
    if key not in _fonts:
        if weight >= 700:
            f = ImageFont.truetype(TTF_HEAD, size)
            try: f.set_variation_by_axes([700, 100])
            except Exception: pass
        else:
            f = ImageFont.truetype(TTF, size)
            try: f.set_variation_by_axes([weight, 100])
            except Exception: pass
        _fonts[key] = f
    return _fonts[key]

def tw(s, size=18, weight=400):
    """Tekstbredde i px. Fet tekst (700) er Roboto Bold, resten Open Sans."""
    return _font(size, weight).getlength(s)

def wrap(s, width, size=18, weight=400):
    """Bryter på mellomrom. Myk bindestrek (\u00ad) i lange ord gir orddeling med «-»."""
    SH = "\u00ad"
    out = []
    for para in s.split("\n"):
        line = ""
        for word in para.split(" "):
            cand = (line + " " + word).strip()
            if tw(cand.replace(SH, ""), size, weight) <= width or not line and SH not in word:
                line = cand
                continue
            # prøv å dele ordet på myke bindestreker
            parts = word.split(SH)
            placed = False
            if len(parts) > 1:
                for k in range(len(parts) - 1, 0, -1):
                    head = "".join(parts[:k]) + "-"
                    c2 = (line + " " + head).strip()
                    if tw(c2, size, weight) <= width:
                        out.append(c2); line = "".join(parts[k:]); placed = True
                        break
            if not placed:
                if line: out.append(line)
                line = word
                # ordet er for langt alene: del det på myke bindestreker
                while SH in line and tw(line.replace(SH, ""), size, weight) > width:
                    parts = line.split(SH); done = False
                    for k in range(len(parts) - 1, 0, -1):
                        head = "".join(parts[:k]) + "-"
                        if tw(head, size, weight) <= width:
                            out.append(head); line = SH.join(parts[k:]); done = True
                            break
                    if not done: break
        out.append(line.replace(SH, ""))
    return [l.replace(SH, "") for l in out]


class Fig:
    def __init__(self, name, h, w=1000):
        self.name, self.w, self.h = name, w, h
        self.el = []

    # --- primitiver -----------------------------------------------------
    def rect(self, x, y, w, h, fill="none", stroke="none", sw=1, rx=2, dash=None):
        """Profil: 2 px hjørneradius på flater, full radius bare for piller. 1 px rammer, 2 px for fokus."""
        rx = rx if rx >= min(w, h) / 2 - 0.5 else 2
        sw = 2 if sw >= 2 else 1
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                       f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=None, sw=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                       f'stroke="{stroke or C["line"]}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=18, weight=400, fill=None, anchor="start", family=None, lh=None):
        """s kan være str eller liste med linjer. y er grunnlinjen for første linje."""
        lines = s if isinstance(s, list) else [s]
        lh = lh or round(size * 1.3)
        fam = family or (HEAD if weight >= 700 else FONT)
        for i, ln in enumerate(lines):
            n = len(ln) - len(ln.lstrip(" "))
            sp = ' xml:space="preserve"' if n else ""
            self.el.append(f'<text{sp} x="{x:.1f}" y="{y + i*lh:.1f}" font-family="{fam}" font-size="{size}" '
                           f'font-weight="{weight}" fill="{fill or C["ink"]}" text-anchor="{anchor}">{escape(ln)}</text>')
        return y + (len(lines) - 1) * lh

    def para(self, x, y, s, width, size=18, weight=400, fill=None, anchor="start", lh=None):
        """Bryter tekst til bredde. Returnerer y for siste linje."""
        return self.text(x, y, wrap(s, width, size, weight), size, weight, fill, anchor, lh=lh)

    def poly(self, pts, fill, stroke="none", sw=1):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.el.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def path(self, d, fill="none", stroke=None, sw=1.5, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<path d="{d}" fill="{fill}" stroke="{stroke or C["ink"]}" stroke-width="{sw}"{da}/>')

    # --- piler ----------------------------------------------------------
    def head(self, x, y, ang, col, size=10):
        a = math.radians(ang)
        p1 = (x, y)
        p2 = (x - size*math.cos(a) + size*0.55*math.sin(a), y - size*math.sin(a) - size*0.55*math.cos(a))
        p3 = (x - size*math.cos(a) - size*0.55*math.sin(a), y - size*math.sin(a) + size*0.55*math.cos(a))
        self.poly([p1, p2, p3], col)

    def arrow(self, pts, col=None, sw=2, dash=None, start=False, end=True, hs=11):
        col = col or C["green"]
        pts = [tuple(p) for p in pts]
        # trekk linja litt inn så pilspissen ikke stikker ut
        def ang(a, b): return math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))
        draw = list(pts)
        if end:
            a = math.radians(ang(pts[-2], pts[-1])); draw[-1] = (pts[-1][0]-hs*0.8*math.cos(a), pts[-1][1]-hs*0.8*math.sin(a))
        if start:
            a = math.radians(ang(pts[1], pts[0])); draw[0] = (pts[0][0]-hs*0.8*math.cos(a), pts[0][1]-hs*0.8*math.sin(a))
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in draw)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{sw}" '
                       f'stroke-linejoin="round"{d}/>')
        if end: self.head(*pts[-1], ang(pts[-2], pts[-1]), col, hs)
        if start: self.head(*pts[0], ang(pts[1], pts[0]), col, hs)

    # piltyper med fast betydning (samme i hele serien)
    def flow(self, pts, **k):   self.arrow(pts, C["green"], **k)                      # dataflyt
    def access(self, pts, **k): self.arrow(pts, C["lil"], sw=2, **k)                # fast tilgang
    def jit(self, pts, **k):    self.arrow(pts, C["lil"], sw=2, dash="7 5", **k)    # tidsavgrenset tilgang
    def ctrl(self, pts, **k):   self.arrow(pts, C["dark"], sw=2, **k)               # styrer / godkjenner / konfigurerer
    def share(self, pts, **k):  self.arrow(pts, C["green"], sw=2, dash="2 5", **k)  # deling (lesetilgang)
    def backup(self, pts, **k): self.arrow(pts, C["green"], sw=2, dash="7 5", **k)  # sikkerhetskopi (manuelt)
    def step(self, pts, **k):   self.arrow(pts, C["grey"], sw=2, **k)               # neste steg / rekkefølge

    def label_on(self, x, y, s, size=16, fill=None, weight=400, bg=C["white"]):
        """Tekst med hvit bakgrunn, for etiketter på piler."""
        w = tw(s, size, weight) + 10
        self.rect(x - w/2, y - size*0.95, w, size*1.35, bg, "none", rx=4)
        self.text(x, y, s, size, weight, fill or C["grey"], "middle")

    # --- byggeklosser ---------------------------------------------------
    def box_h(self, w, title=None, body=None, tsize=18, bsize=16, pad=12):
        """Høyden en boks trenger for tittel og brødtekst."""
        h = 2*pad
        if title: h += len(wrap(title, w - 2*pad, tsize, 700)) * round(tsize*1.3) - round(tsize*0.3)
        if title and body: h += round(tsize*0.45)
        if body: h += len(wrap(body, w - 2*pad, bsize, 400)) * round(bsize*1.3) - round(bsize*0.3)
        return h + 4

    def box(self, x, y, w, h=None, kind="plat", title=None, body=None, dash=None, tsize=18, bsize=16,
            pad=12, center=False, sw=1, rx=2, tfill=None, bfill=None, minh=0):
        """Boks med tittel og brødtekst. h=None gir automatisk høyde. Returnerer høyden."""
        need = self.box_h(w, title, body, tsize, bsize, pad)
        h = max(h or 0, need, minh)
        fill, stroke, txt = KIND[kind]
        self.rect(x, y, w, h, fill, stroke, sw, rx, dash)
        cy = y + pad + tsize * 0.85 if title else y + pad + bsize * 0.85
        ax, anc = (x + w/2, "middle") if center else (x + pad, "start")
        if title:
            cy = self.para(ax, cy, title, w - 2*pad, tsize, 700, tfill or txt, anc) + round(tsize*0.45) + round(bsize*1.3)
        if body:
            self.para(ax, cy, body, w - 2*pad, bsize, 400, bfill or (C["grey"] if kind != "dark" else C["white"]), anc)
        return h

    def bucket(self, x, y, w, h, label, sub=None, kind="data", dash=None, lsize=17, ssize=16):
        """Sylinder (bøtte). x,y = øvre venstre hjørne av omsluttende boks. Tekst sentreres i kroppen."""
        fill, stroke, txt = KIND[kind]
        ry = min(10, h*0.14)
        d = (f"M{x},{y+ry} L{x},{y+h-ry} A{w/2},{ry} 0 0 0 {x+w},{y+h-ry} L{x+w},{y+ry}")
        self.path(d + " Z", fill, stroke, 1, dash)
        self.el.append(f'<ellipse cx="{x+w/2:.1f}" cy="{y+ry:.1f}" rx="{w/2:.1f}" ry="{ry:.1f}" fill="{fill}" '
                       f'stroke="{stroke}" stroke-width="1"' + (f' stroke-dasharray="{dash}"' if dash else "") + '/>')
        L = wrap(label, w - 10, lsize, 700)
        S = wrap(sub, w - 12, ssize, 400) if sub else []
        llh, slh = round(lsize*1.2), round(ssize*1.25)
        block = len(L)*llh + len(S)*slh
        top = y + ry*2 + (h - ry*3 - block) / 2
        self.text(x + w/2, top + lsize*0.85, L, lsize, 700, txt, "middle", lh=llh)
        if S:
            self.text(x + w/2, top + len(L)*llh + ssize*0.85, S, ssize, 400, C["grey"], "middle", lh=slh)

    def notebox(self, x, y, w, h):
        """Faktaboks: mørk 1 med 5 px grønn 4 aksentkant til venstre (som FactBox i designsystemet)."""
        self.rect(x, y, w, h, C["plat"], "none", rx=2)
        self.rect(x, y, 5, h, C["green"], "none", rx=0)

    def person(self, cx, cy, col=None, r=9):
        col = col or C["ink"]
        self.el.append(f'<circle cx="{cx:.1f}" cy="{cy-r*1.3:.1f}" r="{r}" fill="{col}"/>')
        self.path(f"M{cx-r*1.7},{cy+r*1.9} Q{cx-r*1.7},{cy} {cx},{cy} Q{cx+r*1.7},{cy} {cx+r*1.7},{cy+r*1.9} Z",
                  col, "none", 0)

    def lock(self, x, y, col=None):
        col = col or C["green"]
        self.path(f"M{x+3},{y+7} L{x+3},{y+4} A5,5 0 0 1 {x+13},{y+4} L{x+13},{y+7}", "none", col, 2)
        self.rect(x, y+7, 16, 11, col, "none", rx=2)

    def marker(self, x, y, n, r=13):
        self.el.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C["dark"]}"/>')
        self.text(x, y + 5.5, str(n), 16, 700, C["white"], "middle", family=FONT)

    def chip(self, x, y, s, kind="white", size=16, dash=None, mono=False, pad=9, h=None):
        """Pille. Returnerer bredde."""
        fam = MONO if mono else None
        w = (tw(s, size, 400 if mono else 600) * (1.12 if mono else 1)) + 2*pad
        h = h or size + 12
        fill, stroke, txt = KIND[kind]
        self.rect(x, y, w, h, fill, stroke, 1.3, h/2, dash)
        self.text(x + w/2, y + h/2 + size*0.36, s, size, 600 if not mono else 400, txt, "middle", family=fam)
        return w

    def tag(self, x, y, s, kind="dark", size=16):
        """Statusetikett (FORSLAG, PLANLAGT ...). x er høyrekant."""
        w = tw(s, size, 700) + 18
        fill, stroke, txt = KIND[kind]
        self.rect(x - w, y, w, size + 10, fill, stroke, 1.3, 4)
        self.text(x - w/2, y + size*0.95 + 2, s, size, 700, txt, "middle")
        return w

    def zone(self, x, y, w, h, title, kind="plat", sub=None, dash=None, tsize=18):
        fill, stroke, txt = KIND[kind]
        self.rect(x, y, w, h, fill, stroke, 1, 2, dash)
        self.text(x + 14, y + 26, title, tsize, 700, txt)
        if sub:
            self.text(x + 14 + tw(title, tsize, 700) + 10, y + 26, sub, 16, 400, C["grey"])

    # --- ramme: tegnforklaring og kildelinje ----------------------------
    LEG = {
        "flow": "Dataflyt", "access": "Fast tilgang", "jit": "Tidsavgrenset tilgang (JIT)",
        "ctrl": "Styrer / godkjenner", "share": "Deling (lesetilgang)", "backup": "Sikkerhetskopi", "step": "Neste steg",
        "plat": "Plattform og tjenester", "data": "Data", "role": "Roller og team",
        "out": "Utenfor Dapla", "dash": "Kan skrus på / valgfritt", "plan": "Planlagt",
        "marker": "Forklares i teksten",
    }

    def legend(self, items, y=None, x=30, maxw=None):
        y = y or self.h - 52
        maxw = maxw or self.w - 60
        cx, cy = x, y
        for it in items:
            if isinstance(it, tuple): it, lab = it
            else: lab = self.LEG.get(it, it)
            iw = 36 + tw(lab, 16) + 22
            if cx + iw > x + maxw:
                cx = x; cy += 26
            if it in ("flow", "access", "jit", "ctrl", "share", "step", "backup"):
                getattr(self, it)([(cx, cy-5), (cx+28, cy-5)], hs=8)
            elif it in ("plat", "data", "role", "out"):
                f, s, _ = KIND[it]; self.rect(cx+2, cy-14, 24, 16, f, s, 1.3, 3)
            elif it == "dash":
                self.rect(cx+2, cy-14, 24, 16, C["white"], C["grey"], 1.3, 3, "4 3")
            elif it == "plan":
                self.rect(cx+2, cy-14, 24, 16, C["out2"], C["out"], 1.3, 3, "4 3")
            elif it == "marker":
                self.marker(cx+14, cy-6, 1, r=10)
            self.text(cx + 36, cy, lab, 16, 400, C["grey"])
            cx += iw
        return cy

    def frame(self, legend, source):
        self.line(30, self.h - 88, self.w - 30, self.h - 88, C["line"], 1)
        ly = self.legend(legend, self.h - 60)
        self.text(self.w - 30, self.h - 12, f"Kilde: Dapla-manualen, {source} · Utkast {DATO}",
                  16, 400, C["grey"], "end")

    # --- lagre ----------------------------------------------------------
    def svg(self):
        body = "\n  ".join(self.el)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}">\n  '
                f'<rect x="0" y="0" width="{self.w}" height="{self.h}" fill="#ffffff"/>\n  {body}\n</svg>\n')

    def save(self, outdir):
        os.makedirs(outdir, exist_ok=True)
        p = os.path.join(outdir, self.name + ".svg")
        open(p, "w", encoding="utf-8").write(self.svg())
        png = os.path.join(outdir, "png", self.name + ".png")
        os.makedirs(os.path.dirname(png), exist_ok=True)
        subprocess.run(["rsvg-convert", "-w", "1600", p, "-o", png], check=True)
        return p, png
