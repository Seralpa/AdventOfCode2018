def divideRecipes(recipe):
    if recipe>9:
        recipes="".join((str(recipe//10),str(recipe%10)))
    else:
        recipes=str(recipe)
    return recipes

patron="430971"
recipes="37"
current=(0,1)

it=0
while True:
    newRecipe=int(recipes[current[0]])+int(recipes[current[1]])
    newRecipes=divideRecipes(newRecipe)
    recipes+=newRecipes
    current=((int(recipes[current[0]])+1+current[0])%len(recipes), (int(recipes[current[1]])+1+current[1])%len(recipes))
    if it%1000000==0:
        print(it)
        index=recipes.find(patron)
        if index!=-1:
            print(index)
            break
    it+=1