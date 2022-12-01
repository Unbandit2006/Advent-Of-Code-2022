# Advent of Code Day 1

elfs_inv = []
elf = 0

with open("Day1.txt", "r") as f:
    
    for line in f.readlines():
        if line != "\n":
            elf += int(line)
        
        else:
            elfs_inv.append(elf)
            elf = 0

top_three = []

greatest = max(elfs_inv)
top_three.append(greatest)
for i in range(2):
    elfs_inv.remove(greatest)
    greatest = max(elfs_inv)
    top_three.append(greatest)

total = 0
for elf in top_three:
    total += elf
top_three.append(total)

print(top_three)