import string

filename = "inputData/input2.txt"

file = open(filename)

depth = 0
horri = 0

for line in file:
	bits = line.split()
	if (bits[0] == "forward"):
		horri += float(bits[1])
	elif (bits[0] == "down"):
		depth += float(bits[1])
	elif (bits[0] == "up"):
		depth -= float(bits[1])

final = horri * depth
print(final)