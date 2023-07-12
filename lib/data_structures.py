spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5 ]

def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        food_info = f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level}'
        print(food_info)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_foods:
        heat_level = "🌶" * food["heat_level"]
        food_info = f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level}'
        print(food_info)

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat_level += food["heat_level"]

    if num_foods == 0:
        return 0

    average = total_heat_level / num_foods
    return int(average)

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
