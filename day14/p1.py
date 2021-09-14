def divide_recipes(recipe):
	if recipe > 9:
		return [recipe // 10, recipe % 10]
	else:
		return [recipe]


n_recipes = 894501
recipes = [3, 7]
current = (0, 1)

while len(recipes) < n_recipes + 10:
	new_recipe = recipes[current[0]] + recipes[current[1]]
	recipes += divide_recipes(new_recipe)
	current = ((recipes[current[0]] + 1 + current[0]) % len(recipes),
	           (recipes[current[1]] + 1 + current[1]) % len(recipes))

print("".join([str(r) for r in recipes[n_recipes : len(recipes)]]))
