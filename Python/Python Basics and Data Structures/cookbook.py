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

def find_recipes_by_ingredients(available_ingredients):
    matching_recipes = []
    for recipe in recipes:
        recipe_ingredients = recipe['ingredients'][0].keys()
        if all(ingredient in available_ingredients for ingredient in recipe_ingredients):
            matching_recipes.append(recipe)

    return matching_recipes

def main():
    print("Welcome to the Recipe CLI Applicaiton!")

    while True:
        print("\nChoose an option:")
        print("1. List all recipes")
        print("2. Search for recipes")
        print("3. Search by available ingredients")
        print("4. Exit\n")

        choice = input("Choose a number: ")

        if choice == "1":
            list_recipes()
        elif choice == "2":
            get_recipe()
        elif choice == "3":
            available_ingredients = input("Enter the ingredients you have (comma-separated): ").split(', ')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]

            matching_recipes = find_recipes_by_ingredients(available_ingredients)

            if matching_recipes:
                print("You can make the following recipes:")
                for recipe in matching_recipes:
                    print(recipe['name'])
            else:
                print("No recipes found with the given ingredients.")
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice!")

main()