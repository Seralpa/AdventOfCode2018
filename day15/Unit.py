from __future__ import annotations
import networkx as nx
from operator import itemgetter
from enum import Enum, auto


class Race(Enum):
	ELF = 'E'
	GOBLIN = 'G'


class Atk_result(Enum):
	NO_HIT = auto()
	HIT = auto()
	KILL = auto()


def get_unit_by_pos(pos: tuple[int, int], units: list[Unit]):
	for u in units:
		if pos == u.pos:
			return u


def generate_graph(battlefield: list[list[str]]):
	g_battlefield = nx.Graph()
	for i in range(len(battlefield)):
		for j in range(len(battlefield[i])):
			if battlefield[i][j] == '.':
				g_battlefield.add_node((i, j))
				if battlefield[i - 1][j] == '.':
					g_battlefield.add_edge((i, j), (i - 1, j))
				if battlefield[i][j - 1] == '.':
					g_battlefield.add_edge((i, j - 1), (i, j))
	return g_battlefield


def get_num_units_by_race(units: list[Unit]):
	n_elves = 0
	n_goblins = 0
	for u in units:
		if u.race.value == Race.ELF.value:
			n_elves += 1
		else:
			n_goblins += 1
	return (n_elves, n_goblins)


def get_hp_sum(units: list[Unit]):
	total = 0
	for u in units:
		total += u.hp
	return total


class Unit:
	def __init__(self, pos: tuple[int, int], hp: int, atk: int, race: Race):
		self.pos = pos #i,j
		self.hp = hp
		self.atk = atk
		self.race = race

	def is_dead(self):
		return self.hp < 1

	def attack(self, battlefield: list[list[str]], units: list[Unit], g_battlefield: nx.Graph):
		enemies_close: list[Unit] = list()

		up = battlefield[self.pos[0] - 1][self.pos[1]]
		left = battlefield[self.pos[0]][self.pos[1] - 1]
		right = battlefield[self.pos[0]][self.pos[1] + 1]
		down = battlefield[self.pos[0] + 1][self.pos[1]]

		# up
		if any(up == x.value for x in Race) and up != self.race.value:
			u = get_unit_by_pos((self.pos[0] - 1, self.pos[1]), units)
			if not u.is_dead():
				enemies_close.append(u)
		# left
		if any(left == x.value for x in Race) and left != self.race.value:
			u = get_unit_by_pos((self.pos[0], self.pos[1] - 1), units)
			if not u.is_dead():
				enemies_close.append(u)
		# right
		if any(right == x.value for x in Race) and right != self.race.value:
			u = get_unit_by_pos((self.pos[0], self.pos[1] + 1), units)
			if not u.is_dead():
				enemies_close.append(u)

		# down
		if any(down == x.value for x in Race) and down != self.race.value:
			u = get_unit_by_pos((self.pos[0] + 1, self.pos[1]), units)
			if not u.is_dead():
				enemies_close.append(u)
		if len(enemies_close) == 0:
			return Atk_result.NO_HIT

		enemies_close.sort(key = lambda e: e.hp)
		target = enemies_close[0]

		target.hp -= self.atk
		if target.is_dead():
			battlefield[target.pos[0]][target.pos[1]] = '.'
			# add target.pos to g_battlefield as now it's a free space
			g_battlefield.add_node(target.pos)
			# up
			if battlefield[target.pos[0] - 1][target.pos[1]] == '.':
				g_battlefield.add_edge(target.pos, (target.pos[0] - 1, target.pos[1]))
			# left
			if battlefield[target.pos[0]][target.pos[1] - 1] == '.':
				g_battlefield.add_edge(target.pos, (target.pos[0], target.pos[1] - 1))
			# right
			if battlefield[target.pos[0]][target.pos[1] + 1] == '.':
				g_battlefield.add_edge(target.pos, (target.pos[0], target.pos[1] + 1))
			# down
			if battlefield[target.pos[0] + 1][target.pos[1]] == '.':
				g_battlefield.add_edge(target.pos, (target.pos[0] + 1, target.pos[1]))
			return Atk_result.KILL
		return Atk_result.HIT

	def get_enemies(self, units: list[Unit]):
		return [u for u in units if u.race != self.race and not u.is_dead()]

	def move(self, battlefield: list[list[str]], units: list[Unit], g_battlefield: nx.Graph):
		if len(self.get_enemies(units)) == 0:
			return None
		# get targets
		targets = set()
		for e in self.get_enemies(units):
			# up
			if battlefield[e.pos[0] - 1][e.pos[1]] == '.':
				targets.add((e.pos[0] - 1, e.pos[1]))
			# left
			if battlefield[e.pos[0]][e.pos[1] - 1] == '.':
				targets.add((e.pos[0], e.pos[1] - 1))
			# right
			if battlefield[e.pos[0]][e.pos[1] + 1] == '.':
				targets.add((e.pos[0], e.pos[1] + 1))
			# down
			if battlefield[e.pos[0] + 1][e.pos[1]] == '.':
				targets.add((e.pos[0] + 1, e.pos[1]))
		# sort targets
		targets = list(targets)
		targets.sort(key = itemgetter(1))
		targets.sort(key = itemgetter(0))

		# calculate minimum paths to targets

		# get sources
		sources = list()
		# up
		if battlefield[self.pos[0] - 1][self.pos[1]] == '.':
			sources.append((self.pos[0] - 1, self.pos[1]))
		# left
		if battlefield[self.pos[0]][self.pos[1] - 1] == '.':
			sources.append((self.pos[0], self.pos[1] - 1))
		# right
		if battlefield[self.pos[0]][self.pos[1] + 1] == '.':
			sources.append((self.pos[0], self.pos[1] + 1))
		# down
		if battlefield[self.pos[0] + 1][self.pos[1]] == '.':
			sources.append((self.pos[0] + 1, self.pos[1]))

		minimum_paths: list[list] = list()
		for o in targets:
			minimum_paths.append([])
			for s in sources:
				if nx.has_path(g_battlefield, s, o):
					minimum_paths[-1].append(nx.shortest_path(g_battlefield, source = s, target = o))

		minimum_paths = [min(p, key = lambda x: len(x)) for p in minimum_paths if len(p) > 0]

		if len(minimum_paths) == 0:
			return None

		movement = min(minimum_paths, key = lambda x: len(x))[0]

		# make move
		battlefield[self.pos[0]][self.pos[1]] = '.'
		battlefield[movement[0]][movement[1]] = self.race.value
		g_battlefield.add_node(self.pos)
		# up
		if battlefield[self.pos[0] - 1][self.pos[1]] == '.':
			g_battlefield.add_edge(self.pos, (self.pos[0] - 1, self.pos[1]))
		# left
		if battlefield[self.pos[0]][self.pos[1] - 1] == '.':
			g_battlefield.add_edge(self.pos, (self.pos[0], self.pos[1] - 1))
		# right
		if battlefield[self.pos[0]][self.pos[1] + 1] == '.':
			g_battlefield.add_edge(self.pos, (self.pos[0], self.pos[1] + 1))
		# down
		if battlefield[self.pos[0] + 1][self.pos[1]] == '.':
			g_battlefield.add_edge(self.pos, (self.pos[0] + 1, self.pos[1]))
		g_battlefield.remove_node(movement)
		self.pos = movement
