# Day 4 Challenge 1

# split up passwords
with open("day4inputSample.txt", "r") as readFile:
    passports = []
    currentPassport = ""
    for line in readFile:
        if line == "\n":
            passports.append(currentPassport)
            currentPassport = ""
        else:
            currentPassport = currentPassport + line.strip() + " "
    
validPassports = 0
totalPassports = 0
for passport in passports:
    if ("byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and 
    "hcl" in passport and "ecl" in passport and "pid" in passport):
        validPassports += 1
        #print("Valid")
    else:
        pass
        #print("invalid")
    totalPassports += 1




#print(passports[0])

print(passports[1])

print(validPassports)
print(totalPassports)


# Figured out I was missing last entry from running on sample input
# Didn't add 1 for last line so 205 wasn't right, put in 206 with that suspicion and it worked