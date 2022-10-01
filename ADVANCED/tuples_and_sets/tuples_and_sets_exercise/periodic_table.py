count_of_elements = int(input())

unique_elements = set()

for _ in range(count_of_elements):
    current_input = input().split()
    for current in current_input:
        unique_elements.add(current)

for unique in unique_elements:
    print(unique)