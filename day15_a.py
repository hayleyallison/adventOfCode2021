import numpy as np
from queue import PriorityQueue

filename = 'inputData/input15.txt'
file     = open(filename)

data = file.read()
file.close()

lines = data.split()

grid = np.zeros((len(lines), len(lines[0])))

iy = 0
ix = 0
for line in lines:
    for l in line:
        grid[iy,ix] = int(l)
        ix += 1
    iy += 1
    ix = 0

xlen = len(grid[1,:])
ylen = len(grid[:,1])

pos = (0,0)
destination = (ylen-1,xlen-1)

risk_track = {pos: 0}
been_to    = [pos]
optim      = PriorityQueue()
optim.put((0, pos))

offsets = [(-1,0), (1,0), (0,1), (0,-1)]

pos = (0,0)
found = False
while not optim.empty():
    pos = optim.get()[1]
    if pos == destination:
        found = True
        break
    for offset in offsets:
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])
        #check suitablilty
        if (new_pos[0] >= 0)&(new_pos[0]<=destination[0])&(new_pos[1] >= 0)&(new_pos[1] <= destination[1]):
            # calculate new risk
            new_risk = risk_track[pos] + grid[new_pos[0], new_pos[1]]
            if (new_pos not in been_to) or (new_risk < risk_track[new_pos]):
                risk_track[new_pos] = new_risk
                optim.put(((new_risk+abs(new_pos[0]-destination[0])+abs(new_pos[1]-destination[1])),new_pos))
                if new_pos not in been_to: been_to.append(new_pos)
    if found: break
print(risk_track[destination])
