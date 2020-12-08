# Process bags into dictionary


with open("day7input.txt", "r") as readFile:
    bagDict = dict()
    for line in readFile:
        first, other = line.strip().split("contain")
        key, trash = first.split(" bag")

        containedBags = other.strip().split(", ")
        # remove period on last entry
        containedBags[-1] = containedBags[-1][:-1]
        # remove leading number
        for ind, bag in enumerate(containedBags):
            color, useless = bag.split(" bag")
            containedBags[ind] = color[2:]
        # add to dictionary
        bagDict[key] = containedBags


#print(bagDict)

# Example dict entry
# 'drab magenta': ['faded fuchsia', 'dim black', 'dim crimson', 'dotted fuchsia']



# iterate through dictionary, check for gold

kList = bagDict.keys()


# recursively count bags
def containsGold(key):
    # Base Case, bag empty
    

    if not key in bagDict:
        return False
    
    #print(f"Current Bag: {bagDict[key]}")

    if "shiny gold" in bagDict[key]:
        return True

    else:
        for element in bagDict[key]:
            if containsGold(element):
                return True
    return False 



#print(containsGold('drab magenta'))



goldCount = 0

for key in kList:
    if containsGold(key):
        goldCount += 1

print(f"Solution: {goldCount}")






