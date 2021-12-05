import numpy as np

filename = 'inputData/input5.txt'
file     = open(filename)

# get coordinates from file
vent_lines = []
for line in file:
	pairs = line.split(' -> ')

	pairStart = pairs[0].split(',')
	pairEnd   = pairs[1].split(',')
	vent_lines.append([int(pairStart[0]), int(pairStart[1]), int(pairEnd[0]), int(pairEnd[1])])

# determine how big our grid needs to be
maxv = 0
for row in vent_lines:
	max_row = max(row)
	if max_row > maxv: maxv = max_row

maxv += 1

#make grid
board = np.zeros((maxv, maxv), dtype=int)

#populate board with only vertical lines
for row in vent_lines:
		#if x1 = x2
	if (row[0] == row[2]):
		xv = row[0]
		y1 = row[1]
		y2 = row[3]
		if y1 > y2:
			yv1 = y2
			yv2 = y1+1
		else:
			yv1 = y1
			yv2 = y2+1
		board[yv1:yv2, xv] += 1
	elif (row[1] == row[3]):
		yv = row[1]
		x1 = row[0]
		x2 = row[2]
		if x1 > x2:
			xv1 = x2
			xv2 = x1+1
		else:
			xv1 = x1
			xv2 = x2+1
		board[yv, xv1:xv2] += 1

overlaps = 0
for i in range(0, maxv):
	for j in range(0,maxv):
		if board[i,j] > 1:
			overlaps += 1

print(overlaps)
