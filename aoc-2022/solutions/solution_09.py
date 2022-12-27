with open('inputs/input09.txt') as f:
    lines = f.readlines()
lines = lines
h = [0, 0]
t = [0, 0]


def move_tail(head, tail):
    if touching(head, tail):
        pass
    elif two_step(head, tail):
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
        elif head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    else:
        if head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1
        else:
            tail[0] -= 1
            tail[1] += 1
    return tail


def touching(h, t):
    if h[0] == t[0] and h[1] == t[1]:
        return True
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return True
    return False


def two_step(h, t):
    if (abs(h[0] - t[0]) == 2 and h[1] == t[1]) or (abs(h[1] - t[1]) == 2 and h[0] == t[0]):
        return True
    else:
        return False


# Part one
visited = set()
for line in lines:
    dir = line.split()[0]
    step = int(line.split()[1])
    for i in range(step):
        if dir == "L":
            h[0] -= 1
        elif dir == "R":
            h[0] += 1
        elif dir == "U":
            h[1] += 1
        else:
            h[1] -= 1
        t = move_tail(h, t)
        visited.add((t[0], t[1]))

print("Positions visited by the tail at least once (part one) : ", len(visited))

# Part two
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = set()
for line in lines:
    dir = line.split()[0]
    step = int(line.split()[1])
    for i in range(step):
        if dir == "L":
            rope[0][0] -= 1
        elif dir == "R":
            rope[0][0] += 1
        elif dir == "U":
            rope[0][1] += 1
        else:
            rope[0][1] -= 1
        for j in range(1, 10):
            rope[j] = move_tail(rope[j - 1], rope[j])
        visited.add((rope[-1][0], rope[-1][1]))
print("Positions visited by tail at least once (part two) : ", len(visited))
