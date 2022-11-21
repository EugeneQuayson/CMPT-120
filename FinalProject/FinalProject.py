k phase
import random

yes = ['yes', 'y']
no = ['no', 'n']


def attack_power():
    damage = random.randint(1, max_char_str)
    return damage


def attack1_level1():
    enemy_defense = 10
    enemy_health = 10
    overall_defense = enemy_defense + enemy_health
    attack_phase = overall_defense - attack_power()
    print("The goblin has", overall_defense, "defense")
    print("You attack for", attack_power())
    if attack_phase <= 0:
        print("You killed the goblin!")
        return True
    else:
        print("He's still alive with", attack_phase, "health!")
        return False


def min_char_def():
    if max_char_def > 10:
        minimum_char_def = max_char_def - 10
        return minimum_char_def
    else:
        minimum_char_def = random.randint(1, max_char_def)
        return minimum_char_def


def damage_taken(x):
    char_def = random.randint(min_char_def(), max_char_def)
    true_damage = x - char_def
    print("Damage Taken: ", true_damage)
    print(char_name, "'s Defense: ", char_def)
    if true_damage >= 0:
        remaining_health = start_char_health - true_damage
        print("Remaining Health: ", remaining_health)
    else:
        new_def = max_char_def - true_damage
        print("Shield: ", new_def)


char_name = input("Enter your name: ")
max_char_str = 100
max_char_def = 50
start_char_health = 100
print("Health: ", start_char_health)
print("Shield: ", max_char_def)


def level1():
    def enemy1_level1():
        damage = random.randint(1, 20)
        print("You enter a cave and inside lies a goblin.", "He attacks you doing", damage, "damage")
        return damage

    while True:
        fight1_level1 = input("Would you like to fight? ")
        if fight1_level1.lower() in yes:
            damage_taken(enemy1_level1())
            break
        elif fight1_level1.lower() in no:
            print("Too bad!")
            damage_taken(enemy1_level1())
            break
        else:
            print("yes or no")

    attack1_level1_option = input("Do you attack? ")
    if attack1_level1_option.lower() in yes:
        print("You strike back!")
        attack1_level1()
    elif attack1_level1_option.lower() in no:
        print("You have no choice")
        attack1_level1()

    if attack1_level1() is True:
        print("You win the game!")
        print("Thanks for playing")
    elif attack1_level1() is False:
        print("You run out of the cave screaming!")
        print("Maybe you'll get him next time")


level1()
