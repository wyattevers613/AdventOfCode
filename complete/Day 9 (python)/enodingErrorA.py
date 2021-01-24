


with open("day9input.txt") as readFile:
    lineCount = 0
    indNumList = []
    for line in readFile:
        entry = lineCount, int(line.strip())
        indNumList.append(entry)
        lineCount += 1
    
print(indNumList)

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
    print(workingEntry)
    if not sumTo(workingEntry[1], indNumList[workingEntry[0] - 25: workingEntry[0]]):
        print(f"Solution: {workingEntry[1]}")
        valid = False
    startInd += 1