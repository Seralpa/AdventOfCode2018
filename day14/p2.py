def divide_recipes(recipe):
	if recipe > 9:
		recipes = "".join((str(recipe // 10), str(recipe % 10)))
	else:
		recipes = str(recipe)
	return recipes


pattern = "894501"
recipes = "37"
current = (0, 1)

it = 0
while True:
	new_recipe = int(recipes[current[0]]) + int(recipes[current[1]])
	recipes += divide_recipes(new_recipe)
	current = ((int(recipes[current[0]]) + 1 + current[0]) % len(recipes),
	           (int(recipes[current[1]]) + 1 + current[1]) % len(recipes))
	if it % 5000000 == 0:
		# this program takes a while to run, progress updates were added acordingly
		print(f"progress update: {it}")
		index = recipes.find(pattern)
		if index != -1:
			print(f"answer: {index}")
			break
	it += 1
