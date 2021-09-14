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


matrix = [[0 for i in range(1000)] for j in range(1000)]
with open("input.txt", "r") as f:
	for line in f:
		line = line.split()
		id = int(line[0].replace("#", ""))
		offset = line[2].replace(":", "").split(",")
		size = line[3].split("x")
		rect = Rectangle(offset, size, id)
		rect.fillRect(matrix)

cont = 0
for line in matrix:
	cont += line.count("x")
print(f"part 1: {cont}")
