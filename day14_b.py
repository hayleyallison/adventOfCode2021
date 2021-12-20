def cut_up_poly(polytemp):
    parts2str = dict()
    for i in range(0, len(polytemp)-1):
        if polytemp[i:(i+2)] not in parts2str:
            parts2str[polytemp[i:(i+2)]] = 1
        else:
            parts2str[polytemp[i:(i+2)]] += 1
    return parts2str

def build_new(liststr, rules):
    newpartslist = dict()
    for part in liststr:
        if part in rules:
            #need to change
            newpart = part[0] + rules[part] + part[1]
            if newpart not in newpartslist:
                newpartslist[newpart] = liststr[part]
            else:
                newpartslist[newpart] += liststr[part]
        else:
            #don't need to change
            if part not in newpartslist:
                newpartslist[part] = liststr[part]
            else:
                newpartslist[part] += liststr[part]
    return newpartslist

def return_to_len2(len3dic):
    cleandic = dict()
    for key in len3dic:
        if len(key) == 3:
            # split to two
            front2 = key[0:2]
            back2  = key[1:]
            if front2 not in cleandic:
                cleandic[front2] = len3dic[key]
            else:
                cleandic[front2] += len3dic[key]
            if back2 not in cleandic:
                cleandic[back2] = len3dic[key]
            else:
                cleandic[back2] += len3dic[key]
        else:
            cleandic[key] = len3dic[key]
    return cleandic 

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
dic2str   = cut_up_poly(polytemp)
for _ in range(0,40):
    dic3str   = build_new(dic2str, rules)
    dic2str   = return_to_len2(dic3str)

# # calculate the letter frequency in position 1
letters = dict()
for key in dic2str:
    l = key[0]
    if l not in letters:
        letters[l] = dic2str[key]
    else:
        letters[l] += dic2str[key]
letters['V'] += 1   #because first is the same as last and both are V

# calculate the most common minus least common
most  = 0
least = 0
for v in letters:
    if letters[v] > most: most = letters[v]
    if least == 0: least = letters[v]
    if letters[v] < least: least = letters[v]

print(most - least)