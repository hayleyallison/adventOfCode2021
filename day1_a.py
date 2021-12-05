filename = 'inputData/input1.txt'
file = open(filename)

count_increases = 0
old = None

for line in file:
    if old is None:
        print("No depths yet!")
    elif float(line) > old:
        print('Increases')
        count_increases += 1
    elif float(line) < old:
        print('Decreases')
    else:
        print('No change')
    
    old = float(line)

print('Complete. %d increases' % count_increases)