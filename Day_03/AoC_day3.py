# Advent of Code
# Day 3
# https://adventofcode.com/2020/day/3

input = [line.rstrip('\n') for line in open("input.txt")]
arr = []

for i in range(323):
    arr.append(input[i])
    for _ in range(100):
        arr[i] += input[i]

# slope 1
right = 3
down = 1
count_trees_1 = 0
i = 0
j = 0
while i < 323:
    if arr[i][j] == "#":
        count_trees_1 += 1
    j += right
    i += down
    
print("First Puzzle:", count_trees_1)
print("Slope 1:", count_trees_1)

# slope 2
right = 1
down = 1
count_trees_2 = 0
i = 0
j = 0
while i < 323:
    if arr[i][j] == "#":
        count_trees_2 += 1
    j += right
    i += down
print("Slope 2:", count_trees_2)

# slope 3
right = 5
down = 1
count_trees_3 = 0
i = 0
j = 0
while i < 323:
    if arr[i][j] == "#":
        count_trees_3 += 1
    j += right
    i += down
print("Slope 3:", count_trees_3)

# slope 4
right = 7
down = 1
count_trees_4 = 0
i = 0
j = 0
while i < 323:
    if arr[i][j] == "#":
        count_trees_4 += 1
    j += right
    i += down
print("Slope 4:", count_trees_4)

# slope 5
right = 1
down = 2
count_trees_5 = 0
i = 0
j = 0
while i < 323:
    if arr[i][j] == "#":
        count_trees_5 += 1
    j += right
    i += down
print("Slope 5:", count_trees_5)

print("Second Puzzle:", (count_trees_1 * count_trees_2 * count_trees_3 * count_trees_4 * count_trees_5))