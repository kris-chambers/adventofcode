inputFile = open("day02input.txt", "r")
listOfGames = []
bagContents = {"red": 12, "green": 13, "blue": 14}

def createListFromFile(listName, fileName):
    for line in fileName:
        listName.append(line)
    fileName.close()
#    print(listName)
    
def listToDict(listName, dictName):
    for game in listName:
        

createListFromFile(listOfGames, inputFile)
print(listOfGames[0])
print(type(listOfGames[0]))