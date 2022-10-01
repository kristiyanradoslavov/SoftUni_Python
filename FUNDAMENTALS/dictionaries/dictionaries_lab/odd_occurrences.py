courses = input().split(" ")

course_dict = {}


for i in courses:
    word_lower = i.lower()
    if word_lower not in course_dict:
        course_dict[word_lower] = 1
    else:
        course_dict[word_lower] += 1

for key, word in course_dict.items():
    if int(word) % 2 != 0:
        print(key, end=" ")