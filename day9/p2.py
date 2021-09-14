import re


class Node:
	def __init__(self, data, prev, next):
		self.data = data
		self.prev: Node = prev
		self.next: Node = next

	def insert_after(self, dato):
		insertion = Node(dato, self, self.next)
		self.next.prev = insertion
		self.next = insertion

	def delete_prev(self):
		two_behind = self.prev.prev
		self.prev = two_behind
		two_behind.next = self


data = re.compile(r"([0-9]+) players; last marble is worth ([0-9]+) points")

with open("input.txt", "r") as f:
	line = f.readline().strip()
	n_players = int(data.match(line).group(1))
	n_marbles = int(data.match(line).group(2)) * 100

players = list()
for _ in range(n_players):
	players.append(0)

initial = Node(0, None, None)
current = Node(1, initial, initial)
initial.next = current
initial.prev = current
for i in range(2, n_marbles + 1):
	if i % 23 == 0:
		players[i % len(players) - 1] += i
		seven_behind = current.prev.prev.prev.prev.prev.prev.prev
		players[i % len(players) - 1] += seven_behind.data
		current = seven_behind.next
		current.delete_prev()

	else:
		current.next.insert_after(i)
		current = current.next.next

print(max(players))