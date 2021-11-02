# Advent of Code
# Day 15
# https://adventofcode.com/2020/day/15

import time

input = [line.rstrip('\n') for line in open("input.txt")]

temp = input[0].split(",")
numbers_spoken = []
for i in temp:
    numbers_spoken.append(int(i))

# Puzzle 1 & 2
numbers_spoken_counter = len(temp) - 1
while numbers_spoken_counter < 30000000:
    if numbers_spoken.count(numbers_spoken[numbers_spoken_counter]) == 1:
        numbers_spoken.append(0)
    else:
        num_to_find = numbers_spoken[numbers_spoken_counter]
        j = numbers_spoken_counter - 1
        while j > -1:
            if numbers_spoken[j] == num_to_find:
                numbers_spoken.append(numbers_spoken_counter - j)
                break
            j -= 1
    if numbers_spoken_counter % 100000 == 0:
        print(time.asctime(), numbers_spoken_counter)
    numbers_spoken_counter += 1

print("First Puzzle:", numbers_spoken[2020 - 1])
print("Second Puzzle:", numbers_spoken[30000000 - 1])
