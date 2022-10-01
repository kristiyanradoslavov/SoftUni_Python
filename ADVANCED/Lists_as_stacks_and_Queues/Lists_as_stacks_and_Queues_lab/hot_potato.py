from collections import deque

all_kids = deque(input().split())
execute_toss = int(input())

count_of_kids = len(all_kids)
toss_counter = 0

while len(all_kids) > 1:
    toss_counter += 1
    if toss_counter == execute_toss:
        current_kid = all_kids.popleft()
        toss_counter = 0
        print(f"Removed {current_kid}")
    else:
        current_kid = all_kids.popleft()
        all_kids.append(current_kid)


print(f'Last is {"".join(all_kids)}')
