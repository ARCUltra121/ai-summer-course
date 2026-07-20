# Lesson 3 Notes
import random

#Problem 1
# for i in range(1, 101):
#     print(i, end=' ')
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizzbuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print()

#Problem 2
# list_choices = ['Rock', 'Paper', 'Scissors']

# computer_choice = random.choice(list_choices)

# user_choice = input("Choose one: Rock, Paper, or Scissors: ").lower()

# if (computer_choice == list_choices[0] and user_choice == 'scissors') or (computer_choice == list_choices[1] and user_choice == 'rock') or (computer_choice == list_choices[2] and user_choice == 'paper'):
#     print(f"Computer wins. You chose {user_choice.capitalize()} and Computer chose {computer_choice.capitalize()}")
# elif computer_choice == user_choice.capitalize():
#     print(f'Tie. Try again. You both chose {computer_choice.capitalize()}')
# else:
#     print(f"Player wins.  You chose {user_choice.capitalize()} and Computer chose {computer_choice.capitalize()}")

#Problem 3
# running = True
# random_number = random.randint(1, 100)


# while running == True:
#     user_guess = int(input("TRY TO GUESS THE NUMBER: "))

#     if user_guess > random_number:
#         print("Too high.")
#     elif user_guess < random_number:
#         print("Too low.")
#     elif user_guess == random_number:
#         print("You did it! Congratulations!")
#         running = False
#     else:
#         print("This shouldn't even happen but i'm putting it here anyways....")

#Problem 4
# student_num = int(input("How many students are in your class? "))

# students = []
# student_grades = []
# class_avg = 0.0

# for i in range(student_num):
#     students.append(input('Input student name: '))
#     student_grades.append(int(input('Input student grade: ')))

# for grade in student_grades:
#     class_avg += grade

# class_avg /= len(student_grades)

# student_grades_sorted = sorted(student_grades)

# lowest_grade = student_grades_sorted[0]
# highest_grade = student_grades_sorted[-1]

# print(f'The lowest grade in class is: {lowest_grade}')
# print(f'The highest grade in class is: {highest_grade}')
# print(f' The class average is: {class_avg}')

# print(f'The person with the highest grade in class is {students[student_grades.index(highest_grade)]}')


#  Class Problem numero Uno
# another_random_number = random.randint(0, 100)

# if another_random_number < 50:
#     print("The number is less than 50.")
# elif another_random_number > 50:
#     print("The number is greater than 50.")
# else:
#     print("The number is 50.")

# Class Problem Numero Dos
def rectangleArea(input1, input2):
    area = input1 * input2
    return print(area)

rectangleArea(12, 15)