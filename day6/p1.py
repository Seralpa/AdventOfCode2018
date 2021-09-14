from operator import itemgetter
from collections import Counter


def distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


points = list()
with open("input.txt", "r") as f:
	for l in f:
		line = l.split(", ")
		points.append((int(line[0]), int(line[1])))

maxx = max(points, key = itemgetter(0))[0] + 1
maxy = max(points, key = itemgetter(1))[1] + 1

matrix = list()
for y in range(maxy):
	matrix.append([])
	for x in range(maxx):
		min_distance = 1000
		point = -1
		for p in range(len(points)):
			dist = distance(points[p], (x, y))
			if dist == min_distance:
				point = -1
			if min_distance > dist:
				min_distance = dist
				point = p
		matrix[y].append(point)

inf = set()
#upper and lower
for x in range(len(matrix[0])):
	inf.add(matrix[0][x])
	inf.add(matrix[len(matrix) - 1][x])

for y in range(len(matrix)):
	inf.add(matrix[y][0])
	inf.add(matrix[y][len(matrix[0]) - 1])

matrix = [j for sub in matrix for j in sub]

cnt = Counter(matrix)
for p in cnt.most_common():
	if not p[0] in inf:
		print(p[1])
		break
