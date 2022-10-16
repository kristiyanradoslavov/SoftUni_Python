def words_sorting(*args):
    words_dict = {}
    for word in args:
        current_word_value = 0
        for j in range(len(word)):
            current_word_value += ord(word[j])
        words_dict[word] = current_word_value

    value_sum = sum(words_dict.values())
    sorted_dict = None
    if value_sum % 2 == 0:
        sorted_dict = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_dict = sorted(words_dict.items(), key= lambda x: -x[1])
    final_result = []

    for key, value in sorted_dict:
        final_result.append(f"{key} - {value}\n")

    return "".join(final_result)[:-1]


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

