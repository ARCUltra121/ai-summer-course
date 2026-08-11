import math

def automatron_one_efficiency():
    units = 20
    diameter = 15
    pizzas = 2
    area = math.pi * ((diameter / 2)**2)
    pizza_total = (pizzas * area) / units
    return pizza_total

def automatron_two_efficiency():
    units = 20
    side_length = 20
    formula = (math.sqrt(3) / 4) * (side_length ** 2)

    pizza_total = (2 * formula) / units
    return pizza_total

def automatron_three_efficiency():
    side_length = 18
    units = 18
    area = side_length ** 2
    pizza_total = area / units
    return pizza_total


print(f'Area per unit of Automatron 1: {automatron_one_efficiency()}')
print(f'Area per unit of Automatron 2: {automatron_two_efficiency()}')
print(f'Area per unit of Automatron 3: {automatron_three_efficiency()}')