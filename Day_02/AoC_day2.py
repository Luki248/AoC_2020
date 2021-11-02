# Advent of Code
# Day 2
# https://adventofcode.com/2020/day/2

file = open("input.txt", "r")
input = file.readlines()


right_1 = 0
right_2 = 0

for i in input:
    temp = i.split("-")
    count_low = int(temp[0])

    temp2 = temp[1].split(" ")
    count_max = int(temp2[0])

    temp3 = temp2[1].split(":")
    char = temp3[0]
    string = temp2[2]
    
    # Puzzle 1
    count = 0
    for j in string:
        if j == char:
            count += 1
    
    if count >= count_low:
        if count <= count_max:
            right_1 += 1

    # Puzzle 2
    count = 0

    if string[count_low - 1] == char:
        count += 1
    if string[count_max - 1] == char:
        count += 1
    
    if count == 1:
        right_2 += 1

print("First Puzzle:", right_1)
print("Second Puzzle:", right_2)