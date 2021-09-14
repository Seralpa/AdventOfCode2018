abc = "abcdefghijklmnopqrstuvwxyz"
with open("input.txt", "r") as f:
	full_polymer = f.readline().strip()
sizes = []
for char in abc:
	# this program takes a while so progress updates were added
	print(f"Progress update: testing unit {char}")
	polymer = list(full_polymer.replace(char, "").replace(char.upper(), ""))
	modified = True
	while modified:
		modified = False
		for c in range(len(polymer) - 1):
			if abs(ord(polymer[c]) - ord(polymer[c + 1])) == 32:
				del polymer[c : c + 2]
				modified = True
				break
	sizes.append(len(polymer))
print(min(sizes))