# Bygg alle figurer til utdata/<serie>/ og lag PNG-forhåndsvisning.
PY := PYTHONPATH=$(CURDIR) python3

.PHONY: alle dapla faktaformidling mal nettside forhandsvis zip rydd

alle: dapla faktaformidling mal

dapla:
	cd figurer/dapla && for f in orientering_tilgang_sporsmal orientering_tilgang_konsept orientering_tilgang_konsept_b orientering_tilgang orientering_kapabilitet teknisk_struktur teknisk_prosess teknisk_tilgang teknisk_kapabilitet bruk_prosess bruk_kapabilitet bruk_tilgang introduksjon; do $(PY) $$f.py || exit 1; done

faktaformidling:
	cd figurer/bedre-faktaformidling && $(PY) figurer.py

mal:
	$(PY) figurer/_mal/ny_figur.py
	$(PY) figurer/_mal/sekvens.py

# Stegvis visning (Spørsmål → Konsept → Oversikt → Fokus) til nettside/site/. Åpne nettside/site/index.html.
nettside:
	$(PY) nettside/bygg.py

forhandsvis:
	node verktoy/forhandsvis.js

zip:
	cd utdata && for d in */; do zip -qr "$${d%/}.zip" "$$d"; done

rydd:
	rm -rf utdata/* forhandsvisning nettside/site
