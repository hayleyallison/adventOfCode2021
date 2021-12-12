import numpy as np

# get the staring energies
datafile = 'inputData/input11.txt'
file     = open(datafile)

octopus  = []
onum     = []
for line in file:
    for n in line:
        if n != '\n': onum.append(int(n))
    octopus.append(onum.copy())
    onum = []
octopus = np.array(octopus)

flashes = 0

#step
for _ in range(0,100):
    # add one to every octopus
    octopus += 1
    # look for 10s
    while (10 in octopus):
        for x in range(0,len(octopus[:,0])):
            for y in range(0,len(octopus[0,:])):
                if octopus[x,y] == 10:
                    flashes += 1
                    octopus[x,y] = 0
                    #set the surroundings
                    lx = -1
                    ux = 2
                    if (x == 0): lx = 0
                    if (x == (len(octopus[:,0])-1)): ux = 1

                    ly = -1
                    uy = 2
                    if (y == 0): ly = 0
                    if (y == (len(octopus[0,:])-1)): uy = 1

                    for ix in range(lx,ux):
                        for iy in range(ly,uy):
                            if (octopus[x+ix,y+iy] != 0) & (octopus[x+ix,y+iy] != 10): octopus[x+ix,y+iy] += 1
print(flashes)
