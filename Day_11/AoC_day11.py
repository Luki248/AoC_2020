# Advent of Code
# Day 11
# https://adventofcode.com/2020/day/11

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]

# input to numpy array
height = len(input)
width = len(input[0])
arr = np.zeros([height, width], dtype="U8")
m = 0
for i in input:
    n = 0
    for j in i:
        arr[m][n] = j
        n += 1
    m += 1
arr2 = arr.copy()
arr3 = arr.copy()
arr_old = np.zeros([height, width], dtype="U8")

# Puzzle 1
rounds = 0
not_equal = True

while not_equal == True:
    arr_old = arr.copy()
    for i in range(height):
        for j in range(width):
            if arr[i][j] != ".":
                if arr[i][j] == "L":
                    count = 0
                    if i != 0 and j != 0:
                        try:
                            if arr[i-1][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if i != 0:
                        try:
                            if arr[i-1][j  ] == "#":
                                count += 1
                        except:
                            pass
                    if i != 0 and j != (width - 1):
                        try:
                            if arr[i-1][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if j != (width - 1):
                        try:
                            if arr[i  ][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1) and j != (width - 1):
                        try:
                            if arr[i+1][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1):
                        try:
                            if arr[i+1][j  ] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1) and j != 0:
                        try:
                            if arr[i+1][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if j != 0:
                        try:
                            if arr[i  ][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if count == 0:
                        arr2[i][j] = "#"
                if arr[i][j] == "#":
                    count = 0
                    if i != 0 and j != 0:
                        try:
                            if arr[i-1][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if i != 0:
                        try:
                            if arr[i-1][j  ] == "#":
                                count += 1
                        except:
                            pass
                    if i != 0 and j != (width - 1):
                        try:
                            if arr[i-1][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if j != (width - 1):
                        try:
                            if arr[i  ][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1) and j != (width - 1):
                        try:
                            if arr[i+1][j+1] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1):
                        try:
                            if arr[i+1][j  ] == "#":
                                count += 1
                        except:
                            pass
                    if i != (height - 1) and j != 0:
                        try:
                            if arr[i+1][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if j != 0:
                        try:
                            if arr[i  ][j-1] == "#":
                                count += 1
                        except:
                            pass
                    if count >= 4:
                        arr2[i][j] = "L"

    arr = arr2.copy()

    # are old and new array not the same?
    not_equal = False
    for i in range(height):
        for j in range(width):
            if arr[i][j] != arr_old[i][j]:
                not_equal = True

    rounds += 1

# count occupied seats
count = 0
for i in range(height):
    for j in range(width):
        if arr[i][j] == "#":
            count += 1

print("First Puzzle:", count)


# Puzzle 2
rounds = 0
not_equal = True
arr = arr3.copy()

while not_equal == True:
    arr_old = arr.copy()
    for i in range(height):
        for j in range(width):
            if arr[i][j] != ".":
                if arr[i][j] == "L":
                    count = 0
                    # going up
                    m = i - 1
                    while m > -1:
                        if arr[m][j] == "L":
                            m = -1
                        elif arr[m][j] == "#":
                            m = -1
                            count += 1
                        m -= 1
                    
                    # going down
                    m = i + 1
                    while m < height:
                        if arr[m][j] == "L":
                            m = height
                        elif arr[m][j] == "#":
                            m = height
                            count += 1
                        m += 1

                    # going left
                    m = j - 1
                    while m > -1:
                        if arr[i][m] == "L":
                            m = -1
                        elif arr[i][m] == "#":
                            m = -1
                            count += 1
                        m -= 1

                    # going right
                    m = j + 1
                    while m < width:
                        if arr[i][m] == "L":
                            m = width
                        elif arr[i][m] == "#":
                            m = width
                            count += 1
                        m += 1

                    # going up and left
                    m = i - 1
                    n = j - 1
                    while m > -1 and n > -1:
                        if arr[m][n] == "L":
                            m = -1
                            n = -1
                        elif arr[m][n] == "#":
                            m = -1
                            n = -1
                            count += 1
                        m -= 1
                        n -= 1

                    # going up and right
                    m = i - 1
                    n = j + 1
                    while m > -1 and n < width:
                        if arr[m][n] == "L":
                            m = -1
                            n = width
                        elif arr[m][n] == "#":
                            m = -1
                            n = width
                            count += 1
                        m -= 1
                        n += 1

                    # going down and right
                    m = i + 1
                    n = j + 1
                    while m < height and n < width:
                        if arr[m][n] == "L":
                            m = height
                            n = width
                        elif arr[m][n] == "#":
                            m = height
                            n = width
                            count += 1
                        m += 1
                        n += 1

                    # going down and left
                    m = i + 1
                    n = j - 1
                    while m < height and n > -1:
                        if arr[m][n] == "L":
                            m = height
                            n = -1
                        elif arr[m][n] == "#":
                            m = height
                            n = -1
                            count += 1
                        m += 1
                        n -= 1
                    if count == 0:
                        arr2[i][j] = "#"
                
                if arr[i][j] == "#":
                    count = 0
                    # going up
                    m = i - 1
                    while m > -1:
                        if arr[m][j] == "L":
                            m = -1
                        elif arr[m][j] == "#":
                            m = -1
                            count += 1
                        m -= 1
                    
                    # going down
                    m = i + 1
                    while m < height:
                        if arr[m][j] == "L":
                            m = height
                        elif arr[m][j] == "#":
                            m = height
                            count += 1
                        m += 1

                    # going left
                    m = j - 1
                    while m > -1:
                        if arr[i][m] == "L":
                            m = -1
                        elif arr[i][m] == "#":
                            m = -1
                            count += 1
                        m -= 1

                    # going right
                    m = j + 1
                    while m < width:
                        if arr[i][m] == "L":
                            m = width
                        elif arr[i][m] == "#":
                            m = width
                            count += 1
                        m += 1

                    # going up and left
                    m = i - 1
                    n = j - 1
                    while m > -1 and n > -1:
                        if arr[m][n] == "L":
                            m = -1
                            n = -1
                        elif arr[m][n] == "#":
                            m = -1
                            n = -1
                            count += 1
                        m -= 1
                        n -= 1

                    # going up and right
                    m = i - 1
                    n = j + 1
                    while m > -1 and n < width:
                        if arr[m][n] == "L":
                            m = -1
                            n = width
                        elif arr[m][n] == "#":
                            m = -1
                            n = width
                            count += 1
                        m -= 1
                        n += 1

                    # going down and right
                    m = i + 1
                    n = j + 1
                    while m < height and n < width:
                        if arr[m][n] == "L":
                            m = height
                            n = width
                        elif arr[m][n] == "#":
                            m = height
                            n = width
                            count += 1
                        m += 1
                        n += 1

                    # going down and left
                    m = i + 1
                    n = j - 1
                    while m < height and n > -1:
                        if arr[m][n] == "L":
                            m = height
                            n = -1
                        elif arr[m][n] == "#":
                            m = height
                            n = -1
                            count += 1
                        m += 1
                        n -= 1
                    
                    if count >= 5:
                        arr2[i][j] = "L"

    arr = arr2.copy()

    # are old and new array not the same?
    not_equal = False
    for i in range(height):
        for j in range(width):
            if arr[i][j] != arr_old[i][j]:
                not_equal = True

    rounds += 1

# count occupied seats
count = 0
for i in range(height):
    for j in range(width):
        if arr[i][j] == "#":
            count += 1


print("Second Puzzle:", count)
