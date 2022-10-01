import re

destinations = input()
pattern = r"([\/|=])([A-Z{1}][A-Za-z]{2,})\1"

valid_destinations = re.findall(pattern, destinations)
result = []
total_length = 0

if valid_destinations:
    for i in valid_destinations:
        result.append(i[1])

    print(f'Destinations: {", ".join(result)}')
    for j in result:
        total_length += len(j)

else:
    print(f'Destinations:')

print(f"Travel Points: {total_length}")
