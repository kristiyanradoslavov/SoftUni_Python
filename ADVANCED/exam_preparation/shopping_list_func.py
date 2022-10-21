def shopping_list(budget, **kwargs):
    if budget < 100:
        return f"You do not have enough budget."

    final_result = []
    basket = 0

    for key, value in kwargs.items():
        price, quantity = float(value[0]), int(value[1])
        total_price = price * quantity

        if total_price <= budget:
            if basket < 5:
                basket += 1
                budget -= total_price
                final_result.append(f"You bought {key} for {total_price:.2f} leva.")
            else:
                break

    return "\n".join(final_result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))





