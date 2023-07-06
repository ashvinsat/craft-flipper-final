import os
import json
trimmeditemsfolder = "itemdeletertest7"
directory = os.fsencode(trimmeditemsfolder)
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        itemfilepath = f.decode('ASCII')
        try:
            fileplaceholder = open(f'{itemfilepath}', encoding="utf-8")
            iteminfo = json.load(fileplaceholder)
            itemid=iteminfo["internalname"]
            for key in list(iteminfo):
                if key not in ["displayname", "recipe", "internalname", "crafttext"]:
                    del iteminfo[key]
            with open(f"{trimmeditemsfolder}/{itemid}.json", "w") as file:
                json.dump(iteminfo, file, indent = 3)
        finally:
            fileplaceholder.close