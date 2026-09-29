# ADR-utkast: Standard for konseptfigurer

- Status: utkast
- Myndighet: Seksjon for IT-arkitektur (forslag)
- Dato: 2026-09-29

## Kontekst og problemstilling

SSB bruker mange figurer for å forklare Dapla, metadata og formidling. De er laget av ulike personer, blander nivåer og målgrupper, bruker ulike navn på samme ting og viser sjelden hva som finnes i dag og hva som er målbilde. Resultatet er figurer som skaper nye spørsmål i stedet for å avklare.

## Beslutningsdrivere

- Figurer skal kunne brukes i beslutninger uten å villede.
- Samme begreper og farger på tvers av fagmiljøer.
- Endringer i innhold skal være enkle, sporbare og kvalitetssikret.
- Figurene skal kunne brukes direkte i PowerPoint.

## Vurderte løsninger

1. Felles PowerPoint-maler.
2. Felles metode og komponentbibliotek i kode, med figurer som SVG (`ssb-konseptfigurer`).
3. Status quo.

## Beslutning (foreslått)

Løsning 2. Figurer lages etter `docs/standard.md`, med innhold i data og form i felles komponenter, versjonert i Git og kvalitetssikret via pull request.

## Konsekvenser

- Positive: konsistens, sporbarhet, raske endringer, fokusvarianter uten omtegning, tydelig status.
- Negative: krever litt kodekompetanse for nye figurtyper. Redigering i PowerPoint er mulig, men endringer bør føres tilbake til kilden.
