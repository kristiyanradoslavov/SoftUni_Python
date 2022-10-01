order = input()
quantity = int(input())


def order_price(first, second):
    final_price = 0
    if first == "coffee":
        final_price = 1.50 * second
    elif first == "coke":
        final_price = 1.40 * second
    elif first == "water":
        final_price = 1.00 * second
    elif first == "snacks":
        final_price = 2.00 * second

    return final_price


print(f"{order_price(order, quantity):.2f}")
