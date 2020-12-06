


test = "FBFFBFFRLL"

colRange = [0, 7]
for direction in test[7:9]:
    if direction == "L":
        colRange[0] += ((colRange[1] - colRange[0] + 1) // 2)
    if direction == "F":
        colRange[1] -= ((colRange[1] - colRange[0] + 1) // 2)
    print(colRange)
if test[9] == "L":
    col = colRange[0]
else:
    col = colRange[1]
print(col)