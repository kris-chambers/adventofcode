calibrationDocument = []
listOfInts = []
inputFile = open("2023\day01input.txt", "r")
validDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight"
               "nine"]

def createListFromFile(listName, fileName):   
    for line in fileName:
        listName.append(line)
    fileName.close()
    
def removeNonInts():
    for i in calibrationDocument:
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
            
                       
    
createListFromFile(calibrationDocument, inputFile)
removeNonInts()
makeTwoDigitsAndSum()