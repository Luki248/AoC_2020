# Advent of Code
# Day 1
# https://adventofcode.com/2020/day/1

file = open("input.txt", "r")
input = file.readlines()

for i in input:
    i = int(i)

    for j in input:
        j = int(j)

        if i + j == 2020:
            print("First Puzzle:", i, j, (i * j))

        for l in input:
            l = int(l)

            if i + j + l == 2020:
                print("Second Puzzle:", i, j, l, (i * j * l))