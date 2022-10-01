count_of_usernames = int(input())

all_usernames = set()

for _ in range(count_of_usernames):
    current_username = input()
    all_usernames.add(current_username)

for user in all_usernames:
    print(user)