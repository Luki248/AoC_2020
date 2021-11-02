# Advent of Code
# Day 16
# https://adventofcode.com/2020/day/16

input = [line.rstrip('\n') for line in open("input.txt")]

vals1_min = []
vals1_max = []
vals2_min = []
vals2_max = []
myticket = []
nearbytickets = []

line_count = 0
for line in input:
    if line_count < 20:
        temp = line.split(":")
        temp1 = temp[1].split("or")
        temp2 = temp1[0].strip(" ")
        temp4 = temp2.split("-")
        vals1_min.append(int(temp4[0]))
        vals1_max.append(int(temp4[1]))
        temp3 = temp1[1].strip(" ")
        temp5 = temp3.split("-")
        vals2_min.append(int(temp5[0]))
        vals2_max.append(int(temp5[1]))

    if line_count == 22:
        temp = line.split(",")
        for i in temp:
            myticket.append(int(i))

    if line_count >= 25:
        temp = line.split(",")
        temp1 = []
        for i in temp:
            temp1.append(int(i))
        nearbytickets.append(temp1)

    line_count += 1

invalid_tickets = []

# Puzzle 1
error_rate = 0
j = 0
for ticket in nearbytickets:
    for number in ticket:
        is_valid = False
        i = 0
        while i < len(ticket):
            if (vals1_min[i] <= number <= vals1_max[i]) or (vals2_min[i] <= number <= vals2_max[i]):
                is_valid = True
            i += 1
        if is_valid == False:
            error_rate += number
            invalid_tickets.append(j)
            #print(j, number)
    j += 1
print("First Puzzle:", error_rate)


# Puzzle 2
i = len(invalid_tickets) - 1
while i >= 0:
    nearbytickets.pop(invalid_tickets[i])
    i -= 1

# matches of ticket position and field
matches = [[0]*len(nearbytickets[0])]*len(nearbytickets[0]) # if 1 in matrix, all position of ticket matches to position of field

# going through all position of tickets to find possible match
i = 0
while i < len(nearbytickets[0]):    # field after field of a ticket

    j = 0
    while j < len(nearbytickets[0]):    # all field positions on a ticket
        k = 0
        no_match = False
        while k < len(nearbytickets):   # all nearby tickets
            if not(vals1_min[i] <= nearbytickets[k][j] <= vals1_max[i]) or not(vals2_min[i] <= nearbytickets[k][j] <= vals2_max[i]):
                no_match = True
            k += 1
        
        if no_match == True:
            matches[i][j] = 1
        
        j += 1
    
    i += 1


print("Second Puzzle:")

