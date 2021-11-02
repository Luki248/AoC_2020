# Advent of Code
# Day 14
# https://adventofcode.com/2020/day/14

import numpy as np

input = [line.rstrip('\n') for line in open("input.txt")]

# Puzzle 1
memory = np.zeros([2**16, 36], dtype="int") # memory for puzzle 1
mask = [0] * 36
end_loop = False
for i in range(len(input)):
    if input[i][1] == "a" and len(input[i]) > 5:
        temp = input[i].split(" ")[2]
        k = 0
        while k < len(temp):
            if temp[k] == "X":
                mask[k] = "X"
            else:
                mask[k] = temp[k]
            k += 1

        j = i + 1
        while input[j][1] != "a" and len(input[j]) > 5:
            temp = input[j].split("[")
            temp2 = temp[1].split("]")
            temp3 = temp2[1].split(" ")
            addr = int(temp2[0])
            temp4 = bin(int(temp3[2]))
            temp4 = temp4[2:36]
            value = "0" * (36 - len(temp4))
            value = value + temp4

            for k in range(36):
                if mask[k] == "0":
                    memory[addr][k] = 0
                elif mask[k] == "1":
                    memory[addr][k] = 1
                else:
                    if value[k] == "0":
                        memory[addr][k] = 0
                    else:
                        memory[addr][k] = 1

            j += 1

sum = 0
for mem in memory:
    i = 0
    j = len(mem) - 1
    while i < len(mem):
        sum += mem[j] * (2**i)
        i += 1
        j -= 1
print("First Puzzle:", sum)


# Puzzle 2
#memory2 = [0] * 1000000000
mask = [0] * 36
sum = 0
end_loop = False
for i in range(len(input)):
    print(i)
    if input[i][1] == "a" and len(input[i]) > 5:
        temp = input[i].split(" ")[2]
        k = 0
        while k < len(temp):
            if temp[k] == "X":
                mask[k] = "X"
            else:
                mask[k] = temp[k]
            k += 1

        j = i + 1
        while input[j][1] != "a" and len(input[j]) > 5:
            temp = input[j].split("[")
            temp2 = temp[1].split("]")
            temp3 = temp2[1].split(" ")
            addr = int(temp2[0])
            value = int(temp3[2])

            # get all adresses
            addresses = np.zeros([1, 36], dtype="int")
            temp5 = bin(addr)[2:36]
            addr_bin = "0" * (36 - len(temp5))
            addr_bin = addr_bin + temp5
            
            for k in range(36):
                if mask[k] == "0":
                    pass
                elif mask[k] == "1":
                    for l in range(len(addresses)):
                        addresses[l][k] = 1
                else:
                    len_addresses = len(addresses)
                    for l in range(len_addresses):
                        addresses[l][k] = 0
                    for l in range(len_addresses):
                        temp6 = np.copy(addresses[l])
                        temp6[k] = 1
                        addresses = np.append(addresses, [temp6], axis=0)
                    
            normal_adresses = []
            for adr in addresses:
                add = 0
                l = 0
                k = len(adr) - 1
                while l < len(adr):
                    add += adr[k] * (2**l)
                    l += 1
                    k -= 1
                normal_adresses.append(add)

            for k in range(len(normal_adresses)):
                #memory2[k] = value
                sum += value

            j += 1

print("Second Puzzle:", sum)
