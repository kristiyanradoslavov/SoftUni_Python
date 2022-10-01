countries = input().split(", ")
capitals = input().split(", ")


countries_dict = {x: y for x, y in zip(countries, capitals)}

for key, value in countries_dict.items():
    print(f"{key} -> {value}")