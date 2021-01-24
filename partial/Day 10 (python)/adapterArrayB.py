# adapter list


with open("day10input.txt", "r") as readFile:
    adapterList = []
    for line in readFile:
        adapterList.append(int(line.strip()))
    

#print(adapterList)


# print(adapterList)

cur = max(adapterList) + 3


