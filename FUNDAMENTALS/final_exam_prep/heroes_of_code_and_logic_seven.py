def add_hero(name, hit_p, mana_p):
    all_heroes_dict[name] = {}
    all_heroes_dict[name]["HP"] = hit_p
    all_heroes_dict[name]["MP"] = mana_p


def cast_spell(name, mana, spell):
    if all_heroes_dict[name]["MP"] >= mana:
        all_heroes_dict[name]["MP"] -= mana
        print(f"{name} has successfully cast {spell} and now has {all_heroes_dict[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")


def take_damage(name, damage_taken, attacker_name):
    all_heroes_dict[name]["HP"] -= damage_taken
    current_hit_points = all_heroes_dict[name]["HP"]
    if all_heroes_dict[name]["HP"] > 0:
        print(f"{name} was hit for {damage_taken} HP by {attacker_name} and now has {current_hit_points} HP left!")
    else:
        print(f"{name} has been killed by {attacker_name}!")
        del all_heroes_dict[name]


def recharge(name, mp_amount):
    increased_amount = all_heroes_dict[name]["MP"] + mp_amount
    if increased_amount > 200:
        difference = 200 - all_heroes_dict[name]["MP"]
        all_heroes_dict[name]["MP"] = 200
        print(f"{name} recharged for {difference} MP!")
    else:
        all_heroes_dict[name]["MP"] = increased_amount
        print(f"{name} recharged for {mp_amount} MP!")


def heal(name, hp_amount):
    increased_amount = all_heroes_dict[name]["HP"] + hp_amount
    if increased_amount > 100:
        difference_heal = 100 - all_heroes_dict[name]["HP"]
        all_heroes_dict[name]["HP"] = 100
        print(f"{name} healed for {difference_heal} HP!")
    else:
        all_heroes_dict[name]["HP"] = increased_amount
        print(f"{name} healed for {hp_amount} HP!")


count_of_heroes = int(input())

all_heroes_dict = {}

for _ in range(count_of_heroes):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hit_points = int(current_hero[1])
    mana_points = int(current_hero[2])
    add_hero(hero_name, hit_points, mana_points)

command = input()
while command != "End":
    current_command = command.split(" - ")
    key_command = current_command[0]
    if key_command == "CastSpell":
        hero_name_cast = current_command[1]
        MP_needed = int(current_command[2])
        spell_name = current_command[3]
        cast_spell(hero_name_cast, MP_needed, spell_name)
    elif key_command == "TakeDamage":
        hero_name_dmg = current_command[1]
        damage = int(current_command[2])
        attacker = current_command[3]
        take_damage(hero_name_dmg, damage, attacker)
    elif key_command == "Recharge":
        hero_name_recharge = current_command[1]
        MP_increased = int(current_command[2])
        recharge(hero_name_recharge, MP_increased)
    elif key_command == "Heal":
        hero_name_heal = current_command[1]
        HP_increased = int(current_command[2])
        heal(hero_name_heal, HP_increased)
    command = input()

for key, value in all_heroes_dict.items():
    print(f"{key}")
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")