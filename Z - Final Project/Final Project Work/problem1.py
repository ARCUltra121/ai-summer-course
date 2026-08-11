user_input:str = input("Input either 'Miles above Mars' or 'Kilometers above Mars': ").lower()
user_num:int = int(input("Enter a number: "))
if user_input == 'miles above mars':
    print(f'Yards: {user_num * 1760}')
    print(f'Feet: {user_num * 5280}')
    print(f'Inches: {user_num * 63360}')
elif user_input == 'milometers above mars':
    print(f'Meters: {user_num * 1000}')
    print(f'Centimeters: {user_num * 100000}')
    print(f'Millimeters: {user_num * 100000000}')