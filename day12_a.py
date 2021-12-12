def check_branch(key, map, tracked):
    path_found = 0
    old_tracked = tracked
    for cave in map[key]:
        tracked = old_tracked
        if cave == 'end': 
            print(tracked+cave)
            tracked = old_tracked
            path_found += 1
        elif cave == 'start': 
            tracked = old_tracked
            continue
        elif (cave != cave.upper()) & (cave in tracked): 
            tracked = old_tracked
            continue
        else:
            tracked += (cave+',')
            path_found += check_branch(cave, map, tracked)
    return path_found

filename = 'inputData/input12.txt'
file = open(filename) #data.split('\n')

# make the cave map
map = dict()

for line in file:
    pullout = line.split('\n')
    caves   = pullout[0].split('-')
    if caves[0] not in map:
        map[caves[0]] = [caves[1]]
    else:
        map[caves[0]].append(caves[1])
    if caves[1] not in map:
        map[caves[1]] = [caves[0]]
    else:
        map[caves[1]].append(caves[0])

# path find
paths = check_branch('start', map, 'start,')

print(paths)