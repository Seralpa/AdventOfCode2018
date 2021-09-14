from Car import Car

tracks: list[list[str]] = list()
cars: list[Car] = list()
with open("input_new.txt", "r") as f:
	for l in f:
		tracks.append(list(l.replace('\n', "")))

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

while len(cars) > 1:
	for c in cars:
		c.move(tracks)
		c.check_crash(cars)
	cars = [c for c in cars if not c.check_crash(cars)]
	cars.sort(key = lambda j: j.pos[1])
	cars.sort(key = lambda i: i.pos[0])

print(f"{cars[0].pos[1]},{cars[0].pos[0]}")