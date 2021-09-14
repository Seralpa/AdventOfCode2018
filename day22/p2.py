import networkx as nx

with open("input.txt") as f:
	depth = int(f.readline().strip()[7 :])
	t1, t2 = f.readline().strip()[8 :].split(',')
	target = (int(t2), int(t1))

erosion_constant = 20183
cave: list[list[int]] = list()

# calculate erosion
for i in range(target[0] + 100):
	cave.append([])
	for j in range(target[1] + 100):
		if (i, j) == (0, 0) or (i, j) == target: # geo=0
			cave[i].append((0 + depth) % erosion_constant)
		elif i == 0:
			cave[i].append(((j * 16807) + depth) % erosion_constant)
		elif j == 0:
			cave[i].append(((i * 48271) + depth) % erosion_constant)
		else:
			cave[i].append(((cave[i - 1][j] * cave[i][j - 1]) + depth) % erosion_constant)

# calculate risc level
for i in range(len(cave)):
	for j in range(len(cave[i])):
		cave[i][j] = cave[i][j] % 3

g_cave = nx.Graph()
for i in range(len(cave)):
	for j in range(len(cave[i])):
		if cave[i][j] == 0: # rock
			g_cave.add_edge((i, j, 'T'), (i, j, 'C'), w = 7)
		elif cave[i][j] == 1: # wet
			g_cave.add_edge((i, j, 'N'), (i, j, 'C'), w = 7)
		elif cave[i][j] == 2: # narrow
			g_cave.add_edge((i, j, 'N'), (i, j, 'T'), w = 7)

		if i > 0:
			if cave[i][j] == 0: # rock
				if cave[i - 1][j] == 0: # rock
					g_cave.add_edge((i, j, 'T'), (i - 1, j, 'T'), w = 1)
					g_cave.add_edge((i, j, 'C'), (i - 1, j, 'C'), w = 1)
				elif cave[i - 1][j] == 1: # wet
					g_cave.add_edge((i, j, 'C'), (i - 1, j, 'C'), w = 1)
				elif cave[i - 1][j] == 2: # narrow
					g_cave.add_edge((i, j, 'T'), (i - 1, j, 'T'), w = 1)
			elif cave[i][j] == 1: # wet
				if cave[i - 1][j] == 0: # rock
					g_cave.add_edge((i, j, 'C'), (i - 1, j, 'C'), w = 1)
				elif cave[i - 1][j] == 1: # wet
					g_cave.add_edge((i, j, 'C'), (i - 1, j, 'C'), w = 1)
					g_cave.add_edge((i, j, 'N'), (i - 1, j, 'N'), w = 1)
				elif cave[i - 1][j] == 2: # narrow
					g_cave.add_edge((i, j, 'N'), (i - 1, j, 'N'), w = 1)
			elif cave[i][j] == 2: # narrow
				if cave[i - 1][j] == 0: # rock
					g_cave.add_edge((i, j, 'T'), (i - 1, j, 'T'), w = 1)
				elif cave[i - 1][j] == 1: # wet
					g_cave.add_edge((i, j, 'N'), (i - 1, j, 'N'), w = 1)
				elif cave[i - 1][j] == 2: # narrow
					g_cave.add_edge((i, j, 'N'), (i - 1, j, 'N'), w = 1)
					g_cave.add_edge((i, j, 'T'), (i - 1, j, 'T'), w = 1)
		if j > 0:
			if cave[i][j] == 0: # rock
				if cave[i][j - 1] == 0: # rock
					g_cave.add_edge((i, j, 'T'), (i, j - 1, 'T'), w = 1)
					g_cave.add_edge((i, j, 'C'), (i, j - 1, 'C'), w = 1)
				elif cave[i][j - 1] == 1: # wet
					g_cave.add_edge((i, j, 'C'), (i, j - 1, 'C'), w = 1)
				elif cave[i][j - 1] == 2: # narrow
					g_cave.add_edge((i, j, 'T'), (i, j - 1, 'T'), w = 1)
			elif cave[i][j] == 1: # wet
				if cave[i][j - 1] == 0: # rock
					g_cave.add_edge((i, j, 'C'), (i, j - 1, 'C'), w = 1)
				elif cave[i][j - 1] == 1: # wet
					g_cave.add_edge((i, j, 'C'), (i, j - 1, 'C'), w = 1)
					g_cave.add_edge((i, j, 'N'), (i, j - 1, 'N'), w = 1)
				elif cave[i][j - 1] == 2: # narrow
					g_cave.add_edge((i, j, 'N'), (i, j - 1, 'N'), w = 1)
			elif cave[i][j] == 2: # narrow
				if cave[i][j - 1] == 0: # rock
					g_cave.add_edge((i, j, 'T'), (i, j - 1, 'T'), w = 1)
				elif cave[i][j - 1] == 1: # wet
					g_cave.add_edge((i, j, 'N'), (i, j - 1, 'N'), w = 1)
				elif cave[i][j - 1] == 2: # narrow
					g_cave.add_edge((i, j, 'N'), (i, j - 1, 'N'), w = 1)
					g_cave.add_edge((i, j, 'T'), (i, j - 1, 'T'), w = 1)

print(nx.shortest_path_length(g_cave, (0, 0, 'T'), (target[0], target[1], 'T'), weight = 'w'))
