#Lesson 9 

# def palindromechecker(input):
#     if input == "":
#         return True
#     if len(input) == 1:
#         return True
#     if input[0] != input[-1]:
#         return False

#     return palindromechecker(input[1:-1])


# def str_2_int(input:str):
#     if input.isalpha():
#         return False
#     if len(input) == 1:

#     return str

my_list = [1,2,-37]

def sum_list(input:list):
    if len(input) == 1:
        return input[0]

    return input[0] + sum(input[1:])

print(sum_list(my_list))