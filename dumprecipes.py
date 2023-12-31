# pylint: disable-all
import copy
import requests
import json
import os

# bz = requests.get('https://sky.shiiyu.moe/api/v2/bazaar').json()

# # make the file
    
# def GetDict(tag):
#     #open the file for the item
#     scriptDir = os.path.dirname(os.path.abspath(__file__))
#     filePath = os.path.join(scriptDir, 'circumcised items', tag + '.json')
#     file = open(filePath)
#     data = json.load(file)
#     recipe = {}
#     #find the recipe
#     if "Enchanted Book" not in data['displayname']:
#         for i in data['recipe'].values():
#             if i == '':
#                 pass
#             elif type(i) is int:
#                     recipe["count"] = int(data['recipe']["count"]) #make sure it pulls from the full item list
#             else: 
#                 key, value = i.split(':')
#                 if key in recipe:
#                     recipe[key] += int(value)
#                 else:
#                     recipe[key] = int(value)
#     else:
#                 pass
#     #lol find a better automated solution for this eventually that terminates once there isnt anything left
    
#     recipe, bol = MultilayeredRecipe(recipe)
#     while bol == True:
#          recipe, bol = MultilayeredRecipe(recipe)
#     # re2 = MultilayeredRecipe(re1)
#     # re3 = MultilayeredRecipe(re2)
#     # re4 = MultilayeredRecipe(re3)
#     # re5 = MultilayeredRecipe(re4)
#     # re6 = MultilayeredRecipe(re5)
#     # re7 = MultilayeredRecipe(re6)
#     # re8 = MultilayeredRecipe(re7)
#     # re9 = MultilayeredRecipe(re8)
#     # # re10 = MultilayeredRecipe(re9)
#     # # re11 = MultilayeredRecipe(re10)
#     # # re12 = MultilayeredRecipe(re11)
#     # # re13 = MultilayeredRecipe(re12)
#     # # re14 = MultilayeredRecipe(re13)
#     # # re15 = MultilayeredRecipe(re14)
#     # # re16 = MultilayeredRecipe(re15)
    
#     # #create a dictionary that can be dumped into the bigger json
#     jsonableDict = {tag:recipe}
#     print(jsonableDict)
#     return jsonableDict
    

# def MultilayeredRecipe(oldDict):
#     newrecipe = copy.deepcopy(oldDict)
#     hasRecipe = True
#     for i in oldDict.keys():
#         try:
#             scriptDir = os.path.dirname(os.path.abspath(__file__))
#             filePath = os.path.join(scriptDir, 'items backup', i + '.json')
#             file = open(filePath)
#             data = json.load(file)
#             if "Enchanted Book" not in data['displayname']:
#                 try:
#                     for j in data['recipe'].values():
#                         if j == '':
#                             pass
#                         elif type(i) is int:
#                             newrecipe["count"] = int(data['recipe']["count"]) #make sure it pulls from the full item list
#                         else: 
#                             key, value = j.split(':')
#                             if key in newrecipe:
#                                 newrecipe[key] += int(value) * oldDict[i]
#                                 #but some day make it so that if that value goes over 160 u can just leave it as the previous form
#                             else:
#                                 newrecipe[key] = int(value) * oldDict[i]
#                 except KeyError:
#                      hasRecipe = False
#             else:
#                 pass
#             del newrecipe[i]
        
#             file.close()
#         except FileNotFoundError:
#                 pass
#     return(newrecipe), hasRecipe

# def DumpToFile(tag):
#     dumpy = GetDict(tag)
#     with open("craftingrecipes.json", 'a') as f:
#         json.dump(dumpy, f, indent=4)
#         f.write(",")

# DumpToFile("FLORID_ZOMBIE_SWORD")

# pylint: disable-all
import copy
import requests
import json
import os

#bz = requests.get('https://sky.shiiyu.moe/api/v2/bazaar').json()

# make the file
    
def GetDict(tag):
    #open the file for the item
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, 'items backup', tag + '.json')
    file = open(filePath)
    data = json.load(file)
    recipe = {}
    #find the recipe
    if "Enchanted Book" not in data['displayname']:
        
        for i in data['recipe'].values():
            if i == '':
                pass
            elif type(i) is int:
                    recipe["count"] = int(data['recipe']["count"]) #make sure it pulls from the full item list
            else: 
                key, value = i.split(':')
                if key in recipe:
                    recipe[key] += int(value)
                else:
                    recipe[key] = int(value)
    else:
                pass
    #lol find a better automated solution for this eventually that terminates once there isnt anything left
    re1 = MultilayeredRecipe(recipe)
    re2 = MultilayeredRecipe(re1)
    re3 = MultilayeredRecipe(re2)
    re4 = MultilayeredRecipe(re3)
    re5 = MultilayeredRecipe(re4)
    re6 = MultilayeredRecipe(re5)
    re7 = MultilayeredRecipe(re6)
    re8 = MultilayeredRecipe(re7)
    re9 = MultilayeredRecipe(re8)
    #create a dictionary that can be dumped into the bigger json
    jsonableDict = {tag:re9}
    return jsonableDict

def MultilayeredRecipe(oldDict):
    newrecipe = copy.deepcopy(oldDict)
    for i in oldDict.keys():
        try:
            scriptDir = os.path.dirname(os.path.abspath(__file__))
            filePath = os.path.join(scriptDir, 'items backup', i + '.json')
            file = open(filePath)
            data = json.load(file)
            if "Enchanted Book" not in data['displayname'] and data['recipe'].bal:
                for j in data['recipe'].values():
                    if j == '':
                        pass
                    elif j == 'count':
                        newrecipe[j] = int(data['recipe'][j])
                    else: 
                        key, value = j.split(':')
                        if key in newrecipe:
                            newrecipe[key] += int(value) * oldDict[i]
                            #but some day make it so that if that value goes over 160 u can just leave it as the previous form
                        else:
                            newrecipe[key] = int(value) * oldDict[i]
            else:
                pass
            del newrecipe[i]
        
            file.close()
        except FileNotFoundError:
                pass
    return(newrecipe)

def DumpToFile(tag):
    dumpy = GetDict(tag)
    with open("craftingrecipes.json", 'a') as f:
        json.dump(dumpy, f, indent=4)
        f.write(",")

DumpToFile("FLORID_ZOMBIE_SWORD")