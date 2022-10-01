products = input().split(" ")

dictionary_final = {}

for dictionary in range(0, len(products), 2):
    key = products[dictionary]
    element = products[dictionary + 1]
    dictionary_final[key] = int(element)

print(dictionary_final)