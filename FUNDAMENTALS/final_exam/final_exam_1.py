def upper_letters(spell):
    result = spell
    result = result.replace(result, result.upper())
    print(result)
    return result


def low_letters(spell):
    result = spell
    result = result.replace(result, result.lower())
    print(result)
    return result


def index_replacement(index, letter):
    result = spell_to_replace
    if 0 <= index < len(spell_to_replace):
        list_result = list(result)
        list_result.pop(index)
        list_result.insert(index, letter)
        result = "".join(list_result)
        print("Done!")
    else:
        print("The spell was too weak.")
    return result


def replace_all(first, second):
    result = spell_to_replace
    if first in result:
        result = result.replace(first, second)
        print(result)
    return result


def delete_substring(first):
    result = spell_to_replace
    if first in result:
        result = result.replace(first, "")
        print(result)
    return result


spell_to_replace = input()

command = input()

while command != "Abracadabra":
    current_command = command.split(" ")
    key_command = current_command[0]
    if key_command =="Abjuration":
        spell_to_replace = upper_letters(spell_to_replace)
    elif key_command == "Necromancy":
        spell_to_replace = low_letters(spell_to_replace)
    elif key_command == "Illusion":
        index_to_replace = int(current_command[1])
        letter_to_replace = current_command[2]
        spell_to_replace = index_replacement(index_to_replace, letter_to_replace)
    elif key_command == "Divination":
        first_substring = current_command[1]
        second_substring = current_command[2]
        spell_to_replace = replace_all(first_substring, second_substring)
    elif key_command == "Alteration":
        string_to_delete = current_command[1]
        spell_to_replace = delete_substring(string_to_delete)
    else:
        print("The spell did not work!")

    command = input()