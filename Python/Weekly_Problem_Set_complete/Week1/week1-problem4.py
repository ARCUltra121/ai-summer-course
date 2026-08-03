import math
distance = int(input("What is the distance of the trip in miles? "))
fuel_efficiency = float(input("What is your car's miles per gallon rating? "))
gas_price = float(input("What is the gas price in dollars? (Format: X.XX) "))

gallons_needed = distance / fuel_efficiency
total_cost = gas_price * gallons_needed

def trip_calculator():
    print(f"~~~")
    print(f"--- Road Trip Fuel Estimate ---")
    print(f"Distance: {distance} miles")
    print(f"Fuel Efficiency: {fuel_efficiency} MPG")
    print(f"Gas price: ${gas_price:.02f} / gallon")
    print(f"")
    print(f"Gallons needed: {gallons_needed:.01f}")
    print(f"Total Fuel cost: ${math.ceil(total_cost):.02f}")
    print(f"~~~")

trip_calculator()