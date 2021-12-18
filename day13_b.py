import numpy as np

# read in the input
filename = 'inputData/input13.txt'
file     = open(filename)

x = []
y = []
commands = []
for line in file:
    if line == '\n':
        continue
    elif (line[0] == 'f'):
        commands.append(line)
    else:
        coords = line.split(',')
        x.append(int(coords[0]))
        y.append(int(coords[1].split('\n')[0]))

# construct the 'paper'
paper = np.zeros((max(y)+1, max(x)+1), dtype = int)
for i in range(0,len(x)):
    paper[y[i], x[i]] = 1

folds = []
#pull out the folds
for line in commands:
    words = line.split()
    fold = words[2].split('=')
    if fold[0] == 'x':
        folds.append([int(fold[1]), 0])
    else:
        folds.append([0, int(fold[1])])

for just_one in folds:
    if just_one[0] != 0:
        #x fold
        left  = paper[:, 0:just_one[0]]
        right = paper[:, (just_one[0]+1):]

        newpaper = np.zeros((len(paper[:,1]), just_one[0]))

        for ix in range(0, just_one[0]):
            for iy in range(0, len(paper[:,1])):
                if (left[iy, ix] ==1) | (right[iy,just_one[0]-1-ix] == 1):
                    newpaper[iy,ix] = 1
                else:
                    newpaper[iy, ix] = 0
        paper = newpaper.copy()
    else:
        top    = paper[0:just_one[1], :]
        bottom = paper[(just_one[1]+1):, :]
        newpaper = np.zeros((just_one[1], len(paper[1,:])))
        for ix in range(0, len(paper[1,:])):
            for iy in range(0, just_one[1]):
                if (top[iy, ix] ==1) | (bottom[just_one[1]-1-iy,ix] == 1):
                    newpaper[iy,ix] = 1
                else:
                    newpaper[iy, ix] = 0
        paper = newpaper.copy()

out_string = []
linestring = ''

for iy in range(0,len(paper[:,1])):
    for ix in range(0, len(paper[1,:])):
        if paper[iy,ix] == 1: linestring += '#'
        else: linestring += '.'
    out_string.append(linestring)
    linestring = ''

for out_string_bit in out_string:
    print(out_string_bit)