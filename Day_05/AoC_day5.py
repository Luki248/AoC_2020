# Advent of Code
# Day 5
# https://adventofcode.com/2020/day/5

input = [line.rstrip('\n') for line in open("input.txt")]

highest = 0
puzzle_seats = []

# Puzzle 1
for strings in input:

    row = 0
    j = 6
    for i in range(0, 7):
        k = j - i
        if strings[k] == "B":
            row += 2**(i)
    
    column = 0
    j = 9
    for i in range(7, 10):
        k = 7 + j - i
        if strings[k] == "R":
            column += 2**(i - 7)

    seat = row * 8 + column
    puzzle_seats.append(seat)
    if seat > highest:
        highest = seat
print("First Puzzle:", highest)

# Puzzle 2
puzzle_seats.sort()
for i in puzzle_seats:
    if i < 773:
        if (puzzle_seats[i+1] - puzzle_seats[i]) == 2:
            print("Second Puzzle:", puzzle_seats[i] + 1)

