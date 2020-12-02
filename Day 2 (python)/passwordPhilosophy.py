# Day 2 Part A

#create dictionary of allowed and actual

with open("day2input.txt", "r") as readFile:
    allowedActualDict = dict()
    for line in readFile:
        allowed, actual = line.strip().split(":")
        allowedActualDict[allowed] = actual.strip()

    
# process keys and evaluate password validity

validPasswords = 0

for allowed in allowedActualDict.keys():
    allRange, countChar = allowed.split(" ")
    rangeStart, rangeEnd = allRange.split("-")
    rangeStart = int(rangeStart)
    rangeEnd = int(rangeEnd)
    letterCount = 0

    # print Str for debugging
    printStr = f"Looking for: {countChar} in {allowedActualDict[allowed]}, {rangeStart} - {rangeEnd} times. "


    for letter in allowedActualDict[allowed]:
        if letter == countChar:
            letterCount += 1

    printStr += f"Found {letterCount} time(s)."

    if rangeStart <= letterCount <= rangeEnd: 
        validPasswords += 1
        printStr += "Valid. "
        printStr += f"{validPasswords} valid passwords so far."
    else:
        printStr += "Invalid. "
    
    print(printStr)



print("There are " + str(len(allowedActualDict)) + " passwords in list.")
print(f"Found Solution: {validPasswords} are valid.")