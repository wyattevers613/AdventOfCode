# Day 5 part A


with open("day6input.txt", "r") as readFile:
    groupAnswerList = []
    entry = ""
    for line in readFile:
        entry += line.strip()
        if line == "\n":
            groupAnswerList.append(entry)
            entry = ""
        else:
            entry += line      
    groupAnswerList.append(entry)


#print(groupAnswerList[5])

answerSum = 0

"""
test = "abcx\nabcy\nabcz\n"



uniqueLetterList = []
for letter in test:
    if not letter in uniqueLetterList:
        uniqueLetterList.append(letter)
        print(uniqueLetterList)
answerSum += (len(uniqueLetterList) - 2)



"""

for entry in groupAnswerList:
    uniqueLetterList = []
    for letter in entry:
        if not letter in uniqueLetterList:
            uniqueLetterList.append(letter)
    answerSum += (len(uniqueLetterList) - 1)


print(answerSum)