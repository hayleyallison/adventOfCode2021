import numpy as np

# don't need to do all of the fish!
filename = "inputData/input6.txt"
file     = open(filename)

fish  = np.zeros((9, 2))
blank = np.zeros((9, 2))

#create fish cohorts
for i in range(0,9):
	fish[i, 0] = i
	blank[i,0] = i

strfishline   = file.read()
fish_ages_int = strfishline.split(',')

#count the fish!
for fishbit in fish_ages_int:
	a = np.where(fish[:,0] == int(fishbit))
	fish[a,1] += 1

for day in range(0,256):
	fish_update = blank.copy()
	for f in range(0,9):
		if f == 0:
			fish_update[6,1] += fish[0,1]
			fish_update[8,1] += fish[0,1]
		else:
			fish_update[f-1, 1] += fish[f,1] 
	fish = fish_update.copy()

print(sum(fish[:,1]))
