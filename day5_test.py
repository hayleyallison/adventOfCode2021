import numpy as np

test_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

lines = test_input.split('\n')

vent_lines = []
for line in lines:
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
	else:
		#the difficult case
		y1 = row[1]
		y2 = row[3]
		x1 = row[0]
		x2 = row[2]
		if (y1 < y2) & (x1 < x2):
			for i in range(0,((y2+1)-y1)):
					board[y1+i,x1+i] += 1
		elif (y1 > y2) & (x1 < x2):
			for i in range(0,((y1+1)-y2)):
					board[y1-i,x1+i] += 1
		elif (y1 < y2) & (x1 > x2):
			for i in range(0,((y2+1)-y1)):
					board[y1+i,x1-i] += 1
		else:
			for i in range(0,((y1+1)-y2)):
					board[y1-i,x1-i] += 1


overlaps = 0
for i in range(0, maxv):
	for j in range(0,maxv):
		if board[i,j] > 1:
			overlaps += 1

print(board)