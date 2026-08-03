user_name = input("What is your name? ")
user_fav_number = int(input("What is your favorite number? "))

border_num = 0

if user_fav_number < 10 and user_fav_number > 0:
    border_num = 29
elif user_fav_number >=10 and user_fav_number <= 100:
    border_num = 30
else:
    print('Error')

for i in range(border_num):
    print("*", end='')

print()
print(f"* Hello, {user_name}!          *")
print(f"* Your Favorite number is {user_fav_number} *")

for i in range(border_num):
    print("*", end='')
    
print()

print(type(user_name))
print(type(user_fav_number))
user_fav_number = float(user_fav_number)
print(type(user_fav_number))
