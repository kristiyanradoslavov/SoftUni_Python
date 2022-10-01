needed_exp = float(input())
count_of_battles = int(input())

total_exp_gained = 0
battle_counter = 0


for exp in range(0, count_of_battles):
    earned_exp = float(input())
    battle_counter += 1
    if battle_counter % 3 == 0:
        earned_exp += 15/100 * earned_exp
    if battle_counter % 5 == 0:
        earned_exp -= 10/100 * earned_exp
    if battle_counter % 15 == 0:
        earned_exp -= 5/100 * earned_exp

    total_exp_gained += earned_exp
    if total_exp_gained >= needed_exp:
        break

difference = abs(needed_exp - total_exp_gained)

if total_exp_gained >= needed_exp:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")