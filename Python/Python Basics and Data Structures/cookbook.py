from recipes import recipes

for recipe in recipes:
    print(f"{recipe['name']} ingredients needed:")
    
    for ingredients in recipe['ingredients']:
        for ingredient, amount in ingredients.items():
            print(f"{ingredient} - {amount}")

    print(f"Instructions to cook:\n{recipe['instructions']}")
    break