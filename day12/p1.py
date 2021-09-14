import re

initial = re.compile(r"initial state: ([.#]+)")
rule = re.compile(r"([.#]+) => ([.#])")

min = -4
patterns = dict()
updates = list()
plants = list()

with open("input.txt", "r") as f:
	lines = f.readlines()
	state = initial.match(lines.pop(0)).group(1)
	plants = list("".join(('....', state, '....')))

	lines.pop(0)
	for l in lines:
		regla = rule.match(l)
		patterns[regla.group(1)] = regla.group(2)

it = 1
while it <= 20:
	updates = list()
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
	it += 1

suma = 0
for p in range(len(plants)):
	if plants[p] == '#':
		suma += p + min
print(suma)