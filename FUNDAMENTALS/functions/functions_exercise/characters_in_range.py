def characters(start, end):
    final_list = []
    for char in range(ord(start) + 1, ord(end)):
        character = chr(char)
        final_list.append(character)
    result = " ".join(final_list)
    return result


first_input = input()
second_input = input()

print(characters(first_input, second_input))
