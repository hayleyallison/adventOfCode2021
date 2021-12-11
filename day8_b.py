def determine_cypher(in_v):
	cypher = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':''}
	one    = ''
	seven  = ''
	eight  = ''
	four   = ''
	lenfiv = []
	lensix = []

	for i in inpv.split():
		if len(i) == 2: one = i
		if len(i) == 3: seven = i
		if len(i) == 4: four = i
		if len(i) == 7: eight = i
		if len(i) == 5: lenfiv.append(i)
		if len(i) == 6: lensix.append(i)
	cypher['A'] = find_not_in(seven, one)

	#find six
	six = ''
	for l6 in lensix:
		if (one[0] not in l6) | (one[1] not in l6):
			six = l6
			break
	lensix.remove(six)
	

	cypher['B'] = find_not_in(one, six)
	cypher['F'] = find_not_in(one, cypher['B'])

	#find 5
	five = ''
	for l5 in lenfiv:
		if cypher['B'] not in l5:
			five = l5
			break
	lenfiv.remove(five)

	cypher['G'] = find_not_in(five, four+cypher['A'])

	#find 3
	three = ''
	for l5 in lenfiv:
		if  cypher['F'] in l5:
			three = l5
			break
	lenfiv.remove(three)
	two = lenfiv[0]

	cypher['D'] = find_not_in(three, cypher['A']+cypher['B']+cypher['F']+cypher['G'])
	cypher['E'] = find_not_in(two, three)
	cypher['C'] = find_not_in(eight, cypher['A']+cypher['B']+cypher['F']+cypher['G']+cypher['D']+cypher['E'])

	return cypher

def find_not_in(stringin, teststring):
	for s in stringin:
		if s not in teststring:
			return s

def decode_output(stringin, cypher):
	flip_cypher = dict((value, key) for key,value in cypher.items())
	truth = {'ABCEFG': '0', 'BF':'1', 'ABDEG':'2', 'ABDFG':'3','BCDF':'4','ACDFG':'5','ACDEFG':'6','ABF':'7', 'ABCDEFG':'8', 'ABCDFG':'9'}
	
	fourdigit  = ''
	forcompare = ''

	for digit in stringin.split():
		for s in digit:
			forcompare += flip_cypher[s]
		fourdigit += truth[''.join(sorted(forcompare))]
		forcompare = ''

	return fourdigit


#####################################################################

# read in data
filename = "inputData/input8.txt"
file     = open(filename)

totalled = 0

for line in file:
	inpv   = line.split('|')[0]
	cypher = determine_cypher(inpv.split())
	digit4 = decode_output(line.split('|')[1], cypher)
	totalled += int(digit4)

print(totalled)