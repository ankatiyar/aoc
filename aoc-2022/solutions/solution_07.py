with open('inputs/input07.txt') as f:
    lines = f.read()
# Part One
commands = lines.split('$')[1:]


class Tree:
    def __init__(self, name, size, type, parent, children):
        self.name = name
        self.size = size
        self.type = type
        self.parent = parent
        self.children = children

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def add_children(self, children):
        for child in children:
            split_child = child.split()
            if split_child[0] == "dir":
                new_child = Tree(split_child[1], 0, "dir", self, [])
                self.add_child(new_child)
            else:
                new_child = Tree(split_child[1], int(split_child[0]), "file", self, [])
                self.add_child(new_child)
        return self

    def get_info(self):
        print("Name : ", self.name, "Size : ", self.size)


curr = Tree('/', 0, "dir", None, [])
root = curr


def parse_command(root, current, command):
    split_command = command.split('\n')
    # print(split_command)
    if split_command[0] == " cd ..":
        # print("Going back one level")
        return current.parent
    elif split_command[0] == " cd /":
        # print("going to root")
        return root
    elif split_command[0] == " ls":
        # print("Listing files")
        return current.add_children(split_command[1:-1])
    else:
        # print("Change directory")
        for child in current.children:
            if child.name == split_command[0].split()[1]:
                return child
        return current


def dfs(root):
    if root:
        for child in root.children:
            if child:
                root.size += dfs(child)
    return root.size


def inorder(root, visited):
    if root:
        visited.append([root.name, root.size])
        for c in root.children:
            visited = inorder(c, visited)
    return visited


for command in commands:
    curr = parse_command(root, curr, command)


def dir_list(root, size_list):
    if root.type == "dir":
        size_list.append(root.size)
        for child in root.children:
            size_list = dir_list(child, size_list)
    return size_list


dfs(root)
directories = dir_list(root, [])
sum_of_directories = 0
for x in directories:
    if x <= 100000:
        sum_of_directories += x

print("Sum of directories of size <= 100000 : ", sum_of_directories)

# Part Two
free_space = 70000000 - root.size
required_space = 30000000 - free_space

x = [y - required_space for y in directories]
x.sort()

smallest_dir = 0
for i in x:
    if i > 0:
        smallest_dir = i + required_space
        break

print("Smallest directory you can delete : ", smallest_dir)
