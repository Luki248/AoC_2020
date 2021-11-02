# Advent of Code
# Day 6
# https://adventofcode.com/2020/day/6

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]
input.append("")    # to go sure that the last counting will be added to count_yes

count_yes = 0
count_yes_all = 0
new_group = True

letters = []
letters_all = []
for line in input:
    
    if line != "":
        
        # Puzzle 1
        for j in line:
            is_in_letters = False
            for k in letters:
                if k == j:
                    is_in_letters = True
            if is_in_letters == False:
                letters.append(j)

        # Puzzle 2
        # if new group (after empty line) is ahead
        if new_group == True:
            new_group = False
            for j in line:
                letters_all.append(j)
        else:
            temp_list = []
            for _ in range(len(letters_all)):
                temp_list.append("0")
            
            for j in line:
                for k in letters_all:
                    if j == k:
                        temp_list[letters_all.index(j)] = "1"
            
            # remove all letters, that are not in temp_list as 1 marked
            k = 0
            temp_list_2 = letters_all.copy()
            for j in temp_list:
                if j == "0":
                    letters_all.remove(temp_list_2[k])
                k += 1
            
    else:
        new_group = True

        # count letters and add to solution
        for j in letters:
            count_yes += 1

        # count letters of all and add to solution
        for j in letters_all:
            count_yes_all += 1

        letters = []
        letters_all = []


print("First Puzzle:", count_yes)
print("Second Puzzle:", count_yes_all)
