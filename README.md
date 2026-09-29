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
| `konseptfigurer/` | Felles byggeklosser: `fig.py` (palett, former, fokus og nedtoning), `komponenter.py` (ramme, panel, tegnforklaring, flate, brikke, status), `sti.py` |
| `figurer/<serie>/` | Én mappe per tema. Skriptene tegner serien. |
| `figurer/_mal/` | Mal for nye figurer: innhold i JSON, tegning i kode. Start her. |
| `register/` | Figurregister, begrepsliste og kvalitetssikringsliste per serie |
| `docs/` | `standard.md` (metoden og formfaktoren) og `adr-utkast.md` |
| `utdata/<serie>/` | Ferdige SVG-er. Sjekkes inn, slik at de kan hentes direkte. |
| `verktoy/` | `forhandsvis.js` lager PNG-er med riktig font |

## Serier

- **dapla** – 39 figurer: målgruppe × perspektiv (Orientering, Bruk, Teknisk × Kapabilitet, Prosess og flyt, Struktur, Ansvar og tilgang) + introduksjon.
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
