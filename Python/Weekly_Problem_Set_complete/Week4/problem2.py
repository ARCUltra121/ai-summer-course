recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]


class Recipe():
    #attributes
    def __init__(self, name:str, ingredients:list):
        self.name = name
        self.ingredients = ingredients
    #methods
    def 