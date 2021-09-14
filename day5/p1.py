with open("input.txt", "r") as f:
	polymer = list(f.readline().strip())

modified = True
while modified:
	modified = False
	for c in range(len(polymer) - 1):
		if abs(ord(polymer[c]) - ord(polymer[c + 1])) == 32:
			del polymer[c : c + 2]
			modified = True
			break
print(len(polymer))