import re
from collections import Counter

asleep = re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) [0-9]+:([0-9]+)\] falls asleep")
wake = re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) [0-9]+:([0-9]+)\] wakes up")
guard = re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) ([0-9]+):([0-9]+)\] Guard #([0-9]+) begins shift")


class Guardia:
	def __init__(self, id: int):
		self.id = id
		self.sleeps = list()
		self.wakes = list()
		self.turns = list()

	def add_turn(self, date, minutes):
		self.turns.append((date, minutes))

	def add_wake(self, date, minutes):
		self.wakes.append((date, minutes))

	def add_sleep(self, date, minutes):
		self.sleeps.append((date, minutes))

	def get_dates(self):
		return [date for date, _ in self.turns]

	def get_guard_time(self, date, minutes):
		for t in self.turns:
			if t[0] == date:
				return minutes - t[1]

	def get_asleep_minutes(self):
		mins = list()
		for s in self.sleeps:
			min_mins_asleep = 60
			wake = 0
			for w in self.wakes:
				if s[0] != w[0]:
					continue
				mins_asleep_today = w[1] - s[1]
				if mins_asleep_today < min_mins_asleep and mins_asleep_today > 0:
					min_mins_asleep = mins_asleep_today
					wake = w
			mins.extend(range(s[1], wake[1]))
		return mins


guards: list[Guardia] = list()

with open("input.txt", "r") as f:
	lines = f.readlines()

for l in lines:
	# guard shifts
	if guard.match(l):
		id = int(guard.match(l).group(4))
		minutes = int(guard.match(l).group(3))
		hours = int(guard.match(l).group(2))
		date = list(guard.match(l).group(1))
		dia = int(date[8] + date[9])
		mes = int(date[5] + date[6])

		# if record is before midnight add 1 to the day to match it with other events that night
		# minutes also become negative from midnight (23:59 -> 00:-01)
		if hours != 0:
			hours = 0
			minutes = minutes - 60
			# if day is the last of the month we also have to increment the month
			if (dia == 31) or (mes in [4, 6, 9, 11] and dia == 30) or (mes == 2 and dia == 28):
				dia = 1
				mes += 1
			else:
				dia += 1

			# store new updated data in date
			if mes < 10:
				date[5] = "0"
				date[6] = str(mes)
			else:
				date[5] = str(mes)[0]
				date[6] = str(mes)[1]
			if dia < 10:
				date[8] = "0"
				date[9] = str(dia)
			else:
				date[8] = str(dia)[0]
				date[9] = str(dia)[1]

		if not any([g for g in guards if id == g.id]):
			guards.append(Guardia(id))

		# add turn info to this guard
		for g in guards:
			if g.id == id:
				g.add_turn(date, minutes)

for l in lines:
	if asleep.match(l):
		date = list(asleep.match(l).group(1))
		minutes = int(asleep.match(l).group(2))
		min_diff = 120
		guard = None
		for g in guards:
			if date in g.get_dates():
				diff = g.get_guard_time(date, minutes)
				if diff < min_diff and diff >= 0:
					min_diff = diff
					guard = g
		guard.add_sleep(date, minutes)
	elif wake.match(l):
		date = list(wake.match(l).group(1))
		minutes = int(wake.match(l).group(2))
		min_diff = 120
		guard = None
		for g in guards:
			if date in g.get_dates():
				diff = g.get_guard_time(date, minutes)
				if diff < min_diff and diff >= 0:
					min_diff = diff
					guard = g
		guard.add_wake(date, minutes)

max_guard = max(guards, key = lambda g: len(g.get_asleep_minutes()))
cnt = Counter(max_guard.get_asleep_minutes())
print(max_guard.id * cnt.most_common(1)[0][0])
