def count_thing(area, thing, pos):
	cont = 0
	for i in range(pos[0] - 1, pos[0] + 2):
		for j in range(pos[1] - 1, pos[1] + 2):
			if pos != (i, j) and i < len(area) and j < len(area[i]) and i >= 0 and j >= 0:
				if area[i][j] == thing:
					cont += 1
	return cont


with open("input.txt") as f:
	area = [list(l.strip()) for l in f]

n_iter = 10
for _ in range(n_iter):
	updates = []
	for i in range(len(area)):
		for j in range(len(area[i])):
			if area[i][j] == '.':
				if count_thing(area, '|', (i, j)) >= 3:
					updates.append((i, j, '|'))
			elif area[i][j] == '|':
				if count_thing(area, '#', (i, j)) >= 3:
					updates.append((i, j, '#'))
			elif area[i][j] == '#':
				if count_thing(area, '#', (i, j)) < 1 or count_thing(area, '|', (i, j)) < 1:
					updates.append((i, j, '.'))
	for u in updates:
		area[u[0]][u[1]] = u[2]

count_tree = 0
count_lumber = 0
for l in area:
	for c in l:
		if c == '|':
			count_tree += 1
		if c == '#':
			count_lumber += 1
print(count_lumber * count_tree)
