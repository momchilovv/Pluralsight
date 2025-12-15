from recipes import recipes

def list_recipes():
    for recipe in recipes:
        print(f"Recipe: {recipe['name']}")
        for ingredients in recipe['ingredients']:
            ingredient_list = [f"{amount} {name}" for name, amount in ingredients.items()]
            print(f"Ingredients: {", ".join(ingredient_list)}")
        print(f"Instructions: {recipe['instructions']}")
        print(f"{"-" * (len(recipe['instructions']) + 14)}")

def get_recipe():
    recipe_name = input("Enter the recipe you are looking for: ")
    
    found = [recipe for recipe in recipes if recipe_name.lower() in recipe['name'].lower()]

    if found:
        print(f"Found {len(found)} recipes:")
        for recipe in found:
            ingredients = [f"{amount} {name}" for name, amount in recipe['ingredients'][0].items()]
            print(f"Recipe: {recipe['name']}\nIngredients: {", ".join(ingredients)}\nInstructions: {recipe['instructions']}")
    else:
        print("No matching recipes found.")
