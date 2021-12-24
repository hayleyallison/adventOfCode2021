# This was the first time I had to look up an existing alogrithm to solve. But I learned something!
import numpy as np

# Read in the input data
def read_input(filename):
    file = open(filename)
    data = file.read()
    file.close()

    lines = data.split()
    grid  = np.zeros((len(lines), len(lines[0])))

    iy = 0
    ix = 0
    for line in lines:
        for l in line:
            grid[iy,ix] = int(l)
            ix += 1
        iy += 1
        ix = 0
    return grid

# for part 2 expand the grid
def expand_grid(grid):
    xlen = len(grid[1,:])
    ylen = len(grid[:,1])
    expanded_grid = np.zeros((ylen*5, xlen*5))
    new_grid = grid

    expanded_grid[0:ylen, 0:xlen] = grid
    for i in range(4):
        new_grid = new_grid + 1
        new_grid[new_grid > 9] = 1
        expanded_grid[0:ylen, (xlen*(i+1)):(xlen*(i+2))] = new_grid
    new_grid = grid
    for j in range(1,5):
        for i in range(5):
            new_grid = new_grid + 1
            new_grid[new_grid > 9] = 1
            if i == 0: row_start_grid = new_grid
            expanded_grid[(ylen*j):(ylen*(j+1)), (xlen*(i)):(xlen*(i+1))] = new_grid
        new_grid = row_start_grid
    return expanded_grid





filename = 'inputData/input15.txt'
grid     = expand_grid(read_input(filename))

xlen = len(grid[1,:])
ylen = len(grid[:,1])

print(grid.shape)

