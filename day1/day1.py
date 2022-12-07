
f = open("input.txt", "r")

lines = []
for line in f:
    lines.append(line.rstrip())

elves = []
elf = 0
for l in lines:
    if l == '':
        elves.append(elf)
        elf = 0
        continue
    elf += int(l)
# last elf not handled in loop
elves.append(elf)

elves.sort()

# part 1
print(max(elves))

# part 2
print(sum(elves[-3:]))
