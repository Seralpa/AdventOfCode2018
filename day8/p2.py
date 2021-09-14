from Node import Node

with open("input.txt", "r") as f:
	data = [int(d) for d in f.readline().strip().split()]

padre = Node(None, data.pop(0), data.pop(0))

padre.add_children(data)

print(padre.get_value())