def cut_up_poly(polytemp):
    liststr = []
    for i in range(0, len(polytemp)-1):
        liststr.append(polytemp[i:(i+2)])
    
    return liststr

def build_new(liststr, rules):
    newpartslist = []
    for part in liststr:
        if part in rules:
            newpartslist.append(part[0] + rules[part] + part[1])
        else:
            newpartslist.append(part)
    return newpartslist

def reassemble_parts(partslist):
    first = True
    newpoly = ''
    for part in partslist:
        if first:
            newpoly = part
            first = False
        else:
            newpoly += part[1:]
    return newpoly

filename = 'inputData/input14.txt'
file     = open(filename)

count = 0
rules = dict()
for line in file:
    if count == 0:
        polytemp = line.split('\n')[0]
    elif (line != '\n'):
        bits = line.split(' -> ')
        rules[bits[0]] = bits[1].split('\n')[0]
    count += 1

# split the polytemp into a list of two character strings
for _ in range(0,10):
    liststr   = cut_up_poly(polytemp)
    partslist = build_new(liststr, rules)
    polytemp  = reassemble_parts(partslist)

# calculate the letter frequency
letters = dict()
for l in polytemp:
    if l not in letters:
        letters[l] = 1
    else:
        letters[l] += 1

# calculate the most common minus least common
most  = 0
least = 0
for v in letters:
    if letters[v] > most: most = letters[v]
    if least == 0: least = letters[v]
    if letters[v] < least: least = letters[v]

print(most - least)