import numpy as np

with open('inputs/input08.txt') as f:
    lines = f.readlines()

grid = []
for line in lines:
    grid.append([int(s) for s in line.strip()])

visibility = np.zeros((len(grid), len(grid[0])))

for i in range(len(grid)):
    max_left = -1
    max_right = -1
    max_top = -1
    max_bottom = -1
    for j in range(len(grid[0])):
        if max_left < grid[i][j]:
            visibility[i][j] = 1
            max_left = grid[i][j]
        if max_right < grid[i][len(grid) - j - 1]:
            visibility[i][len(grid) - j - 1] = 1
            max_right = grid[i][len(grid) - j - 1]
        if max_top < grid[j][i]:
            visibility[j][i] = 1
            max_top = grid[j][i]
        if max_bottom < grid[len(grid) - j - 1][len(grid) - i - 1]:
            visibility[len(grid) - j - 1][len(grid) - i - 1] = 1
            max_bottom = grid[len(grid) - j - 1][len(grid) - i - 1]
print("No of visible trees : ", sum(sum(visibility)))

# TODO : part 2

tree_dist_left = np.zeros((len(grid), len(grid[0])))
tree_dist_right = np.zeros((len(grid), len(grid[0])))
tree_dist_top = np.zeros((len(grid), len(grid[0])))
tree_dist_bottom = np.zeros((len(grid), len(grid[0])))
