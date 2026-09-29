# Standard for konseptfigurer

Gjelder figurer som forklarer arkitektur, dataflyt, prosess, ansvar, kapabiliteter og strategiske valg.

## Innholdsprinsipper

1. **Én figur, ett spørsmål, én primær målgruppe.** Tittelen er svaret eller spørsmålet, undertittelen sier hva figuren forklarer.
2. **Figurer planlegges i en matrise:** målgruppe × perspektiv. Tomme celler er bevisste.
3. **Oversikt og fokus.** Hver celle har én grunnfigur. Fokusvarianter framhever deler av den og toner ned resten. Elementer flytter seg ikke mellom variantene.
4. **Status skal synes, og gjettes aldri.** Fire verdier: finnes i dag, under arbeid, forslag, uavklart. Det som ikke er bekreftet, tegnes stiplet.
5. **Ingen nye navn** på noe som allerede har et navn. Bruk begrepslisten i `register/`.
6. **Normative figurer merkes** «Diskusjon» eller «Scenario», ikke «Oversikt».
7. **Skill typer ting visuelt:** flate/tjeneste, data/innhold, rolle/ansvar, utenfor/uavklart.
8. **Piler har én betydning hver**, og betydningen står i tegnforklaringen.
9. **Ikke tegn én sømløs reise** hvis det skjuler faglige, juridiske eller organisatoriske skiller.

## Formfaktor (1920 × 1080)

| Element | Plassering |
| --- | --- |
| Tittel | x 60, y 92, 46 px, fet |
| Undertittel | x 60, y 136, 24 px |
| Etikett | øverst til høyre: Oversikt, Fokus n av m, Diskusjon, Scenario (+ INTERN / FORSLAG ved behov) |
| Diagramflate | x 60–1400, y 180–986 |
| Forklaringspanel | x 1440–1860, 3–5 nummererte punkter |
| Tegnforklaring | nederst til venstre, y 1046 |
| Bunnlinje | nederst til høyre: dato · status · kilde |

Minste tekst: 12 px i brikker, 14 px ellers. Font: Open Sans.

## Palett og betydning

| Farge | Hex | Betydning |
| --- | --- | --- |
| Mørk blågrønn | `#274246` | tekst, overskrifter, flater (strek) |
| Lys blågrønn | `#eff8fa` / `#c4dddb` | plattform, tjenester, flater |
| Grønn | `#00824d` / `#b6e9b8` / `#ecfeed` | data, statistikk, metadata |
| Lilla | `#7d5fea` / `#c3baff` / `#f1f1fe` | brukere, roller, team, ansvar, eierskap |
| Grå | `#5e787a` / `#b9c5c6` / `#f3f5f5` | uavklart, utenfor scope, utenfor SSB |

Stiplet grå = uavklart eller ikke bekreftet. Stiplet lilla = forslag eller målbilde.

## SVG-regler for PowerPoint

Bare enkle elementer: `rect`, `line`, `polyline`, `polygon`, `circle`, `ellipse`, `path`, `text`. Ingen CSS-klasser, filtre, markører eller `foreignObject`. Pilspisser tegnes som polygoner.

## Faktadisiplin

- Sjekk påstander mot primærkilder (manualer, ADR-er, vedtak) før tegning. Noter ADR-status (foreslått/vedtatt).
- Lag en liste over det som må kvalitetssikres, og legg den i registeret.
- Skill mellom bekreftet, tolkning og forslag i både figur og følgetekst.

## Arbeidsflyt

1. Kritisk gjennomgang av eksisterende figurer: nivå, begreper, overlapp, status.
2. Matrise og storyboard: spørsmål, målgruppe, budskap, diagramtype, uavklart, fokusvarianter.
3. Faktagrunnlag: kilder og hull.
4. Tegn oversikten, se på forhåndsvisningen, rett, og tegn deretter fokusvariantene.
5. Introduksjonsfoil med matrisen og status.
6. Kvalitetssikring med faglige eiere via pull request.
