sentence = input().split(" ")

result = []

for word in sentence:
    final_word = []
    digit = []
    other = []
    for letter in word:
        if letter.isdigit():
            digit.append(letter)
        else:
            other.append(letter)

    digit = ''.join(digit)
    final_word.append(chr(int(digit)))
    if len(other) > 1:
        other[-1] , other[0] = other[0], other[-1]
        other = ''.join(other)
        final_word.append(other)
    else:
        final_word.append(other[0])

    final_word = ''.join(final_word)
    result.append(final_word)

print(' '.join(result))