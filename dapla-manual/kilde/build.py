import importlib, glob, sys
mods = ["m01_team:m01","m02_tilgang:m02","m03_datatilstander:m03","m04_deling:m04","m05_kildomaten:m05",
        "m06_data_inn:m06","m07_maskinporten:m07","m08_git:m08","m09_metadata:m09","m10_dapla_lab:m10",
        "m11_overgang:m11","m12_altinn:m12"]
for m in mods:
    mod, fn = m.split(":")
    fig = getattr(importlib.import_module(mod), fn)()
    print(fig.save("out")[0], fig.h)
