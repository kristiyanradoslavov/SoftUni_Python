list_of_palindromes = input().split(" ")
palindrome = input()

final_list = []
for list_check in list_of_palindromes:
    current_word = []
    for word_check in range(len(list_check) -1, -1, -1):
        current_word.append(list_check[word_check])
    final_word = "".join(current_word)
    if final_word == list_check:
        final_list.append(final_word)

counter = 0
for check in list_of_palindromes:
    if palindrome == check:
        counter += 1

print(final_list)
print(f"Found palindrome {counter} times")