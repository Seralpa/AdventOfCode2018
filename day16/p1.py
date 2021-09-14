import re

re_before = re.compile(r"Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)]")
re_instruction = re.compile(r"([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)")
re_after = re.compile(r"After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)]")


def execute(instruction: list[int], registers: list[int]):
	if instruction[0] == 0: # addr
		registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
	elif instruction[0] == 1: # addi
		registers[instruction[3]] = registers[instruction[1]] + instruction[2]
	elif instruction[0] == 2: # mulr
		registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
	elif instruction[0] == 3: # muli
		registers[instruction[3]] = registers[instruction[1]] * instruction[2]
	elif instruction[0] == 4: # banr
		registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
	elif instruction[0] == 5: # bani
		registers[instruction[3]] = registers[instruction[1]] & instruction[2]
	elif instruction[0] == 6: # borr
		registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
	elif instruction[0] == 7: # bori
		registers[instruction[3]] = registers[instruction[1]] | instruction[2]
	elif instruction[0] == 8: # setr
		registers[instruction[3]] = registers[instruction[1]]
	elif instruction[0] == 9: # seti
		registers[instruction[3]] = instruction[1]
	elif instruction[0] == 10: # gtir
		if instruction[1] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 11: # gtri
		if registers[instruction[1]] > instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 12: # gtrr
		if registers[instruction[1]] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 13: # eqir
		if instruction[1] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 14: # eqri
		if registers[instruction[1]] == instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 15: # eqrr
		if registers[instruction[1]] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0


before: list[list[int]] = list()
after: list[list[int]] = list()
instructions: list[list[int]] = list()
with open("input.txt") as f:
	part1 = f.read().split("\n\n\n\n")[0]
	for line in part1.splitlines():
		if re_before.match(line):
			matcher = re_before.match(line)
			before.append([int(matcher.group(1)), int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(4))])
		elif re_after.match(line):
			matcher = re_after.match(line)
			after.append([int(matcher.group(1)), int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(4))])
		elif re_instruction.match(line):
			matcher = re_instruction.match(line)
			instructions.append([int(matcher.group(1)), int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(4))])
count = 0
for ins in range(len(instructions)):
	matches = 0
	for i in range(16):
		before_cp = before[ins][:]
		execute([i, instructions[ins][1], instructions[ins][2], instructions[ins][3]], before_cp)
		if before_cp == after[ins]:
			matches += 1
	if matches >= 3:
		count += 1

print(count)