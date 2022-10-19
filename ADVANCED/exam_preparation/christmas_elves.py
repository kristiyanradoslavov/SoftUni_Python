from collections import deque

energy = deque(map(int, input().split()))
materials = list(map(int, input().split()))

total_energy = 0
total_toys = 0

turn_counter = 1
cookie = 1

while energy and materials:
    current_energy = energy[0]
    current_material = materials[-1]
    hot_chocolate = current_energy

    if current_energy < 5:
        energy.popleft()
        continue

    if turn_counter % 3 == 0:
        if current_energy >= current_material * 2:
            materials.pop()
            energy.popleft()
            total_toys += 2
            total_energy += current_material * 2
            if turn_counter % 5 == 0:
                total_toys -= 2
                current_energy = current_energy - current_material * 2
                energy.append(current_energy)
            else:
                current_energy = (current_energy - current_material * 2) + cookie
                energy.append(current_energy)

        else:
            energy.popleft()
            current_energy = current_energy + hot_chocolate
            energy.append(current_energy)

    elif turn_counter % 5 == 0:
        if current_energy >= current_material:
            materials.pop()
            energy.popleft()
            total_energy += current_material
            current_energy -= current_material
            energy.append(current_energy)

        else:
            energy.popleft()
            current_energy = current_energy + hot_chocolate
            energy.append(current_energy)

    if turn_counter % 3 != 0 and turn_counter % 5 != 0:
        if current_energy >= current_material:
            materials.pop()
            energy.popleft()
            total_toys += 1
            total_energy += current_material
            current_energy = current_energy - current_material + cookie
            energy.append(current_energy)

        else:
            energy.popleft()
            current_energy = current_energy + hot_chocolate
            energy.append(current_energy)
    turn_counter += 1

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if energy:
    print(f"Elves left: {(', '.join(map(str, energy)))}")

if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
