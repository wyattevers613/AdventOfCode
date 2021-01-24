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
    





stillRun = True
curInd = 0
acc = 0

while stillRun:
    wEntry = instructionList[curInd]
    if wEntry[3] == True:
        stillRun = False
        print(f"Final Accumulator Value: {acc}")
    else:
        instructionList[curInd][3] = True
        if wEntry[1] == "acc":
            acc += wEntry[2]
            curInd += 1
        elif wEntry[1] == "jmp":
            curInd += wEntry[2]
        elif wEntry[1] == "nop":
            curInd += 1
        