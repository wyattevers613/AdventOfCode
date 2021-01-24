# adapter list


with open("day10input.txt", "r") as readFile:
    adapterList = []
    for line in readFile:
        adapterList.append(int(line.strip()))
    

#print(adapterList)


# print(adapterList)

cur = max(adapterList) + 3


run = True

order = [cur]

while run:
    try:
        del adapterList[adapterList.index(cur)]
    except ValueError:
        pass

    # break
    if len(adapterList) == 0:
        run = False



    adapterDiff = []
    for item in adapterList:
        diff = cur - item
        if not diff == 0:
            adapterDiff.append([diff, item])

    minDiff = 3
    for entry in adapterDiff:
        diff, adapter = entry
        if diff < minDiff:
            minDiff = diff

    for entry in adapterDiff:
        if entry[0] == minDiff:
            cur = entry[1]
    
    order.append(cur)
    
order.append(0)



#print(order)

# count diff

Ind = 0

one = 0
two = 0
three = 0

for x in range(len(order)):

    try:
        diff = order[Ind] - order[Ind + 1]
    except IndexError:
        continue

    if diff == 1:
        one += 1
    elif diff == 2:
        two += 1
    elif diff == 3:
        three += 1
        
    Ind += 1



print(f"Solution: {one * three}")








