# Kvalitetssikring

Til faglige eiere av Dapla-manualen. Tilbake til [README](README.md).


Manualen er brukt som fasit. Der manualen motsier seg selv, har jeg valgt det som står på flest steder, og markert det her.

## A. Avvik internt i manualen

| # | Side | Avvik | Valgt i figuren |
|---|---|---|---|
| A1 | Datatilstander | Utdata «lagres i bøtten `ssb-<teamnavn>-data-produkt-produkt`». Trolig skrivefeil for `…-produkt-prod`. | produkt |
| A2 | Hva er Dapla-team? / Features | Teamsiden sier at det «foreløpig kun» finnes tre features. Features-siden lister fem: dapla-buckets, kildomaten, transfer-service, shared-buckets og delomaten. | Fire features som kan skrus på (dapla-buckets er grunnpakken) |
| A3 | Hva er Dapla-team? / Kildomaten | Teamsiden omtaler Kildomaten som noe teamet skrur på selv. Kildomaten-siden sier at alle statistikkteam har den på i prod som standard. | Vist som feature. Bør avklares |
| A4 | Deling av data | sharedWith «gir … lesetilgang», men eksempelet sier «lese- og skrivetilgang» til play-obr-b. | Lesetilgang |
| A5 | Transfer Service / Overgang | Prosjektnavnet skrives `prisstat-produkt-p` på Transfer Service-siden, men `prisstat-p` på overgangssiden. Navnestrukturen sier `<team>-p`. | `<team>-p` |
| A6 | Altinn 3: Oversikt | Én setning sier at data synkroniseres «til sin delt-bøtte». Resten av siden sier kildebøtte. | Kildebøtte |
| A7 | Data Collector | Siden ber deg kontakte team Datafangsttjenester, men sier også at team Statistikktjenester setter opp instansen. | Ikke vist i figuren |
| A8 | Overgang | Cloud_sync-stien er `ssb/cloud_sync/<team>/standard/tilsky/`. Den gamle Transfer Service-figuren viser også en kilde-mappe. | Forenklet til `/ssb/cloud_sync/‹team›/…/tilsky/` |
| A9 | Datatilstander | Setningen om at statistikkdata ikke er obligatorisk står to ganger, den ene med feil syntaks. | Ingen betydning for figuren |

## B. Avvik mellom foilserien fra september og manualen

Jeg har bare sett foilene i lav oppløsning, så listen er ikke uttømmende.

| # | Foil | Avvik | Valgt i figuren |
|---|---|---|---|
| B1 | 9–13, 15, 38 | Foilene bruker «SSB Dataportal». Manualen sier at en datakatalog «etter hvert» skal implementeres. | Datakatalog, merket planlagt |
| B2 | 9–13 | Teamfiguren viser ikke at teamet har både test- og prodmiljø, eller at tilsky og frasky bare finnes i prod. | Begge miljøer vist (M01) |
| B3 | 35, 36, 45–49 | Forslag som Invoker og Runner-SA og en ny jobbarkitektur finnes ikke i manualen. | Holdt utenfor |
| B4 | 29–49 | Alt som er merket INTERN er holdt utenfor, fordi manualen er åpen på internett. | – |

## C. Mine tolkninger som bør bekreftes

| # | Figur | Tolkning |
|---|---|---|
| C1 | M02 | Manualen sier ikke hvilken identitet Kildomaten kjører som. Figuren sier bare at den kjører automatisk, slik at færre trenger tilgang. |
| C2 | M02 | At data-admins godkjenner PR-er i IaC-repoet generelt, bygger på deling av data, features og Kildomaten. Det står ikke samlet ett sted. |
| C3 | M06 | Data Collector er tegnet som et alternativ til teamets egen kode for API-er. Manualen beskriver ikke at Data Collector bruker Maskinporten Guardian. |
| C4 | M06 | At inndata bør lagres som parquet før overføring fra bakke, står i overgangssiden. Det gjelder ikke kildedata. |
| C5 | M10 | URL-en til testmiljøet i Dapla Lab er utelatt. Manualen nevner den, men teksten var avkortet der jeg leste. |
| C6 | M12 | «For eksempel fra xml til et annet format» forenkler en fotnote om konvertering fra xml. |
| C7 | M11 | «Ett team per gruppe som jobber med de samme dataene» er min forkortelse av manualens avsnitt om teamstruktur. |
| C8 | M13 | At katalogen er felles for alle team, men at hvert team bare ser sine egne tabeller, bygger på «sentral katalog på Dapla» og «liste ut alle tabeller som tilhører teamet». Hvordan teamene er skilt i katalogen (for eksempel ett skjema per team) står ikke i manualen. |
| C9 | M13 | Figuren sier ikke hvor endringsloggen (get_edits) lagres. Manualen er uklar: «slette editeringshistorikk og filene i teamets bøtte», men cleanup=False beholder «editeringshistorikk og selve datafilene i produktbøtta». |
| C10 | M13 | Sikkerhetskopien er tegnet som en pil til teamets produktbøtte. Manualen sier at standardstien er `{data_path}/catalog-export`, men ikke hva data_path er. |
| C11 | M13 | Små endringer kan ligge «inlinet» i katalogen til de flushes til Parquet. Det er utelatt for å holde hovedbudskapet rent: data i bøtta, metadata i katalogen. |
| C12 | M13 | At de grafiske grensesnittene (Parqueditor, Editeringsrammeverket, egne apper) går gjennom Python-pakken, er en forenkling. Manualen sier bare at de bruker Parquedit som lagringsløsning. |

## D. Navn brukt i figurene (begrepsliste)

Dapla-team, Teamansvarlig, developers, data-admins, JIT-tilgang, prodmiljø, testmiljø, kildeprosjekt, standardprosjekt, kildebøtta, produktbøtta, tilsky, frasky, delt-bøtte (standard, delomat), IaC-repo, feature, Atlantis, Kildomaten, Delomaten, Transfer Service, bakke, sky, Dapla Lab, tjenestekatalog, tjenestekonfigurasjon, Mine tjenester, Datadoc, Vardef, Klass, variabelforekomst, datakatalog, Team SU-V, skjema, periode, pulje, utsending, Maskinporten, Maskinporten Guardian, M2M-teamet, Keycloak, Secret Manager, Samarbeidsportalen, MoveIT, Cloud_sync, Parquedit, ssb-parquedit, Parqueditor, Parquedit-tabell, DuckLake, sentral katalog, Editeringsrammeverket.
