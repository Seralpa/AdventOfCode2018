import copy
from Unit import *

elf_atk = 3
battlefield_original: list[list[str]] = list()
units_original: list[Unit] = list()
with open("input.txt", "r") as f:
	battlefield_original = [list(l.strip()) for l in f.readlines()]
	for i, row in enumerate(battlefield_original):
		for j, c in enumerate(row):
			if any(c == x.value for x in Race):
				units_original.append(Unit((i, j), 200, 3, Race(c)))

while True:
	elf_atk += 1
	battlefield = copy.deepcopy(battlefield_original)
	units = copy.deepcopy(units_original)
	for u in units:
		if u.race == Race.ELF:
			u.atk = elf_atk
	g_battlefield = generate_graph(battlefield)
	round = 1
	while True:
		# sort units in reading order
		units.sort(key = lambda j: j.pos[1])
		units.sort(key = lambda i: i.pos[0])
		for u in units:
			if not u.is_dead():
				kill_flag = False
				res = u.attack(battlefield, units, g_battlefield)
				if res == Atk_result.NO_HIT:
					u.move(battlefield, units, g_battlefield)
					res = u.attack(battlefield, units, g_battlefield)
				if res == Atk_result.KILL:
					kill_flag = True
		units = [u for u in units if not u.is_dead()]
		numUnits = get_num_units_by_race(units)
		if numUnits[0] == 0 or numUnits[1] == 0:
			if not kill_flag: # if last round did not end with a kill, combat ended mid round so last round doesn't count
				round -= 1
			break
		round += 1
	if get_num_units_by_race(units)[0] == get_num_units_by_race(units_original)[0]:
		print(round * get_hp_sum(units))
		break
	# this program takes a while to run, progress updates were added
	print(f"Progress update: battle with {elf_atk = } lost")
