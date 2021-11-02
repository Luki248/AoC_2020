# Advent of Code
# Day 8
# https://adventofcode.com/2020/day/8

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]

line_to_change = -1     # -1 nothing changes, otherwise change line

# Puzzle 1
def nintendo(line_to_change):
    acc = 0
    i = 0
    lines = [-1]

    while i < len(input):
        temp = input[i].split(" ")
        instruction = temp[0]
        integer = int(temp[1])

        # line to change
        if line_to_change == i:
            if instruction == "nop":
                instruction = "jmp"
            else:
                instruction = "nop"

        # is line beeing visited again?
        for l in lines:
            if l == i:
                return acc
        lines.append(i)

        if instruction == "acc":
            acc += integer
            i += 1
        elif instruction == "jmp":
            i += integer
        else: # nop
            i += 1

        if i == 636:
            print("Second Puzzle:", acc)
            return i
    
    return 0

# Puzzle 1
ret = nintendo(line_to_change)
print("First Puzzle:", ret)

# Puzzle 2
k = 0
for line in input:
    temp = line.split(" ")
    instruction = temp[0]
    integer = int(temp[1])

    if instruction == "jmp" or instruction == "nop":
        line_to_change = k
        ret = nintendo(line_to_change)

        # was programm at end of code
        if ret == 636:
            pass

    k += 1

