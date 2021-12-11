def run_fuel(steps):
	tot = 0
	for s in range(1,steps+1):
		tot += s
	return tot

import numpy as np 

#read in the data
filename = "inputData/input7.txt"
file     = open(filename)
data     = file.read()

indat     = data.split(",")
positions = []
for pos in indat:
	positions.append(int(pos))

# set up arrays
positions = np.array(positions)
highest   = max(positions)

# calculate all the fuel spent for each scenerio
fuel = np.zeros((highest+1,), dtype=int)
for attempt in range(0,highest+1):
	for pos in positions:
		dif = abs(pos - attempt)
		fuel[attempt] += run_fuel(dif)

print(min(fuel))