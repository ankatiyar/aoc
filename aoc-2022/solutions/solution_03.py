with open('inputs/input03.txt') as f:
    lines = f.readlines()


def get_priority(c):
    if c.islower():
        priority = ord(c) - 96
    elif c.isupper():
        priority = ord(c) - 38
    else:
        priority = 0
    return priority


total = 0
for line in lines:
    compartment1 = line[:len(line) // 2].strip()
    compartment2 = line[len(line) // 2:].strip()
    common = ''.join(set(compartment1).intersection(compartment2))
    priority = 0
    for c in common:
        priority += get_priority(c)
    total += priority
print("Total for part1:", total)

total = 0
for i in range(0, len(lines), 3):
    bag1 = lines[i].strip()
    bag2 = lines[i+1].strip()
    bag3 = lines[i+2].strip()
    common = set(bag1) & set(bag2) & set(bag3)
    total += get_priority(common.pop())

print("Total for part2:", total)
