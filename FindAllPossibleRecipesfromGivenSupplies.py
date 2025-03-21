# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".

def findAllRecipes(recipes, ingredients, supplies):
    supplies = set(supplies)
    recipes = dict(zip(recipes, ingredients))
    made = []
    while True:
        new_recipe_made = False
        for rcp, igs in [*recipes.items()]:
            if not all(i in supplies for i in igs):
                continue
            made.append(rcp)
            supplies.add(rcp)
            del recipes[rcp]
            new_recipe_made = True
        if not new_recipe_made:
            break
    return made

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
print(findAllRecipes(recipes, ingredients, supplies)) 