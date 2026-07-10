#Best deal calculator for Pizza
pi = 3.14159
pizza1_diameter = int(input("What is the diameter of the 1st pizza you're buying? "))
pizza2_diameter = int(input("What is the diameter of the 2nd pizza you're buying? "))

pizza1_cost = float(input("What is the 1st pizza cost? "))
pizza2_cost = float(input("What is the 2nd pizza cost? "))


pizza1_area_calculated = pi * (pizza1_diameter **2) 
pizza1_cost_per_inch = pizza1_cost / pizza1_area_calculated

print(f'Pizza area is calculated at {pizza1_area_calculated:.02f}')
print(f'Cost of the pizza per square inch is: ${pizza1_cost_per_inch:.02f}', end='\n')

pizza2_area_calculated = pi * (pizza2_diameter **2) 
pizza2_cost_per_inch = pizza2_cost / pizza2_area_calculated


print(f'Pizza area is calculated at {pizza1_area_calculated:.02f}')
print(f'Cost of the pizza per square inch is: ${pizza1_cost_per_inch:.02f}', end='\n')

print(f'1st Pizza area is calculated at {pizza1_area_calculated:.02f}')

print(f'1st Pizza Cost per square inch is: ${pizza1_cost_per_inch:.02f}', end='\n')

print(f'2nd Pizza area is calculated at {pizza2_area_calculated:.02f}')

print(f'2nd Pizza Cost per square inch is: ${pizza2_cost_per_inch:.02f}', end ='\n')

if pizza1_cost_per_inch > pizza2_cost_per_inch:
    print('Pizza 1 is the better deal!')
elif pizza1_cost_per_inch == pizza2_cost_per_inch:
    print("It's the same deal!")
else:
    print("Pizza 2 is the better deal!")