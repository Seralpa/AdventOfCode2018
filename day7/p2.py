import re

instruction_line = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n_workers = 5


def get_closed_tasks(instructions, done):
	for t in done:
		instructions = [i for i in instructions if i[0] != t]
	return [i[1] for i in instructions]


def get_open_tasks(instructions, done, assigned):
	not_yet = get_closed_tasks(instructions, done)
	to_do = [t for t in abc if t not in done and t not in not_yet]
	to_do = list(set(to_do).difference(assigned))
	return to_do


def get_duration(task):
	return (ord(task) - ord('A')) + 60


instructions = list()
with open("input.txt", "r") as f:
	for l in f:
		instructions.append((instruction_line.match(l).group(1), instruction_line.match(l).group(2)))

done = list()
assigned = list()
table = list()
open_tasks = get_open_tasks(instructions, done, assigned)
timestamp = [None for _ in range(n_workers)]
for i in range(n_workers):
	if i < len(open_tasks):
		timestamp[i] = (open_tasks[i], get_duration(open_tasks[i]))
		assigned.append(open_tasks[i])
table.append(timestamp)

time = 0
while True:
	time += 1
	timestamp = [None for _ in range(n_workers)]
	for i in range(n_workers):
		if table[time - 1][i] != None:
			if table[time - 1][i][1] != 0: # worker already had an unfinished task
				timestamp[i] = (table[time - 1][i][0], table[time - 1][i][1] - 1)
			else: # worker has finished his task
				done.append(table[time - 1][i][0])
				assigned.remove(table[time - 1][i][0])
	open_tasks = get_open_tasks(instructions, done, assigned)
	for i in range(n_workers):
		if timestamp[i] == None and 0 < len(open_tasks):
			timestamp[i] = (open_tasks[0], get_duration(open_tasks[0]))
			assigned.append(open_tasks[0])
			open_tasks.remove(open_tasks[0])
	if len(done) == len(abc):
		break
	table.append(timestamp)

print(time)