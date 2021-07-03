import os
path = 'xyz'
fileName = os.listdir(path)
def stripName(name,path):
    counter = 0
    for partName in name:
        usableName = partName.split('_')[0]
        currentName = path + partName
        newName = path + usableName + str(counter) + '.jpg'
        os.rename(currentName,newName)
        counter += 1

stripName(fileName,path)
