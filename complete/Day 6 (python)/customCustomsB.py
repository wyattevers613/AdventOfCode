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

responses = test.split("\n")
del responses[-1]
print(responses)

uniqueLetterList = []
for letter in test:
    if not letter in uniqueLetterList:
        uniqueLetterList.append(letter)
answerSum += (len(uniqueLetterList) - 2)



"""


for entry in groupAnswerList:
    uniqueLetterList = []

    for letter in entry:
        if not letter in uniqueLetterList:
            uniqueLetterList.append(letter)

    indResponses = entry.split("\n")
    del indResponses[-1]

    allRespLetters = []
    for letter in uniqueLetterList:
        add = True
        for resp in indResponses:
            if not letter in resp:
                add = False
        if add:
            allRespLetters.append(letter)

    answerSum += len(allRespLetters)
       # for \n


print(answerSum)
