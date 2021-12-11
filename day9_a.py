def check_up_down(grid, r, c):
	if (r != 0) & (r != (len(grid)-1)):
		if (grid[r][c] < grid[r+1][c]) & (grid[r][c] < grid[r-1][c]): 
			return True
		else: return False
	elif (r == 0):
		if grid[r][c] < grid[r+1][c]: 
			return True
		else: return False
	else:
		if grid[r][c] < grid[r-1][c]: 
			return True
		else: return False

# read in data
filename = "inputData/input9.txt"
file     = open(filename)

grid = []
for line in file:
	row = []
	for n in line:
		if n == '\n': continue
		row.append(int(n))
	grid.append(row.copy())

low_points = []

for r in range(0,len(grid)):
	for c in range(0,len(grid[0])):
		if (c != 0) & (c != (len(grid[0])-1)):
			#check left and right
			if (grid[r][c] < grid[r][c-1]) & (grid[r][c] < grid[r][c+1]):
				if check_up_down(grid, r, c):
					low_points.append([r,c])
		elif (c == 0):
			#check right
			if (grid[r][c] < grid[r][c+1]):
				if check_up_down(grid, r, c):
					low_points.append([r,c])
		else:
			#check left
			if (grid[r][c] < grid[r][c-1]):
				if check_up_down(grid, r, c):
					low_points.append([r,c])

total = 0
for v in low_points:
	total += (grid[v[0]][v[1]] + 1)

print(total)