filename = "inputData/input8.txt"
file     = open(filename)

in_v  = []
out_v = []
i = 0

for line in file:
	half = line.split('|')
	in_v.append(half[0])
	out_v.append(half[1])
	i += 1

unique_count = 0

for line in out_v:
	parts = line.split()
	for p in parts:
		numl = len(p)
		if (numl==2)|(numl==3)|(numl==4)|(numl==7):
			unique_count += 1

print(unique_count)