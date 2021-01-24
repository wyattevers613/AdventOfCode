


with open("day9input.txt") as readFile:
    lineCount = 0
    indNumList = []
    for line in readFile:
        entry = lineCount, int(line.strip())
        indNumList.append(entry)
        lineCount += 1
    


def sumTo(target, wList):
    numList = []
    for x in wList:
        numList.append(x[1])
    for a in numList:
        for b in numList:
            if a + b == target:
                return True
    
    return False





valid = True
startInd = 25

while valid:
    workingEntry = indNumList[startInd]
    if not sumTo(workingEntry[1], indNumList[workingEntry[0] - 25: workingEntry[0]]):
        solution = workingEntry[1]
        print(f"Solution: {solution}")
        valid = False
    startInd += 1




found = False
startInd = 0
while found == False:
    print(startInd)
    wEntry = indNumList[startInd]
    wList = indNumList[startInd:0:-1]
    numList = []
    for entry in wList:
        numList.append(entry[1])

    entrySum = 0
    addedList = []

    for num in numList:
        entrySum += num
        addedList.append(num)
        if entrySum == solution:
            found = True
            nSolution = max(addedList) + min(addedList)
            print(f"B Solution: {nSolution}")

    startInd += 1



    if startInd == lineCount + 1:
        found = False
        print("End of File")










