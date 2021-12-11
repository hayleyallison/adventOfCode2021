def other_bracket(s):
	if s == '(': return ')'
	if s == '[': return ']'
	if s == '{': return '}'
	if s == '<': return '>'

filename = 'inputData/input10.txt'
file     = open(filename)

scores = {')':1, ']':2, '}':3, '>':4}
score  = []


expecting = ''

for line in file:
	opened = []
	for s in line:
		if (len(opened) == 0) & ((s == ')') | (s == ']') | (s == '}') | (s == '>')):
			break
		else:
			if ((s == '(') | (s == '[') | (s == '{') | (s == '<')):
				opened.insert(0, s)
				expecting = other_bracket(s)
			elif (s == expecting):
				opened.pop(0)
				expecting = other_bracket(opened[0])
			elif (s == '\n'):
				# in complete line found - score
				ts = 0
				for sym in opened:
					ts *= 5
					ts += scores[other_bracket(sym)]
				score.append(ts)
			elif (s != expecting):
				break
			else:
				print('Something you werent expecting')
score = sorted(score)
print(score[int((len(score)-1)/2)])