import string

filename = "input2.txt"

file = open(filename)

depth = 0
horri = 0
aim   = 0

for line in file:
	bits = line.split()
	if (bits[0] == "forward"):
		horri += float(bits[1])
		depth += (aim * float(bits[1]))
	elif (bits[0] == "down"):
		aim += float(bits[1])
	elif (bits[0] == "up"):
		aim -= float(bits[1])

final = horri * depth
print(final)