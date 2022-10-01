initial_energy = int(input())
command = input()

total_won_battles = 0
energy_left = initial_energy

while command != "End of battle":
    current_command = int(command)
    if current_command <= energy_left:
        total_won_battles += 1
        energy_left -= current_command
        if total_won_battles % 3 == 0:
            energy_left += total_won_battles
    else:
        print(f"Not enough energy! Game ends with {total_won_battles} won battles and {energy_left} energy")
        break

    command = input()

if command == "End of battle":
    print(f"Won battles: {total_won_battles}. Energy left: {energy_left}")
