names = input().split(", ")

sorted_names = sorted(names, key=lambda a: (-len(a), a))

print(sorted_names)