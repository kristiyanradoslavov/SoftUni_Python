command = input()

my_dict = {}

while command != "statistics":
    current_command = command.split(": ")
    key = current_command[0]
    value = int(current_command[1])
    if key in my_dict:
        my_dict[key] += value
    else:
        my_dict[key] = value

    command = input()

print("Products in stock:")
for products, items in my_dict.items():
    print(f"- {products}: {items}")

print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
