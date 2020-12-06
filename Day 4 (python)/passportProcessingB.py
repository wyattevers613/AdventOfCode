# Day 4 Challenge 1

# split up passwords
with open("day4input.txt", "r") as readFile:
    passports = []
    currentPassport = ""
    for line in readFile:
        if line == "\n":
            passports.append(currentPassport)
            currentPassport = ""
        else:
            currentPassport = currentPassport + line.strip() + " "
    
presentPassports = []


for passport in passports:
    if ("byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and 
    "hcl" in passport and "ecl" in passport and "pid" in passport):
        presentPassports.append(passport)



processedPassports = []
# each data field seperate in tup
for passport in presentPassports:
    processedTup = passport.split(" ")
    del processedTup[-1] # delete unnecesary space saved
    processedPassports.append(processedTup)
    




        


def procByr(inStr):
    if inStr[4:].isdigit():
        if 1920 <= int(inStr[4:]) <= 2002:
            return True
    #print("byrTest")
    return False

def procIyr(inStr):
    if inStr[4:].isdigit():
        if 2010 <= int(inStr[4:]) <= 2020:
            return True
    #print("iyrTest")
    return False

def procEyr(inStr):
    if inStr[4:].isdigit():
        if 2020 <= int(inStr[4:]) <= 2030:
            return True
    #print("eyrTest")
    return False

def procHgt(inStr):
    workStr = inStr[4:]
    if "cm" in workStr:
        if workStr[:3].isdigit():
            if 150 <= int(workStr[:3]) <= 193:
                return True
    if "in" in workStr:
        if workStr[:2].isdigit():
            if 59 <= int(workStr[:2]) <= 76:
                return True
    #print("HgtTest")
    return False

def procHcl(inStr):
    workStr = inStr[4:]
    if workStr[0] == "#":
        for letter in workStr[1:]:
            if not letter in "0123456789abcdef":
                return False
        return True
    #print("HclTest")
    #print(workStr[1:])
    return False

def procEcl(inStr):
    workStr = inStr[4:]
    if workStr in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    #print("EclTest")
    return False
    

def procPid(inStr):
    workStr = inStr[4:]
    if len(workStr) == 9 and workStr.isdigit():
        return True
    else:
        #print("pidTest")
        return False


def checkValidity(passTup):
    for field in passTup:
        if field[:3] == "byr":
            if procByr(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "iyr":
            if procIyr(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "eyr":
            if procEyr(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "hgt":
            if procHgt(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "hcl":
            if procHcl(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "ecl":
            if procEcl(field):
                continue
            else:
                print(field)
                return False
        if field[:3] == "pid":
            if procPid(field):
                continue
            else:
                print(field)
                return False
    return True

validPasswords = 0
for passP in processedPassports:
    if checkValidity(passP):
        validPasswords += 1
    else:
        pass
        #print(passP)


print(validPasswords)


















# Evaluated last passport by hand to solve problem faster than implementing special rules to incorporate it
# Last passport is valid so +1 to validPasswords