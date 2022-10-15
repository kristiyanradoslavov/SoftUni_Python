def shopping_cart(*args):
    products_dict = {}
    final_result = []
    all_products = ["Soup", "Pizza", "Dessert"]

    for products in args:
        if products == "Stop":
            break
        current_meal = products[0]
        current_product = products[1]

        if current_meal not in products_dict:
            products_dict[current_meal] = []

        if current_meal == "Soup":
            if len(products_dict[current_meal]) < 3:
                if current_product not in products_dict[current_meal]:
                    products_dict[current_meal].append(current_product)
        elif current_meal == "Pizza":
            if len(products_dict[current_meal]) < 4:
                if current_product not in products_dict[current_meal]:
                    products_dict[current_meal].append(current_product)
        elif current_meal == "Dessert":
            if len(products_dict[current_meal]) < 2:
                if current_product not in products_dict[current_meal]:
                    products_dict[current_meal].append(current_product)

    for i in all_products:
        if i not in products_dict:
            products_dict[i] = []

    for j in products_dict:
        if len(products_dict[j]) > 0:
            break
    else:
        return "No products in the cart!"

    sorted_dict = sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, values in sorted_dict:
        final_result.append(f"{key}:\n")
        for value in sorted(values):
            final_result.append(f" - {value}\n")

    return "".join(final_result)[:-1]


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))






















