def operate(instruction, registers):
	if instruction[0] == 'addr': # addr
		registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
	elif instruction[0] == 'addi': # addi
		registers[instruction[3]] = registers[instruction[1]] + instruction[2]
	elif instruction[0] == 'mulr': # mulr
		registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
	elif instruction[0] == 'muli': # muli
		registers[instruction[3]] = registers[instruction[1]] * instruction[2]
	elif instruction[0] == 'banr': # banr
		registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
	elif instruction[0] == 'bani': # bani
		registers[instruction[3]] = registers[instruction[1]] & instruction[2]
	elif instruction[0] == 'borr': #borr
		registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
	elif instruction[0] == 'bori': # bori
		registers[instruction[3]] = registers[instruction[1]] | instruction[2]
	elif instruction[0] == 'setr': # setr
		registers[instruction[3]] = registers[instruction[1]]
	elif instruction[0] == 'seti': # seti
		registers[instruction[3]] = instruction[1]
	elif instruction[0] == 'gtir': # gtir
		if instruction[1] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 'gtri': # gtri
		if registers[instruction[1]] > instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 'gtrr': # gtrr
		if registers[instruction[1]] > registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 'eqir': # eqir
		if instruction[1] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 'eqri': # eqri
		if registers[instruction[1]] == instruction[2]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0
	elif instruction[0] == 'eqrr': # eqrr
		if registers[instruction[1]] == registers[instruction[2]]:
			registers[instruction[3]] = 1
		else:
			registers[instruction[3]] = 0


ip = 0
instructions = list()
with open("input.txt") as f:
	ip = int(f.readline()[4])
	instructions = [l.strip().split() for l in f.readlines()]
for i in instructions:
	for j in range(1, len(i)):
		i[j] = int(i[j])

registers = [0, 0, 0, 0, 0, 0]
while registers[ip] < len(instructions) and registers[ip] >= 0:
	operate(instructions[registers[ip]], registers)
	registers[ip] += 1
print(registers[0])