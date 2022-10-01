words = input().split(" ")

filtered_words = [i for i in words if len(i) % 2 == 0]


for j in filtered_words:
    print(j)