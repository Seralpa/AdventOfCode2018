import re
import operator

data = re.compile(r"position=< ?(-?[0-9]+),  ?(-?[0-9]+)> velocity=< ?(-?[0-9]+),  ?(-?[0-9]+)>")


class Point:
	def __init__(self, pos: tuple[int, int], vel: tuple[int, int]):
		self.pos = pos
		self.vel = vel

	def move(self):
		self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


def print_pos(points: list[Point], minx, maxx):
	prev_point = points[0]
	for p in points:
		if p == points[0]:
			for _ in range(p.pos[0] - minx):
				print('.', end = '')
			print('#', end = '')
			continue

		if p.pos == prev_point.pos:
			continue

		if p.pos[1] == prev_point.pos[1]:
			for _ in range(p.pos[0] - prev_point.pos[0] - 1):
				print('.', end = '')
		else:
			for _ in range(maxx - prev_point.pos[0]):
				print('.', end = '')
			for _ in range(p.pos[1] - prev_point.pos[1]):
				print('')
			for _ in range(p.pos[0] - minx):
				print('.', end = '')
		print('#', end = '')
		prev_point = p
	print('')


points: list[Point] = list()
with open("input.txt", "r") as f:
	for l in f:
		matcher = data.match(l)
		points.append(Point((int(matcher.group(1)), int(matcher.group(2))), (int(matcher.group(3)), int(matcher.group(4)))))

time = 0
while True:
	minx = min(points, key = lambda x: x.pos[0]).pos[0]
	maxx = max(points, key = lambda x: x.pos[0]).pos[0]
	if maxx - minx < 100:
		points.sort(key = lambda x: x.pos[0])
		points.sort(key = lambda y: y.pos[1])
		print('')
		print_pos(points, minx, maxx)
		print(f"{time = }")
		input("Enter to keep going")
	for p in points:
		p.move()
	time += 1
