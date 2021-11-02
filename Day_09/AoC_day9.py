# Advent of Code
# Day 9
# https://adventofcode.com/2020/day/9

input = [int(line.rstrip('\n')) for line in open("input.txt")]

# Puzzle 1
for i in input:
    if input.index(i) < 25:  # do nothing with Preamble
        continue
    
    sum_found = False
    for j in range(input.index(i) - 25, input.index(i)):
        for l in range(input.index(i) - 25, input.index(i)):
            if j != l:
                if input[j] + input[l] == i:
                    sum_found = True
    
    if sum_found == False:
        invalid_number = i
        print("First Puzzle:", i)

# Puzzle 2
smallest = 0
largest = 0
found = False
for i in input:
    #print(input.index(i))
    for j in input:
        k = input.index(i)
        sum = 0
        while k <= input.index(j):
            sum += input[k]
            if sum > invalid_number:
                break
            if sum == invalid_number:
                m = input.index(i)
                smallest = input[m]
                largest = input[m]
                while m < input.index(j):   # find smallest and largest numbers
                    if input[m] < smallest:
                        smallest = input[m]
                    if input[m] > largest:
                        largest = input[m]
                    m += 1
                sum_l_s = smallest + largest
                found = True
            k += 1
            if found == True:
                break
        if found == True:
            break
    if found == True:
        break

print("Second Puzzle:", sum_l_s)