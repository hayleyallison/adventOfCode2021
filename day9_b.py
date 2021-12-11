# this is an awful piece of code - rewrite... 
import numpy as np

# read in data
filename = "inputData/input9.txt"
file     = open(filename)

# construct the grid
grid = []
for line in file:
	row = []
	for n in line:
		if n == '\n': continue
		row.append(int(n))
	grid.append(row.copy())

checked  = np.zeros((len(grid), len(grid[0])), dtype = int)
to_check = []
basins   = []

for r in range(0,len(grid)):
 	for c in range(0,len(grid[0])):
 		#run through each point and see if we have checked it already
 		if checked[r,c] != 0: continue
 		# for the point has not been checked and does not equal 9 start the hunt
 		checked[r,c] = 1
 		if grid[r][c] != 9:
 			#add all the neighbours to a check list
 			if (r != 0) & (r != (len(grid)-1)):
 				if (c != 0) & (c != (len(grid)-1)):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 				elif (c == 0):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 				else:
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 			elif (r == 0):
 				if (c != 0) & (c != (len(grid)-1)):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 				elif (c == 0):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 				else:
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r+1,c] == 0: to_check.append([r+1,c])
 			else:
 				if (c != 0) & (c != (len(grid)-1)):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 				elif (c == 0):
 					if checked[r,c+1] == 0: to_check.append([r,c+1])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 				else:
 					if checked[r,c-1] == 0: to_check.append([r,c-1])
 					if checked[r-1,c] == 0: to_check.append([r-1,c])
 			# we have touched a new basin, so start the count
 			cnt = 1

 			#loop through the check list, addinng more as we find them until there are no more to check
 			while (len(to_check) > 0):
 				checking = to_check[0]
 				# we haev found another - add neighbours to check list and count
 				if (grid[checking[0]][checking[1]] != 9) & (checked[checking[0],checking[1]] == 0):
 					cnt += 1
 					if (checking[0] != 0) & (checking[0] != (len(grid)-1)):
 						if (checking[1] != 0) & (checking[1] != (len(grid)-1)):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 						elif (checking[1] == 0):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 						else:
		 					if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 					elif (checking[0] == 0):
 						if (checking[1] != 0) & (checking[1] == (len(grid)-1)):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
 						elif (checking[1] == 0):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
 						else:
		 					if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]+1,checking[1]] == 0) & ([checking[0]+1,checking[1]] not in to_check):
		 						to_check.append([checking[0]+1,checking[1]])
 					else:
 						if (checking[1] != 0) & (checking[1] == (len(grid)-1)):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 						elif (checking[1] == 0):
 							if (checked[checking[0],checking[1]+1] == 0) & ([checking[0],checking[1]+1] not in to_check):
 								to_check.append([checking[0],checking[1]+1])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 						else:
 							if (checked[checking[0],checking[1]-1] == 0) & ([checking[0],checking[1]-1] not in to_check):
		 						to_check.append([checking[0],checking[1]-1])
		 					if (checked[checking[0]-1,checking[1]] == 0) & ([checking[0]-1,checking[1]] not in to_check):
		 						to_check.append([checking[0]-1,checking[1]])
 				#mark as checked
 				checked[checking[0],checking[1]] = 1
 				#remove from check list
 				to_check.remove(checking)

 			# add the basin size to the basins array
 			basins.append(cnt)

biggest = max(basins)
basins.remove(biggest)
second_biggest = max(basins)
basins.remove(second_biggest)
third_biggest = max(basins)
basins.remove(third_biggest)

print(biggest * second_biggest * third_biggest)