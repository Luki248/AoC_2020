# Advent of Code
# Day 4
# https://adventofcode.com/2020/day/4

input = [line.rstrip('\n') for line in open("input.txt")]
arr = []

i = 0
j = 0
while i < 1129:
    if input[i] != "":
        arr.append(input[i])
        i += 1
        if i >= 1129:
            break
        while input[i] != "":
            arr[j] = arr[j] + " " + input[i]
            i += 1
            if i >= 1129:
                break

    i += 1
    j += 1

# for better managing add five " " at every element
for i in range(len(arr)):
    arr[i] += "     "

fr = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# First Puzzle:
count1 = 0
count2 = 0
for identity in arr:
    if (fr[0] in identity) and \
       (fr[1] in identity) and \
       (fr[2] in identity) and \
       (fr[3] in identity) and \
       (fr[4] in identity) and \
       (fr[5] in identity) and \
       (fr[6] in identity):
        count1 += 1

        # Second Puzzle:
        # byr
        pos = identity.find(fr[0])
        pos += 4
        if identity[pos + 4] == " ":
            byr = 1000 * int(identity[pos]) + 100 * int(identity[pos + 1]) + 10 * int(identity[pos + 2]) + int(identity[pos + 3])
        else:
            byr = 0

        # iyr
        pos = identity.find(fr[1])
        pos += 4
        if identity[pos + 4] == " ":
            iyr = 1000 * int(identity[pos]) + 100 * int(identity[pos + 1]) + 10 * int(identity[pos + 2]) + int(identity[pos + 3])
        else:
            iyr = 0

        # eyr
        pos = identity.find(fr[2])
        pos += 4
        if identity[pos + 4] == " ":
            eyr = 1000 * int(identity[pos]) + 100 * int(identity[pos + 1]) + 10 * int(identity[pos + 2]) + int(identity[pos + 3])
        else:
            eyr = 0

        # hgt
        pos = identity.find(fr[3])
        pos += 4
        if (identity[pos + 2] != " ") and (identity[pos + 3] != " "):
            # is number 3 or 2 characters long?
            if identity[pos + 2].isdigit():
                hgt = 100 * int(identity[pos]) + 10 * int(identity[pos + 1]) + int(identity[pos + 2])
                if identity[pos + 3] == "c" and identity[pos + 4] == "m" and identity[pos + 5] == " ":
                    unit = "cm"
                else:
                    if identity[pos + 3] == "i" and identity[pos + 4] == "n" and identity[pos + 5] == " ":
                        unit = "in"
                    else:
                        hgt = 0
                        unit = ""
            else:
                hgt = 10 * int(identity[pos]) + int(identity[pos + 1])
                if identity[pos + 2] == "c" and identity[pos + 3] == "m" and identity[pos + 4] == " ":
                    unit = "cm"
                else:
                    if identity[pos + 2] == "i" and identity[pos + 3] == "n" and identity[pos + 4] == " ":
                        unit = "in"
                    else:
                        hgt = 0
                        unit = ""
        else:
            hgt = 0
            unit = ""
        
        # hcl
        pos = identity.find(fr[4])
        if (identity[pos + 4] == "#") and (identity[pos + 11] == " "):
            pos += 5
            i = 0
            hcl = ""
            while (i < 6) and (identity[pos + i] != " "):
                c = identity[pos + i]
                if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or \
                   c == "a" or c == "b" or c == "c" or c == "d" or c == "e" or c == "f":
                    hcl += c
                i += 1
        else:
            hcl = ""

        # ecl
        pos = identity.find(fr[5])
        pos += 4
        if identity[pos + 3] == " ":
            ecl = ""
            ecl = identity[pos]
            ecl += identity[pos + 1]
            ecl += identity[pos + 2]
        else:
            ecl = ""

        # pid
        pos = identity.find(fr[6])
        pos += 4
        if identity[pos + 9] == " ":
            i = 0
            pid = ""
            while i < 9:
                if identity[pos + i] == " ":
                    pid = ""
                    break
                pid += identity[pos + i]
                i += 1
        else:
            pid = ""

        # check data
        if (byr >= 1920) and (byr <= 2002):
            if (iyr >= 2010) and (iyr <= 2020):
                if (eyr >= 2020) and (eyr <= 2030):
                    if hcl.isalnum() and (len(hcl) == 6):
                        if len(ecl) == 3:
                            if (ecl == "amb") or \
                               (ecl == "blu") or \
                               (ecl == "brn") or \
                               (ecl == "gry") or \
                               (ecl == "grn") or \
                               (ecl == "hzl") or \
                               (ecl == "oth"):
                                if (len(pid) == 9) and pid.isdigit():
                                    if (unit == "cm") and (hgt >= 150) and (hgt <= 193):
                                        count2 += 1
                                    else:
                                        if (unit == "in") and (hgt >= 59) and (hgt <= 76):
                                            count2 += 1


print("First Puzzle:", count1)
print("Second Puzzle:", count2)
