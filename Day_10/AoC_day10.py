# Advent of Code
# Day 10
# https://adventofcode.com/2020/day/10

input = [int(line.rstrip('\n')) for line in open("input.txt")]

# are there multiple chargers? No!!
'''
for i in range(len(input)):
    for j in range(len(input)):
        if i != j:
            if input[i] == input[j]:
                print("True")
'''

# sorted list
chargers_sorted = input.copy()
chargers_sorted.sort()

# Puzzle 1
counting_diff = [1, 0, 1]   # starting at 1 because starting from 0 and last adapter is in device with 3 jolts difference
for i in range(len(chargers_sorted) - 1):
    if chargers_sorted[i] + 1 == chargers_sorted[i+1]:  # 1 difference
        counting_diff[0] += 1
    elif chargers_sorted[i] + 2 == chargers_sorted[i+1]:  # 2 difference
        counting_diff[1] += 1
    elif chargers_sorted[i] + 3 == chargers_sorted[i+1]:  # 3 difference
        counting_diff[2] += 1
print("First Puzzle:", counting_diff[0] * counting_diff[2])

# Puzzle 2
depth = 0
def check_arrengements(list):
    global depth
    depth += 1
    count = 0
    if len(list) > 3:
        '''
        for i in range(len(list) - 3):
            if list[i] + 3 == list[i+3]:  # at 3 difference is 3 higher?
                list2 = list.copy()[i:1000]
                list2.pop(2)
                count += 1
                count += check_arrengements(list2)
                list2 = list.copy()[i:1000]
                list2.pop(1)
                count += 1
                count += check_arrengements(list2)
            elif list[i] + 3 == list[i+2]:  # at 2 difference is 3 higher?
                list2 = list.copy()[i:1000]
                list2.pop(1)
                count += 1
                count += check_arrengements(list2)
            else:
                pass # do nothing
        '''
        
        i = 0
        if list[i] + 3 == list[i+3]:  # at 3 difference is 3 higher?
            list2 = list.copy()[i:1000]
            list2.pop(2)
            count += 1
            count *= check_arrengements(list2)
            list2 = list.copy()[i:1000]
            list2.pop(1)
            count += 1
            count *= check_arrengements(list2)
        elif list[i] + 3 == list[i+2]:  # at 2 difference is 3 higher?
            list2 = list.copy()[i:1000]
            list2.pop(1)
            count += 1
            count *= check_arrengements(list2)
        else:
            count += 1
            count *= check_arrengements(list[1:1000])

    print(count, len(list), depth)
    depth -= 1
    return count


chargers_sorted.insert(0, 0)
chargers_sorted.append(183)
print("Second Puzzle:", check_arrengements(chargers_sorted))
print("end")
