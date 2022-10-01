characters = input().split(", ")

final_dict = {characters[i]: ord(characters[i]) for i in range(0, len(characters))}

print(final_dict)
