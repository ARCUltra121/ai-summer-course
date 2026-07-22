#Lesson 5 Notes
import random
# #RPS Game
# #As khow many games
# ##User input can only be an odd number
# #
# running = True

# games = int(input("How many games of Rock, Paper Scissors would you like to play? (Only accepting odd numbers) "))

# rps_choices = ['rock', 'paper', 'scissors']


# while running == True:
#     comp_wins = 0
#     user_wins = 0
#     ties = 0

#     if games % 2 == 1 and game < 10 :
#         for game in range(games):
#             computer_choice = random.choice(rps_choices)

#             user_choice = input("Please input either Rock, Paper, or Scissors: ").lower()
#             if (computer_choice == rps_choices[0] and user_choice == 'scissors') or (computer_choice == rps_choices[1] and user_choice == 'rock') or (computer_choice == rps_choices[2] and user_choice == 'paper'):
#                 print(f"Computer wins. You chose {user_choice.capitalize()} and Computer chose {computer_choice.capitalize()}")
#                 comp_wins += 1
#             elif computer_choice == user_choice.capitalize():
#                 print(f'Tie. Try again. You both chose {computer_choice.capitalize()}')
#                 ties += 1
#             else:
#                 print(f"Player wins.  You chose {user_choice.capitalize()} and Computer chose {computer_choice.capitalize()}")
#                 user_wins += 1

#             print(f'Player Wins: {user_wins}')
#             print(f'Computer Wins: {comp_wins}')
#             print(f'Ties: {ties}')

#             if (user_wins / games) > 0.50:
#                 print(f"Player has won the best of {games} series!")

#                 running = False
#             elif (comp_wins / games) > 0.50:
#                 print(f"Computer has won the best of {games} series!")
#                 running = False
#     else:
#         games = int(input("How many games of Rock, Paper Scissors would you like to play? (Only accepting odd numbers): "))



# Class Exercise 2
# def calculate_compound_interest(principal, interest_rate, year_time, number_int_compounds = 1 ):
#     amount = principal * ((1 + (interest_rate / number_int_compounds)) ** (number_int_compounds * year_time))
#     return amount
# print(f'$ {calculate_compound_interest(1000, 0.0061, 10):.02f}')


#First File IO class exercise
# with open('rando.txt', 'w') as f:
#     for i in range(0, 100):
#         f.write(f'{str(random.randint(50, 100))} \n')

# with open('rando.txt.', 'r') as f:
#     numbers = f.readlines()
#     cleaned_numbers = []
#     for i in numbers:
#         clean_item = i.replace(' \n', '')
#         cleaned_numbers.append(int(clean_item))

#     cleaned_numbers = sorted(cleaned_numbers)
#     min_num = cleaned_numbers[0]
#     max_num = cleaned_numbers[-1]
#     median = cleaned_numbers[int(len(cleaned_numbers) / 2)]

#     total = 0
#     for i in cleaned_numbers:
#         total += i
#     average = total / len(cleaned_numbers)
    

# print(cleaned_numbers)
# print(f'Min number: {min_num}')
# print(f'Max number: {max_num}')
# print(f'Median: {median}')
# print(f'Average: {average:.02f}')

