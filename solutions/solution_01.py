with open('../inputs/input01.txt') as f:
    lines = f.readlines()

elfs = []
curr = 0
for line in lines:
    if line != '\n':
        curr = curr + int(line)
    else:
        elfs.append(curr)
        curr = 0
elfs.sort()
print("Highest calorie : ", elfs[-1])
print("Sum of Top 3 :", sum(elfs[-3:]))