calibrationDocument = []
listOfInts = []
newList = []
inputFile = open("day01input.txt", "r")
validDigits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def createListFromFile():   
    for line in inputFile:
        calibrationDocument.append(line)
    inputFile.close()
    
def convertWordstoNums():
    for i, j in validDigits.items():
        for item in calibrationDocument:
            convert = item.replace(i, j)
            newList.append(convert)

    

def removeNonInts():
    for i in newList:
        ints = []
        for character in i:
            if character.isdigit():
                ints.append(character)
        listOfInts.append(ints)

def makeTwoDigitsAndSum():
    total = 0
    for i in listOfInts:
        if len(i) > 1:
            twoDigitNum = i[0] + i[-1]
            total = total + int(twoDigitNum)
        else:
            twoDigitNum = i[0] + i[0]
            total = total + int(twoDigitNum)
    print(f"The sum of all of the calibration values is {total}.")       
            
                       
    
createListFromFile()
convertWordstoNums()
removeNonInts()
makeTwoDigitsAndSum()