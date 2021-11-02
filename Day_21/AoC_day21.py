# Advent of Code
# Day 21
# https://adventofcode.com/2020/day21

input = [line.rstrip('\n') for line in open("input.txt")]

foods = []
allergenes = []
i = 0
for line in input:
    temp = line.split("(")
    temp2 = temp[0].split(" ")

    foods.append(temp2)
    foods[i].pop(-1)
    
    temp3 = temp[1].split(",")
    if len(temp3) == 1:
        temp4 = temp3[0].split(" ")
        temp4 = temp4[1].split(")")
        allergenes.append([temp4[0]])
    if len(temp3) == 2:
        temp4 = temp3[0].split(" ")
        temp5 = temp3[1].split(" ")
        temp5 = temp5[1].split(")")
        allergenes.append([temp4[1],temp5[0]])
    if len(temp3) == 3:
        temp4 = temp3[0].split(" ")
        temp5 = temp3[1].split(" ")
        temp6 = temp3[2].split(")")
        temp6 = temp6[0].split(" ")
        allergenes.append([temp4[1], temp5[1], temp6[1]])
    i += 1


# Puzzle 1
ingr_w_n_allerg = []

# get all ingredients
all_ingredients = []
for food in foods:
    for ingr in food:
        if all_ingredients.count(ingr) == 0:
            all_ingredients.append(ingr)

# get all allergenes
all_allergenes_n_alloc = []
for allerg in allergenes:
    for al in allerg:
        if all_allergenes_n_alloc.count(al) == 0:
            all_allergenes_n_alloc.append(al)

foods_with_1 = []
i = 0
while i < len(foods):
    if len(allergenes[i]) == 1:
        foods_with_1.append(i)
    i += 1

foods_with_corresp = []
for i in foods_with_1:
    search_allerg = allergenes[i]
    for j in foods_with_1:
        if i != j:
            if allergenes[j] == search_allerg:
                foods_with_corresp.append([i,j])

for index in foods_with_corresp:
    common = []
    
    # get all common ingredients
    for i in foods[index[0]]:
        for j in foods[index[1]]:
            if i == j:
                common.append(i)

    # all not common ingredients have no allergenes
    for ingr in foods[index[0]]:
        if common.count(ingr) == 0:
            if ingr_w_n_allerg.count(ingr) == 0:
                ingr_w_n_allerg.append(ingr)

# count occurences of ingredients with no allergenes in foods-list
count = 0
for food in foods:
    for ingr in food:
        if ingr_w_n_allerg.count(ingr) == 1:
            count += 1

print("First Puzzle:", count)


# Puzzle 2

print("Second Puzzle:")
