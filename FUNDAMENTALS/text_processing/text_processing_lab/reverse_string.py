command = input()

while command != "end":
    current_word = command
    final_word = current_word[::-1]
    print(f"{current_word} = {final_word}")
    command = input()

