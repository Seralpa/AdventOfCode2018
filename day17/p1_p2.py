import re
from operator import itemgetter

re_range = re.compile(r"[a-z]=(\d+)..(\d+)")

walls = set()
with open("input_new.txt", "r") as f:
	for l in f:
		c1, c2 = l.strip().split(", ")
		if c1[0] == 'x':
			j = int(c1[2 :])
			if re_range.match(c2):
				for i in range(int(re_range.match(c2).group(1)), int(re_range.match(c2).group(2)) + 1):
					walls.add((i, j))
			else:
				i = int(c2[2 :])
				walls.add((i, j))
		else:
			i = int(c1[2 :])
			if re_range.match(c2):
				for j in range(int(re_range.match(c2).group(1)), int(re_range.match(c2).group(2)) + 1):
					walls.add((i, j))
			else:
				j = int(c2[2 :])
				walls.add((i, j))
walls = list(walls)
miny = min(walls, key = itemgetter(0))[0]
maxy = max(walls, key = itemgetter(0))[0]
maxx = max(walls, key = itemgetter(1))[1] + 1

scan = [['.' for _ in range(maxx + 1)] for _ in range(maxy + 2)]

for m in walls:
	scan[m[0]][m[1]] = '#'

scan[0][500] = '|'
prev_flowing_count = 0
prev_still_count = 0
while True:
	for i in range(len(scan)):
		for j in range(len(scan[i])):
			if scan[i][j] == '|' and i < len(scan) - 1:
				if scan[i + 1][j] == '.':
					scan[i + 1][j] = '|'
				elif scan[i + 1][j] != '|':
					if scan[i][j - 1] == '.':
						scan[i][j - 1] = '|'
					if scan[i][j + 1] == '.':
						scan[i][j + 1] = '|'
			elif scan[i][j] == '#':
				has_water = False
				convert_still = False
				for j1 in range(j + 1, len(scan[i])):
					if not has_water and scan[i][j1] == '|':
						has_water = True
					if scan[i + 1][j1] == '.' or scan[i + 1][j1] == '|' or scan[i][j1] == '~':
						break
					if scan[i][j1] == '#':
						convert_still = True
						finj = j1
						break
				# convert water to still
				if has_water and convert_still:
					for j2 in range(j + 1, finj):
						scan[i][j2] = '~'
	flowing_count = 0
	still_count = 0
	for i in range(len(scan)):
		for j in range(len(scan[i])):
			if i >= miny and i <= maxy:
				if scan[i][j] == '|':
					flowing_count += 1
				elif scan[i][j] == '~':
					still_count += 1
	if flowing_count == prev_flowing_count and still_count == prev_still_count:
		break
	prev_flowing_count = flowing_count
	prev_still_count = still_count
	# this program takes a while to run, so progress updates were added
	print(f"Progress update: {flowing_count = }, {still_count = }")

print(f"part 1: {flowing_count + still_count}")
print(f"part 2: {still_count}")
