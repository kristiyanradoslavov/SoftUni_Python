command = input()

all_products = {}

while command != "buy":
    content = command.split(" ")
    name = content[0]
    price = float(content[1])
    quantity = int(content[2])
    if name not in all_products:
        all_products[name] = {}
        all_products[name]["price"] = price
        all_products[name]["quantity"] = quantity
    else:
        all_products[name]["price"] = price
        all_products[name]["quantity"] += quantity

    command = input()

for key, item in all_products.items():
    result = all_products[key]["price"] * all_products[key]["quantity"]
    print(f"{key} -> {result:.2f}")