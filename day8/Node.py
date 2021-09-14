class Node:
	def __init__(self, parent, n_children: int, n_data: int):
		self.parent: Node = parent
		self.n_children = n_children
		self.n_data = n_data
		self.children: list[Node] = list()
		self.data: list[int] = list()

	def add_children(self, data: list[int]):
		for i in range(self.n_children):
			child = Node(self, data.pop(0), data.pop(0))
			child.add_children(data)
			self.children.append(child)
		self.add_data(data)

	def add_data(self, data: list):
		for _ in range(self.n_data):
			self.data.append(data.pop(0))

	def __str__(self):
		print("\nData= " + str(self.data) + "\nChildren= ")
		for h in self.children:
			print("children")
			print(h)
		if len(self.children) == 0:
			print("[]")
		return "----------END-----------"

	def sum_data(self):
		suma = sum(self.data)
		for h in self.children:
			suma += h.sum_data()
		return suma

	def get_value(self):
		if len(self.children) == 0:
			return sum(self.data)
		suma = 0
		for d in self.data:
			if d <= len(self.children):
				suma += self.children[d - 1].get_value()
		return suma
