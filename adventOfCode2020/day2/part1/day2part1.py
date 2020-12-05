print("Advent of Code 2020")
print('User: Phishman651')
print('Day  Part 1')
print("")

def openAndParseLines(inputFile, outputList):
    f = open(inputFile,"r")

    myList = []
    for line in f:
        myList.append(line)

    lst = []
    for i in myList:
        i = i[:-1]
        outputList.append(i)

def getMinOccur(inputString):
    # print("Getting minimum occurance")
    tmpMin = ''
    for j in range(len(inputString)):
        # print(inputString[j])
        if(inputString[j] != '-'):
            tmpMin = tmpMin + inputString[j]
            # print(tmpMin)
        elif(inputString[j] == '-'):
            dashIndexTmp = j
            break
    outputMinimum = int(tmpMin)
    # print(outputMinimum)
    return outputMinimum,dashIndexTmp

def getMaxOccur(startIndex,inputString):
    # print("Getting maximum occurance")
    tmpMin = ''
    for j in range(startIndex,len(inputString)):
        # print(inputString[j])
        if((inputString[j] != '-') and (inputString[j] != ' ')):
            tmpMin = tmpMin + inputString[j]
            # print(tmpMin)
        elif(inputString[j] == ' '):
            nextIndexTmp = j + 1
            break
    outputMmaximum = int(tmpMin)
    # print(outputMmaximum)
    return outputMmaximum,nextIndexTmp

def getCharOccur(startIndex,inputString):
    # print("Getting character occurance")
    tmpChar = ''
    for j in range(startIndex,len(inputString)):
        # print(inputString[j])
        if((inputString[j] != ' ') and (inputString[j] != ':')):
            tmpChar = tmpChar + inputString[j]
            # print(tmpChar)
        elif(inputString[j] == ':'):
            nextIndexTmp = j + 1
            break
    # print(tmpChar)
    return tmpChar,nextIndexTmp

def getRemainingString(startIndex,inputString):
    # print("Getting remaining occurance")
    tmpChar = ''
    for j in range(startIndex,len(inputString)):
        # print(inputString[j])
        if((inputString[j] != ' ') and (inputString[j] != '')):
            tmpChar = tmpChar + inputString[j]
        #     # print(tmpChar)
        # elif(inputString[j] == ':'):
        #     nextIndexTmp = j + 1
        #     break
    # print(tmpChar)
    return tmpChar

lst = []
openAndParseLines("input.txt",lst)
listLength = len(lst)

# print(lst)

# minOccur = 0
# maxOccur = 0
# charOccur = 'a'
validPasswords = 0
invalidPasswords = 0

# print(lst[0][0])
# print(lst[0][1])
# print(lst[0][2])
# print(listLength)
for i in range(listLength):
    print("i: " + str(i))
    minOccur,nextIndex = getMinOccur(lst[i])
    maxOccur,nextIndex = getMaxOccur(nextIndex,lst[i])
    charOccur,nextIndex = getCharOccur(nextIndex,lst[i])
    remainingString = getRemainingString(nextIndex,lst[i])
    numOccurrences = remainingString.count(charOccur)
    print(lst[i])
    print("minOccur = " + str(minOccur))
    print("maxOccur = " + str(maxOccur))
    print("charOccur = " + charOccur)
    print("remainingString = " + remainingString)
    print("numOccurrences = " + str(numOccurrences))
    print("")

    if((numOccurrences >= minOccur) and (numOccurrences <= maxOccur)):
        validPasswords = validPasswords + 1
        print("Password valid")
        print("\n")
    else:
        invalidPasswords = invalidPasswords + 1

        print("Password invalid")
        print("\n")
        # break
    
    # print("Total valid   = " + str(validPasswords))
    # print("Total invalid = " + str(invalidPasswords))
    # print("")

print("Total valid   = " + str(validPasswords))
print("Total invalid = " + str(invalidPasswords))
print("")
# print("***")
# print(lst[999])
# print("***")