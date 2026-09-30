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

## Presentasjonssekvens: Spørsmål → Konsept → Oversikt → Fokus

*Status: til utprøving (pilot: Orientering × Ansvar og tilgang, september 2026).*

En oversiktsfigur som er riktig, kan likevel være for mye å ta inn på én gang. Første visning av tilgangsfiguren for SCB-ledere ga reaksjonen «Oj, dette var mye informasjon»: for mange elementer, for mye tekst og uklart hvor man skal begynne å lese. Løsningen er ikke å fjerne innhold fra oversikten eller å skyve det over i fokusbildene. Løsningen er å forberede seeren på oversikten.

| Bilde | Oppgave | Innhold |
| --- | --- | --- |
| **Spørsmål** | Vekke nysgjerrighet og vise hvor svarene kommer | Hovedspørsmålet som tittel. 3–5 nummererte spørsmål plassert der svaret står i oversikten. Svake, stiplede konturer av oversiktens soner. Panelet viser tomme, nummererte plassholdere. |
| **Konsept** | Gi den ene ideen og vise hvordan oversikten skal leses | Svaret som tittel. Høyst 6–8 elementer, direkte merket. Én visuell idé (kontrast, bevegelse eller rom i rommet). Panelet gir regelen i stor skrift og korte svar med samme nummer. |
| **Oversikt** | Vise helheten | Uendret grunnfigur. |
| **Fokus 1..N** | Gå i dybden | Uendret praksis: framheving og nedtoning. |

Regler:

1. **Samme geometri i alle bildene.** Sonene ligger på samme sted fra spørsmål til fokus. Gi objektene samme navn i PowerPoint, så kan Morph animere overgangene.
2. **Nummereringen går gjennom hele sekvensen.** Spørsmål 1 besvares i panelets punkt 1 og peker på samme sted i oversikten.
3. **Spørsmålsfoilen svarer ikke.** Den lover svar og viser plassen de kommer på.
4. **Konseptfoilen er ikke en nedskalert oversikt.** Den viser mekanismen, ikke en forkortet liste. Test: kan seeren forklare hovedpoenget med egne ord etter fem sekunder?
5. **Forenklet tegnforklaring.** Spørsmål og konsept viser bare de 2–3 grunnbegrepene («Tre ting å holde øye med»). Full tegnforklaring kommer i oversikten.
6. **Forenkling skal ikke bli feil.** Det konseptet utelater (for eksempel tidsavgrenset tilgang til kildedata), skal vises i et fokusbilde.
7. **Bruk sekvensen for målgrupper som ser figuren for første gang,** særlig Orientering. For vante brukere er oversikten ofte nok.

Stegvis visning på nett: `nettside/bygg.py` lager en side der stegene glir over i hverandre (se README).

Komponenter: `konseptfigurer/sekvens.py` (`topp`, `sone`, `sporsmal`, `plassholderpanel`, `svarpanel`, `grunnbegreper`). Mal: `figurer/_mal/sekvens.py` med `sekvens.json`.

Åpne spørsmål i utprøvingen:

- Hvilken konseptform virker best: nedskalert oversikt med korte svar (variant A) eller én kontrast (variant B)? Begge finnes for tilgangsfiguren.
- Trengs spørsmålsfoilen hver gang, eller bare når oversikten er tett?
- Filnavn: `00-sporsmal` og `01-konsept` sorteres etter `0-oversikt`. Rekkefølgen står derfor i registeret.

## Formfaktor (1920 × 1080)

| Element | Plassering |
| --- | --- |
| Tittel | x 60, y 92, 46 px, fet |
| Undertittel | x 60, y 136, 24 px |
| Etikett | øverst til høyre: Spørsmål, Konsept, Oversikt, Fokus n av m, Diskusjon, Scenario (+ INTERN / FORSLAG ved behov) |
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
5. Tegn spørsmåls- og konseptfoil på oversiktens geometri, når målgruppen ser figuren for første gang.
6. Introduksjonsfoil med matrisen og status.
7. Test på én person fra målgruppen som ikke har sett figuren. Juster.
8. Kvalitetssikring med faglige eiere via pull request.
