###
# Lesson 1 - Intro to Python 10 JULY 2026
###
import math

#Pizza Calculator

pi = 3.14159

pizza_area = float(input("What is the diameter of the pizza you're buying? "))
pizza_cost = float(input("What is the pizza cost? "))

pizza_area_calculated = pi * (pizza_area **2) 

pizza_cost_per_inch = pizza_cost / pizza_area_calculated

print(f'Pizza area is calculated at {pizza_area_calculated:.02f}')

print(f'Cost of the pizza per square inch is: ${pizza_cost_per_inch:.02f}')
