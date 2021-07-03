import os
path = 'C:\\Users\\naman\\Downloads\\Wormhole\\base2\\'
fileName = os.listdir(path)
def stripName(name,path):
    counter = 0
    for partName in name:
        if partName[0] == 'a':
            usableName = 'aditi_budhathoki'
        else:
            usableName = 'urvisingh'
        currentName = path + partName
        newName = path + usableName + str(counter) + '.jpg'
        os.rename(currentName,newName)
        counter += 1

stripName(fileName,path)
