class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set):
        return all(
            ingredient in pantry_set for ingredient in self.ingredients
        )

    def missing_ingredients(self, pantry_set):
        missing = [
            ingredient
            for ingredient in self.ingredients
            if ingredient not in pantry_set
        ]
        missing.sort()
        return missing


class Pantry:
    def __init__(self, ingredients):
        self.ingredients = set(ingredients)

    def add_ingredients(self, extra_ingredients):
        self.ingredients.update(extra_ingredients)

    def has(self, ingredient):
        return ingredient in self.ingredients


def create_recipes(recipe_data):
    recipes = []

    for name, ingredients in recipe_data.items():
        recipes.append(Recipe(name, ingredients))

    return recipes


def check_recipes(recipes, pantry):
    all_ingredients = set()

    for recipe in recipes:
        all_ingredients.update(recipe.ingredients)

        if recipe.can_make(pantry.ingredients):
            print(f"{recipe.name:<15}: CAN MAKE")
        else:
            missing = recipe.missing_ingredients(pantry.ingredients)
            print(f"{recipe.name:<15}: MISSING — {missing}")

    unique_ingredients = sorted(all_ingredients)

    print()
    print(
        f"All unique ingredients ({len(unique_ingredients)}): "
        f"{unique_ingredients}"
    )


if __name__ == "__main__":
    recipe_data = {
        "omelette": [
            "eggs",
            "butter",
            "salt",
            "pepper",
            "cheese"
        ],
        "pancakes": [
            "flour",
            "eggs",
            "milk",
            "butter",
            "sugar",
            "salt"
        ],
        "tomato pasta": [
            "pasta",
            "tomatoes",
            "garlic",
            "olive oil",
            "salt",
            "pepper"
        ],
        "grilled cheese": [
            "bread",
            "cheese",
            "butter"
        ]
    }

    pantry_items = [
        "eggs",
        "butter",
        "salt",
        "pepper",
        "cheese",
        "milk",
        "bread",
        "garlic"
    ]

    recipes = create_recipes(recipe_data)
    pantry = Pantry(pantry_items)

    print("=== RECIPE CHECKER ===")
    check_recipes(recipes, pantry)

    extra_input = input(
        "\nEnter extra ingredients separated by commas: "
    )

    extra_ingredients = [
        ingredient.strip()
        for ingredient in extra_input.split(",")
        if ingredient.strip()
    ]

    pantry.add_ingredients(extra_ingredients)

    print()
    print("Recipes after adding ingredients:")
    check_recipes(recipes, pantry)
