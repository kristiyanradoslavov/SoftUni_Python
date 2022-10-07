punctuation = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    result = file.readlines()

for i in range(0, len(result), 2):
    for j in range(len(punctuation)):
        if punctuation[j] in result[i]:
            result[i] = result[i].replace(punctuation[j], "@")

    final_result = ("".join(result[i]).split())
    for i in range(len(final_result) - 1, -1, -1):
        print(final_result[i], end=" ")
    print()
