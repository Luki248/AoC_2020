# Advent of Code
# Day 7
# https://adventofcode.com/2020/day/7

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]

bag_to_find = "shiny gold bag"
occurs = []

# Puzzle 1
def find_bag(func_count, to_find):
    if func_count > 6:
        return
    
    for line in input:
        if line.count(to_find) >= 1:
            temp = line.split(" contain ")
            if temp[0].count(bag_to_find) == 0:
                temp2 = temp[0][0:-1]
                if occurs.count(temp2) == 0:
                    occurs.append(temp2)
                find_bag(func_count + 1, temp2)

find_bag(0, bag_to_find)

# Puzzle 2
def find_bag_number(to_find):
    num_of_bag = 1

    for line in input:
        temp = line.split(" contain ")
        if temp[0].count(to_find) == 1:
            temp2 = temp[1].split(", ")
            if temp[1].count("no other bags") == 1:
                return num_of_bag
            else:
                for bag in temp2:
                    numbers_of_bag = int(bag.split(" ")[0])
                    if bag[-1] == ".":
                        bag = bag[0:-1]
                    num_of_bag += numbers_of_bag * find_bag_number(bag[2:100])

    return num_of_bag
    
count_bags = 0
for line in input:
    temp = line.split(" contain ")
    if temp[0].count(bag_to_find) == 1:
        temp2 = temp[1].split(", ")
        for i in temp2:
            numbers_of_bag = int(i.split(" ")[0])
            count_bags += numbers_of_bag * find_bag_number(i[2:-1])


print("First Puzzle:", len(occurs))
print("Second Puzzle:", count_bags)
