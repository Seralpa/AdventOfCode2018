from Unit import *

battlefield: list[list[str]] = list()
units: list[Unit] = list()
with open("input.txt", "r") as f:
	battlefield = [list(l.strip()) for l in f.readlines()]
	for i, row in enumerate(battlefield):
		for j, c in enumerate(row):
			if any(c == x.value for x in Race):
				units.append(Unit((i, j), 200, 3, Race(c)))

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
	n_units = get_num_units_by_race(units)

	if n_units[0] == 0 or n_units[1] == 0:
		if not kill_flag: # if last round did not end with a kill, combat ended mid round so last round doesn't count
			round -= 1
		break
	round += 1
print(round * get_hp_sum(units))
