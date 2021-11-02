# Advent of Code
# Day 20
# https://adventofcode.com/2020/day20

input = [line.rstrip('\n') for line in open("input.txt")]

img_arr = [[]]
i = -1
for line in input:
    try:
        if line[0] == "T":
            img_arr.append([])
            i += 1
            img_arr[i].append(int(line[5:9]))
        else:
            img_arr[i].append(line)
    except:
        pass
img_arr.pop(144)


# Puzzle 1

print("First Puzzle:")


# Puzzle 2

print("Second Puzzle:")
