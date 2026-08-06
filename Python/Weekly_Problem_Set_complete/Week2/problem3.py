hero_hp = 100
hero_atk = 18
enemy_hp = 90
enemy_atk = 12
rounds = 0
def attack(defender_hp, damage):
    new_def_hp = defender_hp - damage
    return new_def_hp

def is_alive(hp):
    if hp > 0:
        return True

while is_alive(hero_hp) == True and is_alive(enemy_hp) == True:
    rounds += 1
    enemy_hp = attack(enemy_hp, hero_atk)
    print(f'Round {rounds}: FIGHT!')
    if is_alive(enemy_hp):
        print(f'Hero Attacks Monster for {hero_atk} damage!')
        print(f'Hero HP: {hero_hp}', end='  |  ')
        print(f'Monster HP: {enemy_hp}')
    else:
        print(f'Ther hero has slain the monster. You gain 38 xp!')

    hero_hp = attack(hero_hp, hero_atk)
    if is_alive(hero_hp):
        print(f'Monster attacks the Hero for {enemy_atk} damage!')
        print(f'Hero HP: {hero_hp}', end='  |  ')
        print(f'Monster HP: {enemy_hp}')
    else:
        print(f'The Monster has slain the Hero. GAME OVER...')
