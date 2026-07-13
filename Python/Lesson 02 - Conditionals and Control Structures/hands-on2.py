#Exercise 11

# fav_colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple']

# for color in fav_colors:
#     print(color)
running = True

while running == True:
    user_input = int(input("Please provide me with an even number: "))
    if user_input % 2 == 1:
        print("You provided me with an odd number you dumbfuck.")
    else:
        print(f"Thank you for the even number!, Number provided: {user_input}")
        running = False
