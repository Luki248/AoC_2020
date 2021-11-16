#!/usr/bin/env python3

# Advent of Code
# Day 24
# https://adventofcode.com/2020/day/24

input = [line.rstrip('\n') for line in open("input.txt")]

DIR_E = 0
DIR_W = 1
DIR_SE = 2
DIR_SW = 3
DIR_NW = 4
DIR_NE = 5


def get_tile(line):
    instr = []
    i = 0
    while i < len(line):
        if line[i] == "e":
            instr.append(DIR_E)
            i += 1
        elif line[i] == "w":
            instr.append(DIR_W)
            i += 1
        elif line[i] == "s":
            if line[i+1] == "e":
                instr.append(DIR_SE)
                i += 2
            else:
                instr.append(DIR_SW)
                i += 2
        elif line[i] == "n":
            if line[i+1] == "w":
                instr.append(DIR_NW)
                i += 2
            else:
                instr.append(DIR_NE)
                i += 2
        else:
            assert False, "Unknown Direction"
    return instr


# Puzzle 1
black_side_up = 0
for line in input:
    tile = get_tile(line)
    print(tile)
print("First Puzzle:", black_side_up)


# Puzzle 2

print("Second Puzzle:")
