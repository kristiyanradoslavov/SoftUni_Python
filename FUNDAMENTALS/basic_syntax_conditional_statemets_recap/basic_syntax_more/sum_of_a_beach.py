word = input().lower()

word = word.replace("water", "1")
word = word.replace("fish", "1")
word = word.replace("sun", "1")
word = word.replace("sand", "1")

counter = 0

for i in word:
    if i.isdigit():
        counter += 1

print(counter)