command = input()

total_price_without_tx = 0

while command != "special" and command != "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price_without_tx += price
    command = input()

taxes = 20/100 * total_price_without_tx

total_price = total_price_without_tx + taxes

if command == "special":
    total_price -= 10/100 * total_price

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_tx:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
