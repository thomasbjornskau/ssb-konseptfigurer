# Register: Dapla

Utkast per 28.09.2026. Eier av innholdet: Dapla-produkteiere og plattformteamet (må bekreftes).

## Figurer

| Målgruppe × perspektiv | Skript | Filer | Status |
| --- | --- | --- | --- |
| Orientering × Ansvar og tilgang | `orientering_tilgang.py` | 1 + 4 fokus | Utkast (laget for SCB-innlegg) |
| Orientering × Kapabilitet | `orientering_kapabilitet.py` | 1 + 3 fokus | Utkast |
| Teknisk × Struktur | `teknisk_struktur.py` | 1 + 5 fokus, INTERN | Utkast, må kvalitetssikres |
| Teknisk × Prosess og flyt | `teknisk_prosess.py` | 4 figurer, INTERN | Utkast, forslag merket |
| Teknisk × Ansvar og tilgang | `teknisk_tilgang.py` | 1 + 4 fokus, INTERN | Utkast |
| Teknisk × Kapabilitet | `teknisk_kapabilitet.py` | 1 + 2 linser, INTERN | Utkast |
| Bruk × Prosess og flyt | `bruk_prosess.py` | 1 + 5 fokus | Utkast |
| Bruk × Kapabilitet | `bruk_kapabilitet.py` | 1 + 3 fokus | Utkast |
| Bruk × Ansvar og tilgang | `bruk_tilgang.py` | 1 | Utkast |
| Introduksjon (matrise) | `introduksjon.py` | 1 | Utkast |

Ikke tegnet: Orientering × Prosess, Orientering × Struktur (nyttige). Bruk × Struktur er vurdert som unødvendig.

## Begrepsliste (låste navn)

| Begrep | Merknad |
| --- | --- |
| Dapla-team | organisatorisk enhet som får tilgang; tilhører én seksjon |
| Kildeprosjekt · standardprosjekt | manualens navn. Tegning 6 brukte «produksjonsprosjekt» – avklar |
| Kildebøtte · produktbøtte · delt-bøtte | |
| Kildedata · inndata · klargjorte data · statistikk · utdata | SSBs datatilstander. Ikke «startdata» |
| Teamansvarlig · data-admins · developers | roller i teamet |
| Dapla Lab · Dapla Ctrl · Kildomaten · Delomaten | |
| SSB Dataportal | er dette det samme som «Datakatalog» i eldre figurer? Avklar |

## Kilder

Dapla-manualen (manual.dapla.ssb.no), ADR0015 (foreslått), ADR0017 (vedtatt 2023), ADR0023 (akseptert), ADR0026 (foreslått), notat «Orkestrering på Dapla» (forslag).

## Må kvalitetssikres

- [ ] Identitetskjeden: hvordan person → gruppe → IAM i GCP
- [ ] Hvor pseudonymiseringsnøklene ligger (ADR0015 er bare foreslått)
- [ ] Om Kildomaten kjører i teamets kildeprosjekt og med egen tjenestekonto (tolkning)
- [ ] Hvilke tjenester som kjører på NAIS
- [ ] Om ORDS-integrasjonen (ADR0017) fortsatt er i drift
- [ ] Om Klass følger samme mønster som metadatatjenestene i ADR0023
- [ ] Om Kubernetes under Onyxia er GKE
- [ ] Leveransevei til Statistikkbanken og Microdata
- [ ] «Etter inndata er alt manuelt i dag» – gjelder for alle team?
- [ ] Om Kildomaten-kode følger samme PR- og godkjenningsspor som IaC
- [ ] Om pseudonymisering alltid skjer i Kildomaten-steget
- [ ] Datadoc-krav for inndata (manualen nevner det ikke)
- [ ] Hvordan Altinn-innhenting settes opp, og av hvem
- [ ] Hvem som utpeker data-admins
- [ ] At tilgang forsvinner når man går ut av et team (formulering)
- [ ] Ressursvalg (CPU/minne) ved oppstart i Dapla Lab
- [ ] At Parquet er obligatorisk (fra godkjentlisten)
- [ ] Status på de ni kapabilitetene og formuleringen av de fire prinsippene
- [ ] Dataportal-punktet og «plattformteamet godkjenner ikke hver tilgang» i SCB-serien
