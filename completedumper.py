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
