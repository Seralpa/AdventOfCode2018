size = 300
serial = 1718
grid: list[list] = list()

for i in range(size - 1):
	grid.append([])
	for j in range(size - 1):
		power = (((j + 1 + 10) * (i + 1)) + serial) * (j + 1 + 10)
		power = (power % 1000) // 100
		grid[i].append(power - 5)

max = 0
index = (0, 0)
for i in range(len(grid) - 2):
	for j in range(len(grid) - 2):
		sum = 0
		for x in range(i, i + 3):
			for y in range(j, j + 3):
				sum += grid[x][y]
		if sum > max:
			max = sum
			index = (i, j)
print(f"{index[1]+1},{index[0]+1}")
