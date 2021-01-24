# Day 1 Report Repair
solution = None


with open("Report Repair Input.txt", "r") as readFile:
    expenseList = []
    for line in readFile:
        expenseList.append(int(line.strip()))

for aInd, aExpense in enumerate(expenseList):
    for bInd, bExpense in enumerate(expenseList):
        if not aInd == bInd:
            for cInd, cExpense in enumerate(expenseList):
                if not cInd == aInd and not cInd == bInd:
                    if aExpense + bExpense + cExpense == 2020:
                        solution = aExpense * bExpense * cExpense

            


print(f"Found Solution (Part B): {solution}")

