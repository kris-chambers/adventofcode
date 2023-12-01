calibrationDocument = []
listOfInts = []
twoDigitList = []
inputFile = open("2023\day01input.txt", "r")

def createListFromFile():   
    for line in inputFile:
        calibrationDocument.append(line)
    inputFile.close()
#    print(calibrationDocument)
    
def removeNonInts():
    for i in calibrationDocument:
        ints = []
        for character in i:
            if character.isdigit():
                ints.append(character)
        listOfInts.append(ints)
#    print(listOfInts)

def makeTwoDigitsAndSum():
    total = 0
    for i in listOfInts:
        if len(i) > 1:
            twoDigitNum = i[0] + i[-1]
#            twoDigitList.append(int(twoDigitNum))
            total = total + int(twoDigitNum)
        else:
            twoDigitNum = i[0] + i[0]
#            twoDigitList.append(int(twoDigitNum))
            total = total + int(twoDigitNum)
#    print(twoDigitList)
    print(f"The sum of all of the calibration values is {total}.")       
            
                       
    
createListFromFile()
removeNonInts()
makeTwoDigitsAndSum()