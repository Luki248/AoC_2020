# Advent of Code
# Day 17
# https://adventofcode.com/2020/day/17

import numpy as np
import time

input = [line.rstrip('\n') for line in open("input.txt")]

size = 100

# Puzzle 1
cubes = np.zeros((size, size, size), dtype="b")
cubes2 = cubes.copy()

for x in range(len(input[0])):
    for y in range(len(input[0])):
        if input[x][y] == "#":
            cubes[int(size/2), int(x + (size/2)), int(y + size/2)] = 1

def count_neighbours1(x, y, z):
    count = 0
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                if j == 0 and k == 0 and l == 0:
                    pass
                elif cubes2[x + j][y + k][z + l] == 1:
                    count += 1
    return count

iteration = 0
while iteration < 6:
    cubes2 = cubes.copy()
    for x in range(1, size-1):
        print(time.asctime(), iteration, x)
        for y in range(1, size-1):
            for z in range(1, size-1):
                
                neighbours = count_neighbours1(x, y, z)
                if cubes2[x][y][z] == 1:
                    if neighbours == 2 or neighbours == 3:
                        pass
                    else:
                        cubes[x][y][z] = 0
                else:
                    if neighbours == 3:
                        cubes[x][y][z] = 1
    iteration += 1

sum = 0
for x in range(size):
    for y in range(size):
        for z in range(size):
            sum += cubes[x][y][z]
print("First Puzzle:", sum)


# Puzzle 2
cubes_2 = np.zeros((size, size, size, size), dtype="b")
cubes2_2 = cubes_2.copy()

def count_neighbours2(x, y, z, w):
    count = 0
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                for m in range(-1, 2):
                    if j == 0 and k == 0 and l == 0 and m == 0:
                        pass
                    elif cubes_2[x + j][y + k][z + l][w + m] == 1:
                        count += 1
    return count

iteration = 0
while iteration < 6:
    cubes2_2 = cubes_2.copy()
    for x in range(1, size-1):
        print(time.asctime(), iteration, x)
        for y in range(1, size-1):
            for z in range(1, size-1):
                for w in range(1, size-1):
                
                    neighbours = count_neighbours2(x, y, z, w)
                    if cubes2_2[x][y][z][w] == 1:
                        if neighbours == 2 or neighbours == 3:
                            pass
                        else:
                            cubes_2[x][y][z][w] = 0
                    else:
                        if neighbours == 3:
                            cubes_2[x][y][z][w] = 1
    iteration += 1

sum = 0
for x in range(size):
    for y in range(size):
        for z in range(size):
            for w in range(size):
                sum += cubes_2[x][y][z][w]
print("Second Puzzle:", sum)
