import numpy as np

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

pos = (0,0)
destination = (99,99)

risk_track = {pos: 0}
been_to    = [pos]

offsets = [(-1,0), (1,0), (0,1), (0,-1)]

for _ in range(4):
    pos = (0,0)
    found = False
    for ix in range(100):
        for iy in range(100):
            pos = (iy, ix)
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
                        if new_pos not in been_to: been_to.append(new_pos)
        if found: break
    print(risk_track[destination])
