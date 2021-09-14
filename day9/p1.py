import re

data = re.compile(r"([0-9]+) players; last marble is worth ([0-9]+) points")
players = []
circle = [0, 1]

with open("input.txt", "r") as f:
	line = f.readline().strip()
	n_players = int(data.match(line).group(1))
	n_marbles = int(data.match(line).group(2))

for _ in range(n_players):
	players.append(0)
current = 1
for i in range(2, n_marbles + 1):
	if i % 23 == 0:
		players[i % len(players) - 1] += i
		players[i % len(players) - 1] += circle.pop(current - 7)
		current -= 7
	else:
		current = (current + 2) % len(circle)
		circle.insert(current, i)

print(max(players))