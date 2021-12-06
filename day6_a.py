filename = "inputData/input6.txt"
file     = open(filename)

fish = []

strfishline   = file.read()
fish_ages_int = strfishline.split(',')

for fishbit in fish_ages_int:
	fish.append(int(fishbit))

for day in range(0,80):
	new_fish = fish.copy()
	cnt = 0
	for f in fish:
		if f == 0:
			new_fish.append(8)
			new_fish[cnt] = 6
		else:
			new_fish[cnt] -= 1
		cnt += 1
	fish = new_fish.copy()

print(len(fish))


