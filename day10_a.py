def other_bracket(s):
	if s == '(': return ')'
	if s == '[': return ']'
	if s == '{': return '}'
	if s == '<': return '>'

filename = 'inputData/input10.txt'
file     = open(filename)

scores = {')':3, ']':57, '}':1197, '>':25137}
score  = 0

opened = []
expecting = ''

for line in file:
	for s in line:
		if s == '\n': continue
		if (len(opened) == 0) & ((s == ')') | (s == ']') | (s == '}') | (s == '>')):
			score += scores[s]
			break
		else:
			if ((s == '(') | (s == '[') | (s == '{') | (s == '<')):
				opened.insert(0, s)
				expecting = other_bracket(s)
			elif (s == expecting):
				opened.pop(0)
				expecting = other_bracket(opened[0])
			else:
				score += scores[s]
				break

print(score)