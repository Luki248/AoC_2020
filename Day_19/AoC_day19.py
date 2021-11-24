# Advent of Code
# Day 19
# https://adventofcode.com/2020/day/19

input = [line.rstrip('\n') for line in open("input.txt")]

# import rules
#rules = [0]*137
rules = [0]*6
for line in input:
    if line == "":
        break
    temp = line.split(":")
    index = int(temp[0])

    if temp[1].count("|") == 1:
        temp2 = temp[1].split(" ")
        if len(temp2) > 4:
            rule = []
            rule.append(int(temp2[1]))
            rule.append(int(temp2[2]))
            rule.append(temp2[3])
            rule.append(int(temp2[4]))
            rule.append(int(temp2[5]))
        else:
            rule = []
            rule.append(int(temp2[1]))
            rule.append(temp2[2])
            rule.append(int(temp2[3]))
    else:
        temp2 = temp[1].split(" ")
        if len(temp2) > 2:
            rule = []
            rule.append(int(temp2[1]))
            rule.append(int(temp2[2]))
        else:
            if temp2[1] == '"a"' or temp2[1] == '"b"':
                rule = []
                rule.append(temp2[1][1])
            else:
                rule = []
                rule.append(int(temp2[1]))

    rules[index] = rule


# import messages
messages = []
i = 0
for line in input:
    #if i >= 138:
    if i >= 7:
        messages.append(line)
    i += 1


# test if message match
def test_message(rule_number, message, mess_index=0):
    rule = rules[rule_number]
    if rule.count("|") == 1:    # split of rules (... | ...)
        if len(rule) > 3:   # more than one rule in any side (... ... | ... ...)
            ret1 = test_message(rule[0], message, mess_index)
            ret2 = test_message(rule[1], message, mess_index + 1)
            ret3 = test_message(rule[3], message, mess_index)
            ret4 = test_message(rule[4], message, mess_index + 1)
            return (ret1 and ret2) or (ret3 and ret4)

        else:   # only two rules (... | ...)
            ret1 = test_message(rule[0], message, mess_index)
            ret2 = test_message(rule[2], message, mess_index)
            return ret1 or ret2

    else:
        if len(rule) == 2:  # two rules (... ...)
            ret1 = test_message(rule[0], message, mess_index)
            ret2 = test_message(rule[1], message, mess_index + 1)
            return ret1 and ret2
            
        elif len(rule) == 3:    # tree rules (... ... ...)
            ret1 = test_message(rule[0], message, mess_index)
            ret2 = test_message(rule[1], message, mess_index + 1)
            ret3 = test_message(rule[3], message, mess_index + 2)
            return ret1 and ret2 and ret3

        else:   # one rule ("a") or ("b") or (...)
            if rule[0] == "a" or rule[0] == "b":    # char "a" or "b"
                return rule[0] == message[mess_index]
            else:   # one rule (...)
                return test_message(rule[0], message, mess_index)


# Puzzle 1
count_correct_messages = 0
for mes in messages:
    if test_message(0, mes):
        count_correct_messages += 1
print("First Puzzle:", count_correct_messages)


# Puzzle 2

print("Second Puzzle:")
