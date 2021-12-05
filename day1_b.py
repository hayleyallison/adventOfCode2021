filename = 'inputData/input1.txt'
file = open(filename)

count_increases = 0
counter = 0
counter2 = 0

depths = [0.0, 0.0, 0.0]
depths_aves = []
old = None

# put data in a list
for line in file:
    depths[counter2] = float(line)
    counter2 += 1
    if counter2 == 3:
        counter2 = 0
    if counter >= 2:
        depths_aves.append((sum(depths)/3.0))

    counter += 1

#no run through the depths_aves and determined if increased
for dd in depths_aves:
    if old is None:
        print("No previous average!")
    elif dd > old:
        print("Increased")
        count_increases += 1
    elif dd < old:
        print("Decreased")
    else:
        print("No change")
    old = dd

print('Complete. %d increases' % count_increases)
