#pylint: disable-all
import os
import copy
import json

def GetDict(tag):
    #open the file for the item
    dictionary, cont = RecipeMaker(tag)
    ny = list(RecipeMakerMultilayer(dictionary))
    truth = True
    nr = {}
    ny[0] = truth
    ny[1] = nr
    while truth:
        try:
            nr = RecipeMakerMultilayer(nr)
        except:
            return nr


def RecipeMaker(tag):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, 'items backup', tag + '.json')
    file = open(filePath)
    data = json.load(file)
    cont = True
    recipe = {}
    try:
        if "Enchanted Book" not in data['displayname']:
            for j in data['recipe'].values():
                cont = True
                try:
                    key, value = j.split(':')
                    if key in recipe:
                        recipe[key] += int(value)
                    else:
                        recipe[key] = int(value)
                    potentialIngotName, bleh = tag.split("_")
                    if key == f"{potentialIngotName}_BLOCK": #iron block to ingot redundancy
                        cont = False
                except:
                    pass
                if cont!=False:
                    if j == '':
                        pass
                    elif type(j) is int:
                        recipe['count'] == int(data['recipe']['count'])
    except:    
        pass
    file.close()
    return recipe, cont
   
def RecipeMakerMultilayer(oldDict):
    newrecipe = copy.deepcopy(oldDict)
    cont = True
    for i in oldDict.keys():
        count = 0
        try:
            scriptDir = os.path.dirname(os.path.abspath(__file__))
            filePath = os.path.join(scriptDir, 'items backup', i + '.json')
            file = open(filePath)
            data = json.load(file)
            if "Enchanted Book" not in data['displayname']:
                try:
                    for j in data['recipe'].values():
                        if j == '':
                            count+=1
                            pass
                        elif j == 'count':
                            newrecipe[j] = int(data['recipe'][j])
                        else: 
                            key, value = j.split(':')
                            potentialIngotName, bleh = tag.split("_")
                            if key == f"{potentialIngotName}_BLOCK": #iron block to ingot redundancy
                                cont +=1
                                pass

                            elif key in newrecipe:
                                newrecipe[key] += int(value) * oldDict[i]
                                #but some day make it so that if that value goes over 160 u can just leave it as the previous form
                            else:
                                newrecipe[key] = int(value) * oldDict[i]
                    del newrecipe[i]

                except:
                    count+=1
            else:
                pass
            
        except:
            pass
        
        if count == 9:
            cont = False
        file.close()
        return cont, newrecipe


print(GetDict("FLORID_ZOMBIE_SWORD"))



# """
#     factors:
#         being an enchanted book
#         iron block to ingot redundancy
#         recipes having a "count"
#     ideas:
#         have each time it gets a recipe return a boolean value to determine if there are more items to go <<<biggest thing 
        
# """