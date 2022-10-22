from collections import deque

milligrams_of_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_caffeine = milligrams_of_caffeine[-1]
    current_drink = energy_drinks[0]
    result = current_caffeine * current_drink

    if (total_caffeine + result) <= 300:
        milligrams_of_caffeine.pop()
        energy_drinks.popleft()
        total_caffeine += result

    else:
        milligrams_of_caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())

        if (total_caffeine - 30) > 0:
            total_caffeine -= 30
        else:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")


