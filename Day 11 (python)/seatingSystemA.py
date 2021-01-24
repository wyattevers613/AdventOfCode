

# create grid

with open("day11input.txt", "r") as readFile:
    grid = []
    for line in readFile:
        row = []
        lineStr = line.strip().split()
        for char in lineStr:
            row.append(char)
        grid.append(row)


# print grid for debugging

def printGrid(wGrid):
    for row in wGrid:
        lineStr = ""
        for item in row:
            lineStr += f"{item} "
        print(lineStr)


#printGrid(grid)












