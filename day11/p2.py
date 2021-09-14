import operator

max_size = 300
serial = 1718
cuadrants = dict()


def get_cuadrant_power(i, j, size):
	if (i, j, size) in cuadrants:
		return cuadrants[(i, j, size)]
	if size % 2 == 0:
		sum = get_cuadrant_power(i, j, size / 2) + get_cuadrant_power(i, j + size / 2, size / 2) + get_cuadrant_power(
		    i + size / 2, j, size / 2) + get_cuadrant_power(i + size / 2, j + size / 2, size / 2)
	elif size == 1:
		sum = get_power(i, j)
	else:
		sum = get_cuadrant_power(i, j, size - 1)
		for a in range(size):
			sum += get_cuadrant_power(i + a, j + size - 1, 1)
		for a in range(size - 1):
			sum += get_cuadrant_power(i + size - 1, j + a, 1)
	cuadrants[(i, j, size)] = sum
	return sum


def get_power(i, j):
	power = (((j + 1 + 10) * (i + 1)) + serial) * (j + 1 + 10)
	power = (power % 1000) // 100
	return power - 5


for size in range(1, 300 - 1):
	# this program takes a while to run, progress updates were added
	print(f"progress update: {size = }")
	for i in range(max_size - size + 1):
		for j in range(max_size - size + 1):
			get_cuadrant_power(i, j, size)

ans = max(list(cuadrants.items()), key = operator.itemgetter(1))[0]
print(f"\nRESULT\nx, y, size = {ans[1]+1, ans[0]+1, ans [2]}")
