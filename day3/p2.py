class Rectangle:
	def __init__(self, offset, size, id):
		self.offset = (int(offset[0]), int(offset[1]))
		self.size = (int(size[0]), int(size[1]))
		self.id = id

	def fillRect(self, matrix):
		for i in range(self.offset[0], self.offset[0] + self.size[0]):
			for j in range(self.offset[1], self.offset[1] + self.size[1]):
				if matrix[i][j] != 0:
					matrix[i][j] = "x"
				else:
					matrix[i][j] = id

	def isFull(self, matrix):
		for i in range(self.offset[0], self.offset[0] + self.size[0]):
			for j in range(self.offset[1], self.offset[1] + self.size[1]):
				if matrix[i][j] == "x":
					return False
		return True


matrix = [[0 for i in range(1000)] for j in range(1000)]
rect_list = []

with open("input.txt", "r") as f:
	for l in f:
		l = l.split()
		id = int(l[0].replace("#", ""))
		distancias = l[2].replace(":", "").split(",")
		tam = l[3].split("x")
		rect = Rectangle(distancias, tam, id)
		rect.fillRect(matrix)
		rect_list.append(rect)

for r in rect_list:
	if r.isFull(matrix):
		print(f"part 2: {r.id}")
