def count_bits(nums, i):
	bit_count = [0,0]
	for line in nums:
		b = line[i]
		if b == '0':
			bit_count[0] += 1
		elif b == '1':
			bit_count[1] +=1
	return bit_count

def target_bit_find_ox(bit_count):
	if bit_count[0] > bit_count[1]: targetbit = '0'
	elif bit_count[0] < bit_count[1]: targetbit = '1'
	else: targetbit = '1'
	return targetbit

def target_bit_find_co(bit_count):
	if bit_count[0] < bit_count[1]: targetbit = '0'
	elif bit_count[0] > bit_count[1]: targetbit = '1'
	else: targetbit = '0'
	return targetbit

def remove_noncomplies(nums, targetbit, i):
	numshorter = []
	for line in nums:
		if line[i] == targetbit:
			numshorter.append(line)
	return numshorter

###########################################################

filename = 'input3.txt'
file = open(filename)

nums_ox = []

#read in the file content into a list
for line in file:
	nums_ox.append(line)
nums_co = nums_ox

i = 0
while (len(nums_ox) > 1):
	bit_count = count_bits(nums_ox, i)
	targetbit = target_bit_find_ox(bit_count)
	nums_ox   = remove_noncomplies(nums_ox, targetbit, i)
	i += 1

i = 0
while (len(nums_co) > 1):
	bit_count = count_bits(nums_co, i)
	targetbit = target_bit_find_co(bit_count)
	nums_co   = remove_noncomplies(nums_co, targetbit, i)
	i += 1

print(int(nums_ox[0], 2) * int(nums_co[0], 2))