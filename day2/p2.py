import sys

with open("input.txt", "r") as f:
	boxes = f.readlines()

for b1 in boxes:
	boxes.remove(b1)
	for b2 in boxes:
		# assumes IDs are the same length
		out = [c1 for c1, c2 in zip(b1, b2) if c1 == c2]
		if len(out) == len(b1) - 1 == len(b2) - 1:
			print(f"part 2: {''.join(out)}")
