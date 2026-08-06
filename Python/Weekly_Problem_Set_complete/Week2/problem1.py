import math
def pizza_calc(people, slices_per_person, slices_per_pizza):
    return math.ceil((people * slices_per_person) / slices_per_pizza)

print(f"You need {pizza_calc(3, 3, 8)} pizzas.")