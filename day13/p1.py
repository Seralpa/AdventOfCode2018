import sys
from Car import Car

tracks: list[list[str]] = []
cars: list[Car] = []
with open("input.txt", "r") as f:
	for l in f:
		tracks.append(list(l.replace('\n', "")))

#quitar coches
for i in range(len(tracks)):
	for j in range(len(tracks[i])):
		if tracks[i][j] == 'v':
			tracks[i][j] = '|'
			cars.append(Car((i, j), (1, 0)))
		if tracks[i][j] == '^':
			tracks[i][j] = '|'
			cars.append(Car((i, j), (-1, 0)))
		if tracks[i][j] == '<':
			tracks[i][j] = '-'
			cars.append(Car((i, j), (0, -1)))
		if tracks[i][j] == '>':
			tracks[i][j] = '-'
			cars.append(Car((i, j), (0, 1)))

while True:
	for c in cars:
		c.move(tracks)
		if c.check_crash(cars):
			print(f"{c.pos[1]},{c.pos[0]}")
			sys.exit()
	cars.sort(key = lambda j: j.pos[1])
	cars.sort(key = lambda i: i.pos[0])
