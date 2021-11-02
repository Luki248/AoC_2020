# Advent of Code
# Day 12
# https://adventofcode.com/2020/day/12

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]

# Puzzle 1
ship_pos = [0, 0]
ship_facing = "east"
for line in input:
    instruction = line[0]
    amount = int(line[1:100])

    if instruction == "N":
        ship_pos[0] += amount
    elif instruction == "E":
        ship_pos[1] += amount
    elif instruction == "S":
        ship_pos[0] -= amount
    elif instruction == "W":
        ship_pos[1] -= amount
    elif instruction == "L":
        if amount == 90:
            if ship_facing == "north":
                ship_facing = "west"
            elif ship_facing == "east":
                ship_facing = "north"
            elif ship_facing == "south":
                ship_facing = "east"
            elif ship_facing == "west":
                ship_facing = "south"
            else:
                pass
        elif amount == 180:
            if ship_facing == "north":
                ship_facing = "south"
            elif ship_facing == "east":
                ship_facing = "west"
            elif ship_facing == "south":
                ship_facing = "north"
            elif ship_facing == "west":
                ship_facing = "east"
            else:
                pass
        elif amount == 270:
            if ship_facing == "north":
                ship_facing = "east"
            elif ship_facing == "east":
                ship_facing = "south"
            elif ship_facing == "south":
                ship_facing = "west"
            elif ship_facing == "west":
                ship_facing = "north"
            else:
                pass
        elif amount == 0:
            pass
        else:
            print("unnowm command", instruction, amount)
    elif instruction == "R":
        if amount == 90:
            if ship_facing == "north":
                ship_facing = "east"
            elif ship_facing == "east":
                ship_facing = "south"
            elif ship_facing == "south":
                ship_facing = "west"
            elif ship_facing == "west":
                ship_facing = "north"
            else:
                pass
        elif amount == 180:
            if ship_facing == "north":
                ship_facing = "south"
            elif ship_facing == "east":
                ship_facing = "west"
            elif ship_facing == "south":
                ship_facing = "north"
            elif ship_facing == "west":
                ship_facing = "east"
            else:
                pass
        elif amount == 270:
            if ship_facing == "north":
                ship_facing = "west"
            elif ship_facing == "east":
                ship_facing = "north"
            elif ship_facing == "south":
                ship_facing = "east"
            elif ship_facing == "west":
                ship_facing = "south"
            else:
                pass
        elif amount == 0:
            pass
        else:
            print("unnowm command", instruction, amount)
    elif instruction == "F":
        if ship_facing == "north":
            ship_pos[0] += amount
        elif ship_facing == "east":
            ship_pos[1] += amount
        elif ship_facing == "south":
            ship_pos[0] -= amount
        elif ship_facing == "west":
            ship_pos[1] -= amount
        else:
            pass
    else:
        pass

manhattan_distance = abs(ship_pos[0]) + abs(ship_pos[1])
print("First Puzzle:", manhattan_distance)


# Puzzle 2
ship_pos = [0, 0]
ship_facing = "east"
waypoint_pos = [1, 10]
for line in input:
    instruction = line[0]
    amount = int(line[1:100])

    if instruction == "N":
        waypoint_pos[0] += amount
    elif instruction == "E":
        waypoint_pos[1] += amount
    elif instruction == "S":
        waypoint_pos[0] -= amount
    elif instruction == "W":
        waypoint_pos[1] -= amount
    elif instruction == "L":
        if amount == 90:
            y_new = waypoint_pos[1]
            x_new = (-1) * waypoint_pos[0]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 180:
            y_new = (-1) * waypoint_pos[0]
            x_new = (-1) * waypoint_pos[1]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 270:
            y_new = (-1) * waypoint_pos[1]
            x_new = waypoint_pos[0]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 0:
            pass
        else:
            print("unnowm command", instruction, amount)
    elif instruction == "R":
        if amount == 90:
            y_new = (-1) * waypoint_pos[1]
            x_new = waypoint_pos[0]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 180:
            y_new = (-1) * waypoint_pos[0]
            x_new = (-1) * waypoint_pos[1]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 270:
            y_new = waypoint_pos[1]
            x_new = (-1) * waypoint_pos[0]
            waypoint_pos[0] = y_new
            waypoint_pos[1] = x_new
        elif amount == 0:
            pass
        else:
            print("unnowm command", instruction, amount)
    elif instruction == "F":
        i = 0
        while i < amount:
            ship_pos[0] += waypoint_pos[0]
            ship_pos[1] += waypoint_pos[1]
            i += 1

        #waypoint_pos[0] = ship_pos[0] + 1
        #waypoint_pos[1] = ship_pos[1] + 10
    else:
        pass

manhattan_distance2 = abs(ship_pos[0]) + abs(ship_pos[1])

print("Second Puzzle:", manhattan_distance2)
