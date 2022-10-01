products = input().split(' ')
products_to_search = input().split(' ')

my_dict = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i + 1])
    my_dict[key] = value

for x in products_to_search:
    if x in my_dict:
        print(f"We have {my_dict[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")

