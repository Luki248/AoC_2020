# Advent of Code
# Day 18
# https://adventofcode.com/2020/day/18


input = [line.rstrip('\n') for line in open("input.txt")]

calculations = [[]]
i = 0
while i < len(input):
    calculations.append([])
    j = 0
    while j < len(input[i]):
        if input[i][j] != " ":
            calculations[i].append(input[i][j])
        j += 1
    i += 1
calculations.remove([])


# Puzzle 1
def parse_calc(calc):

    if len(calc) == 0:
        print("Can not process string of length 0!")
        return None

    if (len(calc) == 1):
        if (calc[0] != "(") or (calc[0] != ")"):
            return int(calc[0])
        else:
            print("Can not process one parentheses!")
            return None

    if len(calc) == 2:
        print("Can not process string of length 2!")
        return None

    if len(calc) == 3:
        if calc[1] == "+":
            return int(calc[0]) + int(calc[2])
        else:
            return int(calc[0]) * int(calc[2])

    # if there are no parentheses in back of string calc
    if calc[-1] != "(" and calc[-1] != ")":
        res2 = parse_calc(calc[0:-2])
        if res2 == None:
            return None
        if calc[-2] == "+":
            return int(calc[-1]) + res2
        else:
            return int(calc[-1]) * res2

    # if parentheses are in last position of string calc
    if calc[-1] == ")":
        first_parentheses_close = len(calc) - 2
        parentheses_count = 1
        while parentheses_count != 0:
            if calc[first_parentheses_close] == "(":
                parentheses_count -= 1
            if calc[first_parentheses_close] == ")":
                parentheses_count += 1
            first_parentheses_close -= 1

        res2 = parse_calc(calc[(first_parentheses_close + 2):-1])
        temp = calc
        calc = temp[0:(first_parentheses_close + 1)]
        calc.append(str(res2))
        return parse_calc(calc)

sum = 0
for calc in calculations:
    res = parse_calc(calc)
    sum += res
print("First Puzzle:", sum)


# Puzzle 2
def parse_calc2(calc):

    if len(calc) == 0:
        print("Can not process string of length 0!")
        return None

    if (len(calc) == 1):
        if (calc[0] != "(") or (calc[0] != ")"):
            return int(calc[0])
        else:
            print("Can not process one parentheses!")
            return None

    if len(calc) == 2:
        print("Can not process string of length 2!")
        return None

    if len(calc) == 3:
        if calc[1] == "+":
            return int(calc[0]) + int(calc[2])
        else:
            return int(calc[0]) * int(calc[2])

    # if there is a term with no parentheses => account for + before *
    if calc.count("(") == 0 and calc.count(")") == 0:
        if calc[1] == "+":
            res = parse_calc2(calc[0:3])
            return parse_calc2([res] + calc[3:])
        if calc[-2] == "+":
            res = parse_calc2(calc[-3:])
            return parse_calc2(calc[0:-3] + [res])
        # if there is no "+" in calc
        if calc.count("+") == 0:
            calc_string = ""
            for i in calc:
                calc_string += str(i)
            return eval(calc_string)
        # if there is a "+" in the middle
        if calc[3] == "+":
            res = parse_calc2(calc[2:5])
            return parse_calc2(calc[0:2] + [res] + calc[5:])
        res = parse_calc2(calc[0:3])
        return parse_calc2([res] + calc[3:])
        
    # if there are no parentheses in back of string calc
    if calc[-1] != "(" and calc[-1] != ")":
        res2 = parse_calc2(calc[0:-2])
        if res2 == None:
            return None
        if calc[-2] == "+":
            return int(calc[-1]) + res2
        else:
            return int(calc[-1]) * res2

    # if parentheses are in last position of string calc
    if calc[-1] == ")":
        first_parentheses_close = len(calc) - 2
        parentheses_count = 1
        while parentheses_count != 0:
            if calc[first_parentheses_close] == "(":
                parentheses_count -= 1
            if calc[first_parentheses_close] == ")":
                parentheses_count += 1
            first_parentheses_close -= 1

        res2 = parse_calc2(calc[(first_parentheses_close + 2):-1])
        temp = calc
        calc = temp[0:(first_parentheses_close + 1)]
        calc.append(str(res2))
        return parse_calc2(calc)

sum = 0
for calc in calculations:
    res = parse_calc2(calc)
    sum += res
print("Second Puzzle:", sum)
