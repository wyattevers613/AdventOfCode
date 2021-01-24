# Day 1 Report Repair
solution = None


with open("Report Repair Input.txt", "r") as readFile:
    expenseList = []
    for line in readFile:
        expenseList.append(int(line.strip()))

for aInd, aExpense in enumerate(expenseList):
    for bInd, bExpense in enumerate(expenseList):
        if not aInd == bInd:
            if aExpense + bExpense == 2020:
                solution = aExpense * bExpense


print(f"Found Solution: {solution}")

