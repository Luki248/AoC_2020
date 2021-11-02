# Advent of Code
# Day 22
# https://adventofcode.com/2020/day22

input = [line.rstrip('\n') for line in open("input.txt")]

player_1 = []
player_2 = []
for_pl_1 = True
for line in input:
    if len(line) > 0:
        if line[0] == "P":
            if line[7] == "1":
                for_pl_1 = True
            else:
                for_pl_1 = False
        else:
            if for_pl_1 == True:
                player_1.append(int(line))
            else:
                player_2.append(int(line))

player_1_start = player_1.copy()
player_2_start = player_2.copy()

# Puzzle 1
while len(player_1) > 0 and len(player_2) > 0:
    if player_1[0] > player_2[0]:
        player_1.append(player_1[0])
        player_1.append(player_2[0])
    else:
        player_2.append(player_2[0])
        player_2.append(player_1[0])
    player_1.pop(0)
    player_2.pop(0)

sum = 0
if len(player_1) > 0:
    i = len(player_1)
    j = 0
    while i > 0:
        sum += i * player_1[j]
        i -= 1
        j += 1
else:
    i = len(player_2)
    j = 0
    while i > 0:
        sum += i * player_2[j]
        i -= 1
        j += 1
print("First Puzzle:", sum)


# Puzzle 2
player_1 = player_1_start.copy()
player_2 = player_2_start.copy()

all_card_occurences_1 = []
all_card_occurences_2 = []

def sub_game(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        #if p1[0] < len(p1) or p2[0] < len(p2):
        #    sub_game(p1[1:100], p2[1:100])

        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
        else:
            p2.append(p2[0])
            p2.append(p1[0])
        p1.pop(0)
        p2.pop(0)
    
    if len(p1) > 1:
        return 1
    else:
        return 2

while len(player_1) > 0 and len(player_2) > 0:
    temp1 = ""
    for card in player_1:
        temp1 = temp1 + str(card)
    if all_card_occurences_1.count(temp1) == 1:
        print("Player 1 wins")
        break
    else:
        all_card_occurences_1.append(temp1)

    temp2 = ""
    for card in player_2:
        temp2 = temp2 + str(card)
    if all_card_occurences_2.count(temp2) == 1:
        print("Player 1 wins")
        break
    else:
        all_card_occurences_2.append(temp2)

    if player_1[0] < len(player_1) or player_2[0] < len(player_2):
        ret = sub_game(player_1[1:(player_1[0] + 1)], player_2[1:(player_2[0] + 1)])

        if ret == 1:
            player_1.append(player_1[0])
            player_1.append(player_2[0])
        else:
            player_2.append(player_2[0])
            player_2.append(player_1[0])
        player_1.pop(0)
        player_2.pop(0)

    else:
        if player_1[0] > player_2[0]:
            player_1.append(player_1[0])
            player_1.append(player_2[0])
        else:
            player_2.append(player_2[0])
            player_2.append(player_1[0])
        player_1.pop(0)
        player_2.pop(0)

sum = 0
if len(player_1) > 0:
    i = len(player_1)
    j = 0
    while i > 0:
        sum += i * player_1[j]
        i -= 1
        j += 1
else:
    i = len(player_2)
    j = 0
    while i > 0:
        sum += i * player_2[j]
        i -= 1
        j += 1
print("Second Puzzle:", sum)
