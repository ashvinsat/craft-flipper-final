#pylint: disable-all
import os
import copy
import json

def GetDict(tag):
    #open the file for the item
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, 'circumcised items', tag + '.json')
    file = open(filePath)
    data = json.load(file)
    recipe = {}
    """
    factors:
        being an enchanted book
        iron block to ingot redundancy
        recipes having a "count"

    ideas:
        have each time it gets a recipe return a boolean value to determine if there are more items to go <<<biggest thing        
    """