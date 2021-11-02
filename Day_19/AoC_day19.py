# Advent of Code
# Day 19
# https://adventofcode.com/2020/day/19

input = [line.rstrip('\n') for line in open("input.txt")]

# import rules
rules = [0]*137
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
    if i >= 138:
        messages.append(line)
    i += 1

# get all possible messages
def get_possible_messages(rule_number, m_array):
    rule = rules[rule_number]
    if rule.count("|") == 1:
        if len(rule) > 3:
            temp1 = []
            i = 0
            while i < len(m_array):

                temp1 = []
                ret1 = get_possible_messages(rule[0], [""])
                j = 0
                while j < len(m_array):
                    for mes in ret1:
                        temp1.append(m_array[j] + mes)
                    j += 1

                ret1 = get_possible_messages(rule[1], [""])
                j = 0
                while j < len(m_array):
                    for mes in ret1:
                        temp1.append(m_array[j] + mes)
                    j += 1

                i += 1
            
            temp2 = []
            i = 0
            while i < len(m_array):
                
                temp2 = []
                ret1 = get_possible_messages(rule[3], [""])
                j = 0
                while j < len(m_array):
                    for mes in ret1:
                        temp2.append(m_array[j] + mes)
                    j += 1

                ret1 = get_possible_messages(rule[4], [""])
                j = 0
                while j < len(m_array):
                    for mes in ret1:
                        temp2.append(m_array[j] + mes)
                    j += 1

                i += 1

            temp = temp1
            for arr in temp2:
                temp.append(arr)
            return temp

        else:
            temp1 = []
            ret = get_possible_messages(rule[0], [""])
            i = 0
            while i < len(m_array):
                for mes in ret:
                    temp1.append(m_array[i] + mes)
                i += 1

            temp2 = []
            ret = get_possible_messages(rule[2], [""])
            i = 0
            while i < len(m_array):
                for mes in ret:
                    temp2.append(m_array[i] + mes)
                i += 1

            temp = temp1
            for arr in temp2:
                temp.append(arr)
            return temp
    else:
        if len(rule) == 2:
            temp = []
            i = 0
            while i < len(m_array):
                ret = get_possible_messages(rule[0], [""])
                for mes in ret:
                    temp.append(m_array[i] + mes)
                i += 1
            
            i = 0
            while i < len(m_array):
                ret = get_possible_messages(rule[1], [""])
                for mes in ret:
                    temp.append(m_array[i] + mes)
                i += 1
            return temp

        else:
            if rule[0] == "a" or rule[0] == "b":
                i = 0
                while i < len(m_array):
                    m_array[i] += rule[0]
                    i += 1
                return m_array
            else:
                temp = []
                i = 0
                while i < len(m_array):
                    ret = get_possible_messages(rule[0], [""])
                    for mes in ret:
                        temp.append(m_array[i] + mes)
                    i += 1
                return temp


# Puzzle 1
possible_messages = get_possible_messages(0, [""])
correct_messages = 0
for mes in messages:
    pass
    #if match(mes):
    #    correct_messages += 1
print("First Puzzle:", correct_messages)


# Puzzle 2

print("Second Puzzle:")
