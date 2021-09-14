from operator import itemgetter


def distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


points = list()
with open("input.txt", "r") as f:
	for l in f:
		line = l.split(", ")
		points.append((int(line[0]), int(line[1])))

maxx = max(points, key = itemgetter(0))[0] + 1
maxy = max(points, key = itemgetter(1))[1] + 1

matrix: list[list] = list()
for y in range(maxy):
	matrix.append(list())
	for x in range(maxx):
		total_distance = 0
		for p in points:
			total_distance += distance(p, (x, y))
		if total_distance < 10000:
			matrix[y].append(1)
		else:
			matrix[y].append(0)

matrix = [j for sub in matrix for j in sub]
print(matrix.count(1))
