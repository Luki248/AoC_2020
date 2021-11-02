# Advent of Code
# Day 23
# https://adventofcode.com/2020/day23

input = [line.rstrip('\n') for line in open("input.txt")]

arr = []
i = 0
while i < len(input[0]):
    arr.append(int(input[0][i]))
    i += 1

min = min(arr)
max = max(arr)

current_cup = 0

# Puzzle 1
pickup = [0, 0, 0]
i = 0
while i < 10:
    j = current_cup
    if j + 1 >= len(arr):
        pickup[0] = arr[0]
    else:
        pickup[0] = arr[j + 1]
    if j + 2 >= len(arr):
        pickup[1] = arr[1]
    else:
        pickup[1] = arr[j + 2]
    if j + 3 >= len(arr):
        pickup[2] = arr[2]
    else:
        pickup[2] = arr[j + 3]

    destination = arr[current_cup] - 1

    while pickup.count(destination) == 1:
        destination -= 1
        if destination < 0:
            destination = max

    for cup in pickup:
        arr.remove(cup)

    arr.insert(destination, pickup[2])
    arr.insert(destination, pickup[1])
    arr.insert(destination, pickup[0])

    current_cup = destination - 1
    if current_cup < 0:
        current_cup = len(arr) - 1
    i += 1

output = ""
for i in arr:
    output = output + str(i)
print("First Puzzle:", output)


# Puzzle 2

print("Second Puzzle:")
