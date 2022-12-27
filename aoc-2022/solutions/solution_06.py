with open('inputs/input06.txt') as f:
    lines = f.read()


def parse_message(lines, n):
    for i in range(len(lines) - n):
        if len(set(lines[i:i + n])) == n:
            return i + n


print("start of datastream : ", parse_message(lines, 4))
print("start of message : ", parse_message(lines, 14))