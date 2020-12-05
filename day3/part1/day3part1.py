print("Advent of Code 2020")
print('User: Phishman651')
print('Day 3, Part 1')
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

def printHill(inputList):
    for line in inputList:
        print(line)

def advStep(xStart,yStart,xDist,yDist,width):
    yStart = yStart + yDist
    xTmp = xStart + xDist

    if(xTmp <= (width)):
        #on the same patch
        xStart = xTmp
    else:
        #on the next patch, wrap around
        xTmp = xTmp - width
        xStart = xTmp - 1
    
    return xStart,yStart

def markSpot(myX,inputList):
    myWidth = len(inputList)
    myLine = ''
    for spot in range(myWidth):
        # myLine = myLine + inputList[spot]
        if(spot == myX):
            # print(spot)
            # print(myX)
            # print("")
            if(inputList[spot] == '.'):
                myLine = myLine + 'O'
            elif(inputList[spot] == '#'):
                myLine = myLine + 'X'
        else:
            if(inputList[spot] == '.'):
                myLine = myLine + '.'
            elif(inputList[spot] == '#'):
                myLine = myLine + '#'
    # print(myLine)
    return myLine

lst = []
openAndParseLines("input.txt",lst)
listLength = len(lst) - 1
patternWidth = len(lst[0]) - 1

# printHill(lst)
# print(listLength)
# print(patternWidth)
# print("")

#define movement slope
xMove = 3
yMove = 1

myX = [0]
myY = [0]

iterationCnt = 0
# print("myY = " + str(myY))
# print("myX = " + str(myX))
print("")
numTrees = 0
openSpot = 0
spotStatus = lst[0][0]
markedMap = []
# while(myY[iterationCnt] < listLength):
# for steps in range(listLength):
for steps in range(listLength):
    spotStatus = lst[myY[iterationCnt]][myX[iterationCnt]]
    # print("myY[" + str(iterationCnt) + "] = " + str(myY[iterationCnt]))
    # print("myX[" + str(iterationCnt) + "] = " + str(myX[iterationCnt]))
    # print("myY    = " + str(myY))
    # print("myX    = " + str(myX))
    # print(spotStatus)
    if(spotStatus == '.'):
        #spot open
        # print("Spot open")
        openSpot = openSpot + 1
    elif(spotStatus == '#'):
        #spot tree
        # print("Tree")
        numTrees = numTrees + 1
    # printHill(lst)
    markedMap.append(markSpot(myX[iterationCnt],lst[myY[iterationCnt]]))
    # printHill(markedMap)
    # print("\n\n")
    tmpX,tmpY = advStep(myX[iterationCnt],myY[iterationCnt],xMove,yMove,patternWidth)
    myX.append(tmpX)
    myY.append(tmpY)
    iterationCnt = iterationCnt + 1


# print("myY[i] = " + str(myY[iterationCnt]))
# print("myX[i] = " + str(myX[iterationCnt]))
# print("myY    = " + str(myY))
# print("myX    = " + str(myX))
# print(spotStatus)  
if(spotStatus == '.'):
    #spot open
    # print("Spot open")
    openSpot = openSpot + 1
elif(spotStatus == '#'):
    #spot tree
    # print("Tree")
    numTrees = numTrees + 1
# printHill(lst)
markedMap.append(markSpot(myX[iterationCnt],lst[myY[iterationCnt]]))
printHill(markedMap)
print("\n\n")
print("")
print("numTrees = " + str(numTrees))
print("openSpot = " + str(openSpot))