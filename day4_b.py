import numpy as np

# read in data
filename = 'input4.txt'
file = open(filename)

call = ''
i    = -2
boards = []
scores = []
won    = []

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
			won.append(0)
		else:
			#read in the board
			numbers = line.split()
			for n in numbers:
				boards[i][r,c] = int(n)
				c += 1
			r +=1
			c = 0

# play
call_numbers = call.split(',')
final_winner = False
lastWinningBoardIndex = None

for n in call_numbers:
	#set called number
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
		if won[ib] == 0:
			for r in range(0,5):
				if sum(s[r,:]) == 5:
					won[ib] = 1
					lastWinningBoardIndex = ib
					break
			for c in range(0,5):
				if sum(s[:,c]) == 5:
					won[ib] = 1
					lastWinningBoardIndex = ib
					break
		ib += 1

	# check if we have found the final winner
	if sum(won) == len(boards): final_winner = True

	if final_winner: break
	
#calculate score
winning_board = boards[lastWinningBoardIndex]
winning_score = scores[lastWinningBoardIndex]

sumval = 0
for r in range(0,5):
	for c in range(0,5):
		if winning_score[r,c] == 0:
			sumval += winning_board[r,c]
print(sumval*nn)
