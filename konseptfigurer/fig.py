"""Kjernen i konseptfigurer: Fig-klassen, palett og primitive former.
Opprinnelig fra SCB-serien: Brukere, Dapla-team og tilgangsstyring.
Én grunnfigur, fem varianter (oversikt + fire fokus). 1920x1080 (16:9).
Kun PowerPoint-vennlige SVG-elementer: ingen CSS, markers, filtre eller foreignObject."""
import os

W, H = 1920, 1080
FONT = "Open Sans, Segoe UI, Arial, sans-serif"

# Palett (fra SSB-palettvedlegget)
C = dict(
    ink="#1e3a3f", dark="#274246", grey="#5e787a", line="#cdd3d4",
    teal="#c4dddb", tealp="#eff8fa",
    green="#00824d", greenl="#b6e9b8", greenp="#ecfeed",
    purple="#7d5fea", purplel="#c3baff", purplep="#f1f1fe",
    white="#ffffff",
)
PURPLE_TXT = "#4b2fb0"  # mørk lilla for tekst på lys lilla (kontrast)
DIM = dict(fill="#f5f7f7", stroke="#dfe5e5", text="#b9c5c6")

# ---------- rammeverk ----------
class Fig:
    def __init__(self, hi=None):
        self.hi = hi  # None = alt i farger (oversikt); ellers sett av aktive id-er
        self.o = []

    def on(self, gid):
        return self.hi is None or gid == "_" or gid in self.hi

    def add(self, s):
        self.o.append(s)

    def col(self, gid, key, color):
        if self.on(gid):
            return color
        return DIM[key]

    # primitive
    def rect(self, gid, x, y, w, h, fill, stroke, sw=2, rx=10, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                 f'fill="{self.col(gid,"fill",fill)}" stroke="{self.col(gid,"stroke",stroke)}" stroke-width="{sw}"{d}/>')

    def text(self, gid, x, y, s, size=22, color=None, weight=400, anchor="start", italic=False):
        color = color or C["ink"]
        st = ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
                 f'fill="{self.col(gid,"text",color)}" text-anchor="{anchor}"{st}>{esc(s)}</text>')

    def lines(self, gid, x, y, rows, size=20, color=None, weight=400, anchor="start", lh=None):
        lh = lh or round(size * 1.3)
        for i, r in enumerate(rows):
            self.text(gid, x, y + i * lh, r, size, color, weight, anchor)

    def arrow(self, gid, pts, color, sw=3, dash=None, head=True, hs=13):
        c = self.col(gid, "stroke", color)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{x},{y}" for x, y in pts)
        # kort ned siste segment så linjen ikke stikker gjennom pilspissen
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        import math
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        if head:
            pts2 = pts[:-1] + [(x2 - ux * hs * 0.8, y2 - uy * hs * 0.8)]
            p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts2)
        self.add(f'<polyline points="{p}" fill="none" stroke="{c}" stroke-width="{sw}" '
                 f'stroke-linejoin="round" stroke-linecap="round"{d}/>')
        if head:
            px, py = -uy, ux
            a = (x2, y2)
            b = (x2 - ux * hs * 1.5 + px * hs * 0.7, y2 - uy * hs * 1.5 + py * hs * 0.7)
            e = (x2 - ux * hs * 1.5 - px * hs * 0.7, y2 - uy * hs * 1.5 - py * hs * 0.7)
            self.add(f'<polygon points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {e[0]:.1f},{e[1]:.1f}" fill="{c}"/>')

    def person(self, gid, cx, cy, s=1.0, color=None):
        c = self.col(gid, "stroke", color or C["dark"])
        r = 15 * s
        self.add(f'<circle cx="{cx}" cy="{cy-22*s}" r="{r}" fill="{c}"/>')
        self.add(f'<path d="M{cx-27*s},{cy+28*s} C{cx-27*s},{cy-2*s} {cx-16*s},{cy-4*s} {cx},{cy-4*s} '
                 f'C{cx+16*s},{cy-4*s} {cx+27*s},{cy-2*s} {cx+27*s},{cy+28*s} Z" fill="{c}"/>')

    def cyl(self, gid, x, y, w, h, fill, stroke, sw=2):
        f, s = self.col(gid, "fill", fill), self.col(gid, "stroke", stroke)
        ry = 14
        self.add(f'<path d="M{x},{y+ry} L{x},{y+h-ry} A{w/2},{ry} 0 0 0 {x+w},{y+h-ry} L{x+w},{y+ry}" '
                 f'fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
        self.add(f'<ellipse cx="{x+w/2}" cy="{y+ry}" rx="{w/2}" ry="{ry}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')

    def lock(self, gid, x, y, color=None):
        c = self.col(gid, "stroke", color or C["dark"])
        self.add(f'<path d="M{x+5},{y+12} L{x+5},{y+7} A7,7 0 0 1 {x+19},{y+7} L{x+19},{y+12}" fill="none" stroke="{c}" stroke-width="3"/>')
        self.add(f'<rect x="{x}" y="{y+12}" width="24" height="18" rx="3" fill="{c}"/>')

    def badge(self, x, y, n):
        self.add(f'<circle cx="{x}" cy="{y}" r="19" fill="{C["ink"]}" stroke="{C["white"]}" stroke-width="3"/>')
        self.add(f'<text x="{x}" y="{y+8}" font-family="{FONT}" font-size="22" font-weight="700" '
                 f'fill="{C["white"]}" text-anchor="middle">{n}</text>')

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
                + "\n".join(self.o) + "\n</svg>\n")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


