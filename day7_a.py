import numpy as np 

filename = "inputData/input7.txt"
file     = open(filename)
data     = file.read()

indat     = data.split(",")
positions = []
for pos in indat:
	positions.append(int(pos))

positions = np.array(positions)
highest   = max(positions)

fuel = np.zeros((highest+1,), dtype=int)
for attempt in range(0,highest+1):
	fuel[attempt] = sum(abs(positions - attempt))

print(min(fuel))