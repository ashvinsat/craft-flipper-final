# pylint: disable-all
import os 
import json 
from requests import get

bazitems = get("https://api.hypixel.net/skyblock/bazaar").json()

def VolumeBound(ItemID):
    auctionvolume = len(get(f"https://sky.coflnet.com/api/auctions/tag/{ItemID}/sold").json())
    try:
        if auctionvolume < 100:
            return True
        elif auctionvolume >= 100:
            return False
# in case item not on ah
    except TypeError:
        return True

def CheckingforSoulbound(lorelist):
    for line in lorelist:
        if "soulbound" in line.lower():
            return True
    return False

#change to name of folder vvvvvvvvvvv
directory = os.fsencode("itemdeletertest7")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        itemfilepath = f.decode('ASCII')
        itemid = os.path.splitext(os.path.basename(itemfilepath))[0]
        try:
            fileplaceholder = open(f'{itemfilepath}', encoding="utf-8")
            iteminfo = json.load(fileplaceholder)
            if "Enchanted Book" not in iteminfo["displayname"]:
                if "recipe" not in iteminfo:
                    fileplaceholder.close()
                    os.remove(itemfilepath)
                elif itemid not in bazitems["products"]:
                    if VolumeBound(itemid):
                        fileplaceholder.close()
                        os.remove(itemfilepath)
                    elif "_GENERATOR_" in itemfilepath:
                        fileplaceholder.close()
                        os.remove(itemfilepath)
                    elif CheckingforSoulbound(iteminfo["lore"]):
                        fileplaceholder.close()
                        os.remove(itemfilepath)
        finally:
            fileplaceholder.close()