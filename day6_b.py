import numpy as np

# don't need to do all of the fish!
filename = "inputData/input6.txt"
file     = open(filename)

fish  = np.zeros((9,)) #you have to use double because of an overfill
blank = np.zeros((9,))

strfishline   = file.read()
fish_ages_int = strfishline.split(',')

#count the fish!
for fishbit in fish_ages_int:
	a = int(fishbit)
	fish[a] += 1

for day in range(0,256):
	fish_update = blank.copy()
	for f in range(0,9):
		if f == 0:
			fish_update[6] += fish[0]
			fish_update[8] += fish[0]
		else:
			fish_update[f-1] += fish[f] 
	fish = fish_update.copy()

print(sum(fish))