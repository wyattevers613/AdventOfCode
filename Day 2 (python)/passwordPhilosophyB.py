# Day 2 Part A



validPasswords = 0



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
        if actual[countStart] == searchChar:
            searchCharCount += 1
        if actual[countEnd] == searchChar:
            searchCharCount += 1
        if searchCharCount == 1:
            validPasswords += 1




#print("There are " + str(len(allowedActualDict)) + " passwords in list.")
print(f"Found Solution: {validPasswords} are valid.")

