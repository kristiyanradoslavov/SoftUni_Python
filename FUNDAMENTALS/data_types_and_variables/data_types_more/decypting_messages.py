key_num = int(input())
letters_count = int(input())

final_message = []

for i in range(letters_count):
    current_letter = input()
    current_ascii_amount = ord(current_letter)
    final_letter = current_ascii_amount + key_num
    final_message.append(chr(final_letter))

print("".join(final_message))