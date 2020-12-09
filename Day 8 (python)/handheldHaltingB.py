# Day 8

workingFile = "day8input.txt"

with open(workingFile, "r") as readFile:
    instructionList = []
    # example entry [index, instruction, number, executed]
    lineCount = 0
    for line in readFile:
        index = lineCount
        instruction, number = line.strip().split(" ")
        executed = False
        entry = [index, instruction, int(number), executed]
        instructionList.append(entry)
        lineCount += 1
    
lastLine = "Success"
instructionList.append(lastLine)

def hasEnd(wList):

    stillRun = True
    curInd = 0
    acc = 0

    while stillRun:
        if instructionList[curInd] == "Success":
            return acc
        wEntry = wList[curInd]
        if wEntry[3] == True:
            stillRun = False
            return False
        else:
            wList[curInd][3] = True
            if wEntry[1] == "acc":
                acc += wEntry[2]
                curInd += 1
            elif wEntry[1] == "jmp":
                curInd += wEntry[2]
            elif wEntry[1] == "nop":
                curInd += 1
        



def swap(entry):
    if entry[1] == "jmp":
        entry[1] = "nop"
    elif entry[1] == "nop":
        entry[1] = "jmp"
    return entry




import copy

def generateAllCombos(originalList):
    allComboList = []

    # get ind of all nop and jmp
    indList = []
    for entry in originalList:
        if entry[1] == "nop" or "jmp":
            indList.append(entry[0])
    
    for ind in indList:
        wList = copy.deepcopy(originalList)
        wList[ind] = swap(wList[ind])
        
        ran = hasEnd(wList)
        if not ran == False:   # optimized, no need to store every possible combo if one works
            return ran


print(generateAllCombos(instructionList))