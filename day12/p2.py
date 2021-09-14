import re

ini = re.compile(r"initial state: ([.#]+)")
rule = re.compile(r"([.#]+) => ([.#])")

min = -4
patterns = dict()
updates = list()
plants = list()

with open("input.txt", "r") as f:
	lines = f.readlines()
	state = ini.match(lines.pop(0)).group(1)
	plants = list("".join(('....', state, '....')))

	lines.pop(0)
	for l in lines:
		regla = rule.match(l)
		patterns[regla.group(1)] = regla.group(2)

max_iters = 50000000000
suma = 0
prev_plants = ""
for it in range(1, max_iters + 1):
	updates = []
	for p in range(len(plants)):
		if p > 1 and p < len(plants) - 2:
			patron = "".join((plants[p - 2], plants[p - 1], plants[p], plants[p + 1], plants[p + 2]))
			if plants[p] != patterns[patron]:
				updates.append(p)

	for u in updates:
		if plants[u] == '.':
			plants[u] = '#'
		else:
			plants[u] = '.'

	if plants[2] == '#':
		plants.insert(0, '.')
		min -= 1
	if plants[3] == '#':
		plants.insert(0, '.')
		min -= 1
	if plants[len(plants) - 3] == '#':
		plants.append('.')
	if plants[len(plants) - 4] == '#':
		plants.append('.')

	begining = plants[0 : plants.index('#')]
	if len(begining) > 4:
		for _ in range(len(begining) - 4):
			plants.remove('.')
		min += len(begining) - 4

	prev_sum = suma
	suma = 0
	for p in range(len(plants)):
		if plants[p] == '#':
			suma += p + min

	# check if pattern has stabilized
	if prev_plants == plants:
		break

	prev_plants = plants[:]

print(suma + (suma - prev_sum) * (max_iters - it))
