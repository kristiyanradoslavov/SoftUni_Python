items_to_buy = input().split("|")
budget = float(input())
starting_budget = budget

bought_items = []

for current_item in items_to_buy:
    split_item = current_item.split("->")
    type_to_buy = split_item[0]
    price = float(split_item[1])
    if type_to_buy == "Clothes" and price <= 50 and budget >= price:
        budget -= price
        clothes_price = f"{price + (price * 0.4):.2f}"
        bought_items.append(clothes_price)
    elif type_to_buy == "Shoes" and price <= 35 and budget >= price:
        budget -= price
        shoes_price = f"{price + (price * 0.4):.2f}"
        bought_items.append(shoes_price)
    elif type_to_buy == "Accessories" and price <= 20.5 and budget >= price:
        budget -= price
        accessories_price = f"{price + (price * 0.4):.2f}"
        bought_items.append(accessories_price)

result = sum(map(float, bought_items)) + budget
profit = result - starting_budget

print(" ".join(map(str, bought_items)))
print(f"Profit: {profit:.2f}")

if result >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")