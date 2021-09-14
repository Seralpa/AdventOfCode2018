import sys

results = set()
result = 0
with open("input.txt", "r") as f:
	lines = [int(l) for l in f]
while True:
	for n in lines:
		if result in results:
			print(f"part 2: {result}")
			sys.exit()
		results.add(result)
		result += n
