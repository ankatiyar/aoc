with open('../inputs/input04.txt') as f:
    lines = f.readlines()

count1 = 0
count2 = 0
for line in lines:
    line = line.strip()
    elf1, elf2 = line.split(',')
    min1, max1 = elf1.split('-')
    min2, max2 = elf2.split('-')
    print(min1, max1, min2, max2)
    if (int(min2) >= int(min1) and int(max2) <= int(max1)) or (int(min1) >= int(min2) and int(max1) <= int(max2)):
        # complete overlap
        count1 += 1
        count2 += 1
        print("Yes")
    elif int(min1) > int(max2) or int(min2) > int(max1):
        # no overlap at all
        pass
    else:
        # partial overlap
        count2 += 1
print("Count of total overlaps:", count1)
print("Count of partial overlaps: ", count2)
