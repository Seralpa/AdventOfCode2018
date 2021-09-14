with open("input.txt", "r") as f:
	lines = f.readlines()

boxes_2x = 0
boxes_3x = 0
for line in lines:
	twice = False
	thrice = False
	for l in line:
		count = line.count(l)
		if count == 2:
			twice = True
		if count == 3:
			thrice = True
		if twice and thrice:
			break
		line.replace(l, "")
	if twice:
		boxes_2x += 1
	if thrice:
		boxes_3x += 1

print(f"part 1: {boxes_2x * boxes_3x}")
