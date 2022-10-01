word = input()

vowel_list = ["a", "o", "u", "e", "i"]

vowels_removed = [char for char in word if char.lower() not in vowel_list]

print("".join(vowels_removed))