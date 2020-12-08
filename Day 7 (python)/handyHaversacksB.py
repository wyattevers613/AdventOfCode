# Process bags into dictionary


with open("day7input.txt", "r") as readFile:
    bagDict = dict()
    for line in readFile:
        first, other = line.strip().split("contain")
        key, trash = first.split(" bag")

        containedBags = other.strip().split(", ")
        # remove period on last entry
        containedBags[-1] = containedBags[-1][:-1]
        #print(containedBags)
        # remove leading number
        numBagList = []
        for ind, bag in enumerate(containedBags):
            if bag == "no other bags":
                EndNotice = "STOP"
                numBagList.append(EndNotice)
            else:
                color, useless = bag.split(" bag")
                col = color[2:]
                num = int(color[:2])
                bagTup = num, col
                numBagList.append(bagTup)

            
        # add to dictionary
        bagDict[key] = numBagList



print(bagDict)

# Example dict entry
# 'dull brown': [(5, 'dim lavender'), (4, 'bright tomato'), (5, 'drab crimson'), (1, 'vibrant tomato')]
# 'striped silver': ['STOP']


def countBags(key):
    bagSum = 0
    print(key)
    if "STOP" in bagDict[key]:
        print("END")
        return 0
    
    for element in bagDict[key]:
        bagSum += (element[0] + element[0] * countBags(element[1]))
    
    print("BREAK")
    return bagSum

solution = countBags("shiny gold")
print(f"Solution: {solution}")
