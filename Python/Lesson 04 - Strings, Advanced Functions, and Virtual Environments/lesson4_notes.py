# my_list = ['c','a','t']
# my_str = "cat"

# for i in my_list:
#     print(i, end=' ')

# print()
# for i in my_str:
#     print(i, end =' ')

# print()
# print(my_list[0], my_str[0])
# print(my_list[-1], my_str[-1])
# print(my_str[:2])
# print(len(my_list), len(my_str))
# print('a' in my_list, 'a' in my_str)

# print(list('cat'))

# new_string = my_list.join()

# print(new_string)

# def validate_username(username:str):
#     if len(username) >= 5 and len(username) <= 15:
#         if username.isalnum() == True or  '_' in username[0:]:
#             if username[0].isalpha() == True:
#                 if username.endswith('_') == False:
#                     for i in range(0, 10):
#                         if str(i) in username[:]:
#                             return True

# print(validate_username('f___ob1700by'))


# def greet(name, greeting = "What's up!"):
#     return print(f'{greeting} {name}!')

# greet('Reggie')

passengers = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

def print_boarding_list(passengers:list):
    for index, passenger in enumerate(passengers, 1):
        print(f'Seat {index}: {passenger}')

print_boarding_list(passengers)