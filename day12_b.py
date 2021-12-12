def check_branch(key, map, tracked, flag_small_twice):
    path_found = 0
    old_tracked = tracked
    old_flag    = flag_small_twice
    for cave in map[key]:
        tracked = old_tracked
        flag_small_twice = old_flag
        if cave == 'end': 
            print(tracked+cave)
            tracked = old_tracked
            flag_small_twice = old_flag
            path_found += 1
        elif cave == 'start': 
            tracked = old_tracked
            flag_small_twice = old_flag
            continue
        elif (cave != cave.upper()) & (cave in tracked):
            if flag_small_twice: 
                tracked = old_tracked
                flag_small_twice = old_flag
                continue
            else: 
                flag_small_twice = True
                tracked += (cave+',')
                path_found += check_branch(cave, map, tracked, flag_small_twice)
        else:
            tracked += (cave+',')
            path_found += check_branch(cave, map, tracked, flag_small_twice)
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
paths = check_branch('start', map, 'start,', False)

print(paths)