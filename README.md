# ssb-konseptfigurer

Konseptuelle figurer for SSB, laget som SVG i 16:9 (1920 × 1080) for presentasjoner og dokumenter.
Innholdet ligger i data, formen i felles komponenter. Da kan figurer rettes, versjoneres og kvalitetssikres som kode.

> Sjekk SSBs navnestandard for GitHub-repoer før repoet opprettes, og endre navnet om nødvendig.

## Kom i gang

```bash
make alle            # bygger alle serier til utdata/<serie>/
npm install          # første gang: Open Sans og Playwright for forhåndsvisning
npx playwright install chromium
make forhandsvis     # PNG-er i forhandsvisning/<serie>/ (ikke sjekket inn)
make zip             # én zip per serie i utdata/
```

Krever Python 3.10 eller nyere (bare standardbiblioteket) og Node 18 eller nyere for forhåndsvisning.

## Struktur

| Mappe | Innhold |
| --- | --- |
| `konseptfigurer/` | Felles byggeklosser: `fig.py` (palett, former, fokus og nedtoning), `komponenter.py` (ramme, panel, tegnforklaring, flate, brikke, status), `sekvens.py` (spørsmåls- og konseptfoil), `sti.py` |
| `figurer/<serie>/` | Én mappe per tema. Skriptene tegner serien. |
| `figurer/_mal/` | Maler: `ny_figur` (oversikt og fokus) og `sekvens` (spørsmål og konsept). Innhold i JSON, tegning i kode. Start her. |
| `register/` | Figurregister, begrepsliste og kvalitetssikringsliste per serie |
| `docs/` | `standard.md` (metoden og formfaktoren) og `adr-utkast.md` |
| `utdata/<serie>/` | Ferdige SVG-er. Sjekkes inn, slik at de kan hentes direkte. |
| `verktoy/` | `forhandsvis.js` lager PNG-er med riktig font |
| `nettside/` | Stegvis visning av sekvenser for GitHub Pages: `bygg.py`, `mal.html`, `forside.html`. Bygges til `nettside/site/` (ikke sjekket inn). |

## Fire typer bilder

En figurserie kan presenteres i fire steg: **Spørsmål → Konsept → Oversikt → Fokus**. Spørsmålsfoilen vekker nysgjerrighet og viser hvor svarene kommer. Konseptfoilen gir den ene ideen. Oversikten viser helheten, og fokusbildene går i dybden. Alle bruker samme geometri, så seeren kjenner seg igjen fra bilde til bilde. Metoden er til utprøving; se `docs/standard.md`.

## Nettside med stegvis visning

`make nettside` bygger én side per presentasjonssekvens til `nettside/site/`. Siden viser stegene etter hverandre med myke overganger: det som er likt fra bilde til bilde, blir stående; det som bare skifter farge (nedtoning i fokus), glir over; det nye tones inn. Det fungerer fordi alle bildene deler geometri, og krever ingen egen animasjonsmodell.

- Navigasjon: piltaster, mellomrom, klikk i bildet eller stegknappene. F gir fullskjerm. Adressen husker steg og konseptvariant (`?konsept=B#3`).
- Nye sekvenser legges til som en funksjon i `SEKVENSER` i `nettside/bygg.py`.
- Publisering: `.github/workflows/pages.yml` bygger og publiserer ved push til `main`. Engangsoppsett: *Settings → Pages → Source: GitHub Actions*.
- Bare `nettside/site/` publiseres. Legg ikke INTERN-figurer i en sekvens så lenge Pages-siden er offentlig.

## Serier

- **dapla** – 42 figurer: målgruppe × perspektiv (Orientering, Bruk, Teknisk × Kapabilitet, Prosess og flyt, Struktur, Ansvar og tilgang) + introduksjon. Orientering × Ansvar og tilgang har også spørsmåls- og konseptfoil (pilot).
- **bedre-faktaformidling** – introduksjon, F1–F12 og F2c.

## Arbeidsflyt

1. Endringer i innhold og nye figurer lages på egen gren.
2. Pull request med forhåndsvisning (CI legger PNG-ene ved som artefakt).
3. Gjennomgang av faglig eier av innholdet, i tillegg til figurforfatter.
4. Oppdater `register/<serie>.md`: status, dato og hva som er kvalitetssikret.

## Bruk i PowerPoint

Sett inn SVG, høyreklikk og velg «Konverter til figur» for å redigere. Fonten er Open Sans. Mangler den, faller PowerPoint tilbake til Segoe UI eller Arial.

## Merk

Tekniske Dapla-figurer er merket INTERN (jf. ADR0026 om eksponering av systemdetaljer). Vurder om repoet skal være internt.
Eksisterende serier er flyttet inn som skript. Nye figurer bør følge JSON-mønsteret i `figurer/_mal/`, og serier kan migreres gradvis.
