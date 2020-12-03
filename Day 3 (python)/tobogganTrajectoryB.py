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



def treesHit(slopeX,slopeY):
    x = 0
    y = 0
    treesHit = 0
    while y < height:
        #print(f"Coordinates: ({x}, {y})")
        if grid[y][x] == 1:
            treesHit +=1
        y += slopeY
        x += slopeX
        if x > 30:
            x -= 31
    return treesHit


solution = treesHit(1,1) * treesHit(3,1) * treesHit(5,1) * treesHit(7,1) * treesHit(1,2)

print(f"Part B: {solution}")