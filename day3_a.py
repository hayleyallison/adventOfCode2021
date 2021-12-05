filename = 'input3.txt'
file = open(filename)

bit_d = dict()
for line in file:
	i = 0
	for b in line:
		if b == '0':
			if str(i) not in bit_d: bit_d[str(i)] = [1,0]
			else: bit_d[str(i)][0] += 1
		elif b == '1':
			if str(i) not in bit_d: bit_d[str(i)] = [0,1]
			else: bit_d[str(i)][1] += 1
		i += 1

gamma   = ''
epsilon = ''
for pos in bit_d:
	if bit_d[pos][0] > bit_d[pos][1]:
		gamma   += '0'
		epsilon += '1'
	else:
		gamma   += '1'
		epsilon += '0'

power = int(gamma, 2) * int(epsilon, 2)
print(power)