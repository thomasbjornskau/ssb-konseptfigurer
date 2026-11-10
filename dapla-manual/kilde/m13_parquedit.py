from lib import *
import lib
lib.DATO = "10.11.2026"

def m13():
    f = Fig("m13-parquedit", 860)

    # 1 Grensesnitt i Dapla Lab
    f.zone(30, 16, 280, 448, "Dapla Lab", "plat", sub="startes som teamet")
    f.marker(306, 16, 1)
    clients = [("IDE", "Jupyter, VS Code, RStudio eller Marimo", 96),
               ("Grafisk grensesnitt", "Parqueditor, Editeringsrammeverket eller en egenutviklet app", 270)]
    mids = []
    for t, b, cy in clients:
        h = f.box(46, cy, 248, 120, "white", t, b, pad=12)
        mids.append(cy + h/2)

    # 2 ssb-parquedit
    ex, ew, ey0, ey1 = 340, 154, 96, 386
    ey1 = 390
    f.rect(ex, ey0, ew, ey1 - ey0, C["plat"], C["plat2"], 2, 8)
    f.text(ex + 12, ey0 + 30, "ssb-parquedit", 18, 700)
    f.para(ex + 12, ey0 + 58, "Python-pakke bygget på DuckLake. Holder data og metadata i takt", ew - 22, 16, 400,
           C["grey"])
    f.marker(ex + ew - 4, ey0, 2)
    for y in mids:
        f.ctrl([(294, y), (ex, y)], hs=9)

    # 3 Sentral katalog
    kx, kw = 580, 390
    f.zone(kx, 16, kw, 224, "Sentral katalog", "plat", sub="felles for alle team på Dapla")
    f.marker(kx + kw - 4, 16, 3)
    f.bucket(kx + 14, 66, 128, 146, "PostgreSQL", "DuckLake- katalog", "data", lsize=16)
    f.text(kx + 158, 86, "Metadata", 17, 700, C["green"])
    f.text(kx + 158, 112, ["Tabeller og kolonner", "Versjoner og tidspunkter", "Hvilke Parquet-filer",
                           "tabellen består av"], 16, 400, C["ink"], lh=22)
    f.para(kx + 158, 210, "Teamet ser sine egne tabeller", kw - 170, 16, 400, C["grey"])

    # 4 Teamets produktbøtte
    ty = 290
    f.zone(kx, ty, kw, 174, "Dapla-team «Skatt næring»", "role")
    f.marker(kx + kw - 4, ty, 4)
    f.bucket(kx + 14, ty + 40, 128, 120, "produkt", "teamets produktbøtte", "data", lsize=16)
    f.text(kx + 158, ty + 60, "Data", 17, 700, C["green"])
    f.text(kx + 158, ty + 86, ["Parquet-filer med selve", "innholdet i tabellene"], 16, 400, C["ink"], lh=22)
    f.para(kx + 158, ty + 134, "Midlertidig lagring mens dataene editeres manuelt", kw - 170, 16, 400, C["grey"])

    # Flyt mellom pakken og lagrene
    f.flow([(ex + ew, 150), (kx, 150)], start=True, hs=9)
    f.text((ex + ew + kx) / 2, 136, "metadata", 16, 400, C["grey"], "middle")
    f.flow([(ex + ew, 370), (kx, 370)], start=True, hs=9)
    f.text((ex + ew + kx) / 2, 356, "data", 16, 400, C["grey"], "middle")

    # 5 Sikkerhetskopi
    bx = kx + kw - 70
    f.backup([(bx, 240), (bx, ty)], hs=9)
    tx = bx - 16
    f.text(tx, 260, "export_catalog()", 16, 400, C["ink"], "end", family=MONO)
    f.text(tx, 280, "teamet må selv ta sikkerhetskopi", 16, 400, C["grey"], "end")
    f.marker(bx + 24, 265, 5)

    f.h = 464 + 36 + 92
    f.frame(["plat", "data", "role", ("ctrl", "Bruker Parquedit"), "flow", "backup", "marker"],
            "Parquedit · Parqueditor")
    return f

if __name__ == "__main__":
    print(m13().save("out"))
