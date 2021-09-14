with open("input.txt") as f:
	depth = int(f.readline().strip()[7 :])
	t1, t2 = f.readline().strip()[8 :].split(',')
	target = (int(t2), int(t1))

erosion_constant = 20183
cave: list[list[int]] = list()

# calculate erosion
for i in range(target[0] + 1):
	cave.append(list())
	for j in range(target[1] + 1):
		if (i, j) == (0, 0) or (i, j) == target: #geo=0
			cave[i].append((0 + depth) % erosion_constant)
		elif i == 0:
			cave[i].append(((j * 16807) + depth) % erosion_constant)
		elif j == 0:
			cave[i].append(((i * 48271) + depth) % erosion_constant)
		else:
			cave[i].append(((cave[i - 1][j] * cave[i][j - 1]) + depth) % erosion_constant)

# calculate risc level and sum
risk_level = 0
for i in range(len(cave)):
	for j in range(len(cave[i])):
		cave[i][j] = cave[i][j] % 3
		risk_level += cave[i][j]
print(risk_level)
