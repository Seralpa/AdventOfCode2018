import re

instruction_line = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

instructions = []
with open("input.txt", "r") as f:
	for l in f:
		instructions.append((instruction_line.match(l).group(1), instruction_line.match(l).group(2)))

tasks = ""
while len(abc) > 0:
	not_yet = [i[1] for i in instructions]
	for a in abc:
		if not a in not_yet:
			tasks += a
			abc = abc.replace(a, "")
			instructions = [i for i in instructions if i[0] != a]
			break
print(tasks)