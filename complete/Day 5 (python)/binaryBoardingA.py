# Day 5 Part A

with open("day5input.txt", "r") as readFile:
    passList = []
    for line in readFile:
        passList.append(line.strip())





# Visualize

cabin = []
for row in range(128):
    row = []
    for col in range(8):
        row.append("O")
    cabin.append(row)


def printMatrix(cabin):
    for row in cabin:
        rowStr = ""
        for col in row:
            rowStr += (col + " ")
        print(rowStr)


#printMatrix(cabin)

# FBFFBFFRLL
# 0123456789


test = passList[0]

highVal = 0

for p in passList:

    rows = []
    startRow = 0
    for x in range(128):
        rows.append(startRow)
        startRow += 1

    cols = []
    startCol = 0
    for x in range(8):
        cols.append(startCol)
        startCol += 1

    for direction in p[:7]:
        if direction == "F":
            rowsLength = len(rows)
            rows = rows[0:-(rowsLength // 2)]
        if direction == "B":
            rowsLength = len(rows)
            rows = rows[0 + (rowsLength // 2):]
    row = rows[0]

    for direction in p[7:]:
        if direction == "L":
            colsLength = len(cols)
            cols = cols[0:-(colsLength // 2)]
        if direction == "R":
            colsLength = len(cols)
            cols = cols[0 + (colsLength // 2):]
    col = cols[0]


    val = row * 8 + col
    if val > highVal:
        highVal = val

print(highVal)




"""


highVal = 0

for p in passList:
    # row
    rowRange = [0, 127]
    for direction in p[0:6]:
        if direction == "F":
            rowRange[0] += ((rowRange[1] - rowRange[0] + 1) // 2)
        if direction == "B":
            rowRange[1] -= ((rowRange[1] - rowRange[0] + 1) // 2)
    if p[6] == "F":
        row = rowRange[0]
    else:
        row = rowRange[1]

    # column
    colRange = [0, 7]
    for direction in p[7:9]:
        if direction == "R":
            colRange[0] += ((colRange[1] - colRange[0] + 1) // 2)
        if direction == "L":
            colRange[1] -= ((colRange[1] - colRange[0] + 1) // 2)
    if p[-1] == "L":
        col = colRange[0]
    else:
        col = colRange[1]

    val = (row * 8) + col
    #print(f"Row: {row} | Column: {col} | Value: {val}")
    if cabin[row][col] == "X":
        raise ValueError("Seat taken, fix your code")
    else:
        cabin[row][col] = "X"
    
    if val > highVal:
        highVal = val


printMatrix(cabin)
print(highVal)

"""