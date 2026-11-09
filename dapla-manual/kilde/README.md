# Kildekode

Figurene lages med Python. `lib.py` har komponentene (bokser, bøtter, piler, markører, tegnforklaring), og hver `mNN_*.py` tegner én figur.

## Bygge alle figurene

Krever Python 3, Pillow, `rsvg-convert` (librsvg) og fontene Open Sans og Roboto i `~/.fonts/OpenSans.ttf` og `~/.fonts/Roboto.ttf` (variable fonter fra Google Fonts). De brukes til å måle tekstbredde.

```bash
cd kilde
python3 build.py        # skriver SVG til out/ og PNG til out/png/
```

Kopier deretter filene til `../figurer/` og `../png/`.

## Regler koden følger

- viewBox 1000 px bred, minste tekst 16 px.
- Profil: fet tekst blir Roboto, resten Open Sans. 2 px hjørner (piller unntatt), 1 px rammer, 2 px piler. Se `rect()` og `C` i `lib.py`.
- Bare `rect`, `line`, `polyline`, `polygon`, `circle`, `ellipse`, `path` og `text`. Farger som attributter.
- Hver piltype og farge har én betydning. Se `Fig.LEG` og `KIND` i `lib.py`.
