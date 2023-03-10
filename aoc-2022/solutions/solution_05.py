with open('inputs/input05.txt') as f:
    lines = f.readlines()

# TODO : the stack input also from input file
stack_9000 = {1: ["B", "G", "S", "C"],
              2: ["T", "M", "W", "H", "J", "N", "V", "G"],
              3: ["M", "Q", "S"],
              4: ["B", "S", "L", "T", "W", "N", "M"],
              5: ["J", "Z", "F", "T", "V", "G", "W", "P"],
              6: ["C", "T", "B", "G", "Q", "H", "S"],
              7: ["T", "J", "P", "B", "W"],
              8: ["G", "D", "C", "Z", "F", "T", "Q", "M"],
              9: ["N", "S", "H", "B", "P", "F"]}


def crate_mover_9000(crates, move):
    move = move.split()
    no_of_moves = move[1]
    from_stack = move[3]
    to_stack = move[5]
    for i in range(int(no_of_moves)):
        x = crates[int(from_stack)].pop()
        crates[int(to_stack)].append(x)
    return crates


# Part 1
lines = lines[10:]
for line in lines:
    stack_9000 = crate_mover_9000(stack_9000, line)

top_items = []
for key, value in stack_9000.items():
    top_items.append(value[-1])
print("Top items for crate mover 9000 : ", ''.join(top_items))


# Part 2
def crate_mover_9001(stacks_9001, move):
    move = move.split()
    no_of_crates = int(move[1])
    from_stack = int(move[3])
    to_stack = int(move[5])
    x = stacks_9001[from_stack][-no_of_crates:]
    for i in range(no_of_crates):
        stacks_9001[from_stack].pop()
    for c in x:
        stacks_9001[to_stack].append(c)

    return stacks_9001


# Part Two
stack_9001 = {1: ["B", "G", "S", "C"],
              2: ["T", "M", "W", "H", "J", "N", "V", "G"],
              3: ["M", "Q", "S"],
              4: ["B", "S", "L", "T", "W", "N", "M"],
              5: ["J", "Z", "F", "T", "V", "G", "W", "P"],
              6: ["C", "T", "B", "G", "Q", "H", "S"],
              7: ["T", "J", "P", "B", "W"],
              8: ["G", "D", "C", "Z", "F", "T", "Q", "M"],
              9: ["N", "S", "H", "B", "P", "F"]}

for line in lines:
    stack_9001 = crate_mover_9001(stack_9001, line)

top_items = []
for key, value in stack_9001.items():
    top_items.append(value[-1])
print("Top items for crate mover 9000 : ", ''.join(top_items))
