text = input()

digits = ""
letters = ""
other = ""

for letter in text:
    if letter.isdigit():
        digits += letter
    elif 97 <= ord(letter.lower()) <= 122:
        letters += letter
    # elif letter.isalpha():
    #     letters += letter
    else:
        other += letter

print(digits)
print(letters)
print(other)