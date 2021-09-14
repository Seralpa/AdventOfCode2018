from __future__ import annotations


class Car:
	def __init__(self, pos: tuple[int, int], direction: tuple[int, int]):
		self.pos = pos
		self.dir = direction # format: (i,j) i positive down j positive right
		self.next_intersect = 0 # 0->left 1->straight 2->right
		self.crashed = False

	def move(self, tracks: list[list[str]]):
		if tracks[self.pos[0]][self.pos[1]] == '+':
			self.turn()
		elif tracks[self.pos[0]][self.pos[1]] == '/':
			if self.dir == (-1, 0):
				self.dir = (0, 1)
			elif self.dir == (0, -1):
				self.dir = (1, 0)
			elif self.dir == (1, 0):
				self.dir = (0, -1)
			elif self.dir == (0, 1):
				self.dir = (-1, 0)
		elif tracks[self.pos[0]][self.pos[1]] == '\\':
			if self.dir == (-1, 0):
				self.dir = (0, -1)
			elif self.dir == (0, -1):
				self.dir = (-1, 0)
			elif self.dir == (1, 0):
				self.dir = (0, 1)
			elif self.dir == (0, 1):
				self.dir = (1, 0)
		self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])

	def check_crash(self, cars: list[Car]):
		if self.crashed:
			return True
		for c in cars:
			if c != self and c.pos == self.pos and not c.crashed:
				self.crashed = True
				c.crashed = True
				return True
		return False

	def turn(self):
		if self.next_intersect == 0: # left
			if self.dir == (0, 1):
				self.dir = (-1, 0)
			elif self.dir == (0, -1):
				self.dir = (1, 0)
			elif self.dir == (1, 0):
				self.dir = (0, 1)
			elif self.dir == (-1, 0):
				self.dir = (0, -1)
		elif self.next_intersect == 2: # right
			if self.dir == (0, 1):
				self.dir = (1, 0)
			elif self.dir == (0, -1):
				self.dir = (-1, 0)
			elif self.dir == (1, 0):
				self.dir = (0, -1)
			elif self.dir == (-1, 0):
				self.dir = (0, 1)
		self.next_intersect = (self.next_intersect + 1) % 3
