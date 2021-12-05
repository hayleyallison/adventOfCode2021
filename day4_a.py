import numpy as np

filename = 'inputData/input4.txt'
file = open(filename)

call = ''
i    = -2
boards = []
scores = []

for line in file:
	if i == -2:
		call = line
		i += 1
	else:
		if line == "\n":
			i += 1
			r = 0
			c = 0
			boards.append(np.zeros((5,5)))
			scores.append(np.zeros((5,5)))
		else:
			#read in the board
			numbers = line.split()
			for n in numbers:
				boards[i][r,c] = int(n)
				c += 1
			r +=1
			c = 0

call_numbers = call.split(',')
winner = False

for n in call_numbers:
	nn = int(n)

	#check every board for called number
	ix = 0
	for board in boards:
		for r in range(0,5):
			for c in range(0,5):
				if board[r,c] == nn:
					scores[ix][r,c] = 1
		ix += 1

	#check scores of every board
	ib  = 0
	for s in scores:
		for r in range(0,5):
			if sum(s[r,:]) == 5:
				print(s)
				winner = True
				break
		for c in range(0,5):
			if sum(s[:,c]) == 5:
				print(s)
				winner = True
				break
		if winner: break
		ib += 1

	if winner: break
	
#calculate score
winning_board = boards[ib]
winning_score = scores[ib]

sumval = 0
for r in range(0,5):
	for c in range(0,5):
		if winning_score[r,c] == 0:
			sumval += winning_board[r,c]
print(sumval*nn)




