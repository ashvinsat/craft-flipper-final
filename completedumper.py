# pylint: disable-all

import os
from dumprecipes import DumpToFile

file = open("craftingrecipes.json", 'w')
file.write("[")
file.close()
directory = os.fsencode("circumcised items")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(filename)
        itemnamestring = f.decode('ASCII')
        unused, name = itemnamestring.split("/")
        name, unused = name.split(".")
        DumpToFile(name)

file = open("craftingrecipes.json", 'a')
file.write("]")


"""
list of weird cases:
1. some items like emerald have trades https://discord.com/channels/@me/1112917933593743370/1126578877611917464
2. some items like gold/iron ingots have backwards and forwards recipes that are the same and cause issues with the amount of items
    potential fix is: if recipe[j] 
3. some rift items are effectively soulbound but dont have the indicator in the lore (agaricus chum cap)

"""