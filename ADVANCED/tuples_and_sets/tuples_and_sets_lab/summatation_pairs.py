all_numbers = list(map(int, input().split()))
target_number = int(input())

found_pair = set()

iterations_counter = 0

for num in range(0, len(all_numbers) - 1):
    for second_num in range(num + 1, len(all_numbers)):
        iterations_counter += 1
        if all_numbers[num] + all_numbers[second_num] == target_number:
            print(f"{all_numbers[num]} + {all_numbers[second_num]} = {target_number}")
            found_pair.add((all_numbers[num], all_numbers[second_num]))

print(f"Iterations done: {iterations_counter}")

for pair in found_pair:
    print(pair)