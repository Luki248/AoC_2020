# Advent of Code
# Day 13
# https://adventofcode.com/2020/day/13

input = [line.rstrip('\n') for line in open("input.txt")]

# probably not used
def primefactorization(integer):
    primefactors = []
    i = integer - 1
    while i > 1:
        if integer % i == 0:
            primefactors.append(i)
        i -= 1
    
    return primefactors

# Puzzle 1
earliest_bus = int(input[0])
busses = []
temp = input[1].split(",")
for i in temp:
    if i != "x":
        busses.append(int(i))

timedifference = []
for i in busses:
    max_factor = int(earliest_bus / i) + 1
    timedifference.append((max_factor * i) - earliest_bus)

minimum_wait_time = min(timedifference)
busindex = timedifference.index(minimum_wait_time)

print("First Puzzle:", busses[busindex] * minimum_wait_time)


# Puzzle 2
temp = input[1].split(",")
busses = []
delays = []
i = 0
while i < len(temp):
    if temp[i] != "x":
        busses.append(int(temp[i]))
        delays.append(i)
    i += 1

busses_inc =[0] * 9
bus_counters = busses.copy()
timestamp = 100000000000000
end_loop = False
while end_loop == False:
    
    if busses_inc[8] - busses_inc[7] == delays[8]:
        #print(timestamp, "delay 7 - 8")
        pass
    elif busses_inc[7] - busses_inc[6] == delays[7]:
        #print(timestamp, "delay 6 - 7")
        pass
    elif busses_inc[6] - busses_inc[5] == delays[6]:
        #print(timestamp, "delay 5 - 6")
        pass
    elif busses_inc[5] - busses_inc[4] == delays[5]:
        #print(timestamp, "delay 4 - 5")
        pass
    elif busses_inc[4] - busses_inc[3] == delays[4]:
        #print(timestamp, "delay 3 - 4")
        pass
    elif busses_inc[3] - busses_inc[2] == delays[3]:
        #print(timestamp, "delay 2 - 3")
        pass
    elif busses_inc[2] - busses_inc[1] == delays[2]:
        #print(timestamp, "delay 1 - 2")
        pass
    elif busses_inc[1] - busses_inc[0] == delays[1]:
        #print(timestamp, "delay 0 - 1")
        end_loop = True
    else:
        pass
    
    for j in range(len(bus_counters)):
        bus_counters[j] = bus_counters[j] - 1
        if bus_counters[j] == -1:
            bus_counters[j] = busses[j]
            busses_inc[j] = timestamp

    print(timestamp, busses_inc)
    timestamp += 1

print("Second Puzzle:")
