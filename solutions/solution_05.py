with open('inputs/input05.txt') as f:
    lines = f.readlines()

# TODO : the stack input also from input file
stacks = {1: ["B", "G", "S", "C"],
          2: ["T", "M", "W", "H", "J", "N", "V", "G"],
          3: ["M", "Q", "S"],
          4: ["B", "S", "L", "T", "W", "N", "M"],
          5: ["J", "Z", "F", "T", "V", "G", "W", "P"],
          6: ["C", "T", "B", "G", "Q", "H", "S"],
          7: ["T", "J", "P", "B", "W"],
          8: ["G", "D", "C", "Z", "F", "T", "Q", "M"],
          9: ["N", "S", "H", "B", "P", "F"]}


def crate_mover_9000(stacks, move):
    move = move.split()
    no_of_moves = move[1]
    from_stack = move[3]
    to_stack = move[5]
    for i in range(int(no_of_moves)):
        x = stacks[int(from_stack)].pop()
        stacks[int(to_stack)].append(x)
    return stacks


# Part 1
lines = lines[10:]
stack_9000 = stacks
for line in lines:
    stack_9000 = crate_mover_9000(stack_9000, line)

top_items = []
for key, value in stack_9000.items():
    top_items.append(value[-1])

print("Top items for crate mover 9000 : ", ''.join(top_items))


# Part 2
# TODO: not correct
def crate_mover_9001(stacks, move):
    move = move.split()
    no_of_crates = int(move[1])
    from_stack = int(move[3])
    to_stack = int(move[5])
    print(no_of_crates, stacks[from_stack], stacks[to_stack])

    x = stacks[from_stack][-no_of_crates:]
    for i in range(no_of_crates):
        stacks[from_stack].pop()
    for c in x:
        stacks[to_stack].append(c)

    return stacks


stack_9001 = stacks
lines = lines[:2]
for line in lines:
    stack_9001 = crate_mover_9001(stack_9001, line)

top_items = []
for key, value in stack_9001.items():
    print(key, value)


print("Top items for crate mover 9001 : ", ''.join(top_items))
