import networkx as nx
import sys

sys.setrecursionlimit(10000)
mapa = nx.Graph()
dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}


def follow_path(pos, path, mapa): #pos is ij
	posAnterior = pos
	for i, c in enumerate(path):
		if c not in '(|)':
			pos = (pos[0] + dirs[c][0], pos[1] + dirs[c][1])
			mapa.add_edge(posAnterior, pos)
			posAnterior = pos
		elif c == '(': #empieza parentesis
			start = i
			nivel = 0
			bar = [i]
			while True:
				start += 1
				if nivel == 0 and path[start] == '|':
					bar.append(start)
				elif nivel == 0 and path[start] == ')':
					cierre = start
					break
				elif path[start] == '(':
					nivel += 1
				elif path[start] == ')':
					nivel -= 1
			for b in range(len(bar) - 1):
				follow_path(pos, path[bar[b] + 1 : bar[b + 1]] + path[cierre + 1 :], mapa)
			follow_path(pos, path[bar[-1] + 1 : cierre] + path[cierre + 1 :], mapa)
			break


with open("input.txt") as f:
	path = list(f.readline().strip())
	path.pop()
	path.pop(0)

follow_path((0, 0), path, mapa)
print(max(nx.single_source_bellman_ford_path_length(mapa, (0, 0)).values()))
