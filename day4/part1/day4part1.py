print("Advent of Code 2020")
print('User: Phishman651')
print('Day 4, Part 1')
print("")

def openAndParseLines(inputFile):
    outputList = []
    f = open(inputFile,"r")

    myList = []
    for line in f:
        myList.append(line)

    lst = []
    for i in myList:
        i = i[:-1]
        outputList.append(i)

    return outputList

def printHill(inputList):
    for line in inputList:
        print(line)

def getNextPassport(passportList,startPoint,listLength):
    print("Getting the next passport!")
    outputPassport = []
    bMoreEntries = True

    for line in range(startPoint,len(passportList)):
        print(passportList[line])
        if passportList[line] != '':
            outputPassport.append(passportList[line])
            outputPassport.append(" ")
        else:
            break
    
    print("Next passport:")
    outputPassport = "".join(outputPassport)
    print("".join(outputPassport))
    print("")

    if line == listLength - 1:
        bMoreEntries = False

    return outputPassport,bMoreEntries,line

def checkPassport(passportList):
    print("Checking the passport!")
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
    BirthYear = "byr:"
    IssueYear = "iyr:"
    ExpYear = "eyr:"
    Height = "hgt:"
    EyeClr = "ecl:"
    PassId = "pid:"
    CntryId = "cid:"

    if BirthYear in passportList:
        print("Birth Year Present!")
    else:
        return False
    if IssueYear in passportList:
        print("Issue Year Present!")
    else:
        return False
    if ExpYear in passportList:
        print("Expire Year Present!")
    else:
        return False
    if Height in passportList:
        print("Height Present!")
    else:
        return False
    if EyeClr in passportList:
        print("Eye Color Present!")
    else:
        return False
    if PassId in passportList:
        print("Passport ID Present!")
    else:
        return False
    # if CntryId in passportList:
    #     print("Country ID Present!")
    print("")
    print("")

    return True



lst = []
lst = openAndParseLines("input.txt")
listLength = len(lst)
# patternWidth = len(lst[0])
bMorePassports = True
# while(bMorePassports):
lineTmp = 0
invalidCnt = 0
validCnt = 0
# for i in range(4):
while(bMorePassports):
    myPassport,bMorePassports,lineTmp = getNextPassport(lst,lineTmp,listLength)
    lineTmp = lineTmp + 1
    bPassportValid = checkPassport(myPassport)
    print("bPassportValid = " + str(bPassportValid))
    if(bPassportValid == True):
        validCnt = validCnt + 1
    else:
        invalidCnt = invalidCnt + 1
    print("bMorePassports = " + str(bMorePassports))
    print("")
    print("validCnt = " + str(validCnt))
    print("invalidCnt = " + str(invalidCnt))
    print("")
    print("")