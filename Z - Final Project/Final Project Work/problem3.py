import math


def fuel_required(mass:int):
    fuel_formula:int = math.floor(mass / 3 ) - 2
    return fuel_formula

module_num:int = int(input('How many modules are onboard?: '))

fuel_total = 0
counter = 0

while counter < module_num:
    rocket_mass:int = int(input("What is the mass of your rocket?: "))
    fuel_total += fuel_required(rocket_mass)

    print(f'Current fuel need: {fuel_total}')
    counter += 1

print(f'Full Fuel Total for ship: {fuel_total}')