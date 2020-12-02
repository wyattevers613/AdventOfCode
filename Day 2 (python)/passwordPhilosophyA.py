# Day 2 Part A



validPasswords = 0


"""      # Attempt with dictionary
#create dictionary of allowed and actual

with open("day2input.txt", "r") as readFile:
    allowedActualDict = dict()
    for line in readFile:
        allowed, actual = line.strip().split(":")
        allowedActualDict[allowed] = actual.strip()

# process keys and evaluate password validity

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

"""

# Attempt with lists

with open("day2input.txt", "r") as readFile:
    # pull lines into list
    wList = []
    for line in readFile:
        wList.append(line.strip())
    # process each item in list
    for entry in wList:
        policy, actual = entry.split(":")
        countRange, searchChar = policy.split(" ")
        countStart, countEnd = countRange.split("-")
        countStart = int(countStart)
        countEnd = int(countEnd)
        searchCharCount = 0
        for character in actual:
            if character == searchChar:
                searchCharCount += 1
        if countStart <= searchCharCount <= countEnd:
            validPasswords += 1




#print("There are " + str(len(allowedActualDict)) + " passwords in list.")
print(f"Found Solution: {validPasswords} are valid.")

