import random
roll_count = 0


def roll(sides):
    return random.randint(1, sides)

def roll_many(dice_num, sides):
    roll_list = [roll(sides) for i in range(dice_num)]
    return roll_list

rolls = roll_many(2,6)

for i in rolls:
    roll_count += 1
    print(f'Roll {roll_count}: {i}')