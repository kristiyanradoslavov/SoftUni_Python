import re

command = input()
furniture_list = []
total_money_spent = 0

while command != "Purchase":
    current_furniture_information = command
    reg_pattern = r">>([A-z]+)<<([\d]+|[\d\.\d]+)\!(\d+)"
    reg_result = re.search(reg_pattern, current_furniture_information)
    if reg_result:
        furniture, price, quantity = reg_result.groups()
        purchase_price = float(price) * int(quantity)
        total_money_spent += purchase_price
        furniture_list.append(furniture)

    command = input()

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_money_spent:.2f}")