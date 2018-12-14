def divideRecipes(recipe):
    recipes=[]
    if recipe>9:
        recipes=[recipe//10,recipe%10]
    else:
        recipes=[recipe]
    return recipes

numRecipes=430971
recipes=[3,7]
current=(0,1)



while len(recipes)<numRecipes+10:
    newRecipe=recipes[current[0]]+recipes[current[1]]
    newRecipes=divideRecipes(newRecipe)
    recipes.extend(newRecipes)
    current=((recipes[current[0]]+1+current[0])%len(recipes), (recipes[current[1]]+1+current[1])%len(recipes))

    

print("".join([str(r) for r in recipes[numRecipes:len(recipes)]]))