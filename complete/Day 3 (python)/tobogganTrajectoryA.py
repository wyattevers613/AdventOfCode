# Day 3

# create grid using nested list, store as 0 and 1

with open("day3input.txt","r") as readFile:
    grid = []
    for line in readFile:
        row = []
        for spot in line.strip():
            if spot == "#":
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

# simple grid print function

def printGrid(wGrid):
    for row in wGrid:
        rowStr = ""
        for val in row:
            rowStr += f"{val} "
        print(rowStr)




height = len(grid)
width = len(grid[0])

print(f"Grid is {width} by {height}")

# count trees

x = 0
y = 0

treesHit = 0

while y < height:
    print(f"Coordinates: ({x}, {y})")
    if grid[y][x] == 1:
        treesHit +=1
    y += 1
    x += 3
    if x > 30:
        x -= 31


print(f"{treesHit} trees hit.")