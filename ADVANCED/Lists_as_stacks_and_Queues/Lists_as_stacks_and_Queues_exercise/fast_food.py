from collections import deque

quantity_of_food = int(input())
food_ordered = deque(map(int, input().split(" ")))
copy_of_food = food_ordered.copy()

max_num = max(food_ordered)
print(max_num)

while food_ordered:
    food_finished = False
    for current_order in copy_of_food:
        if quantity_of_food >= current_order:
            food_ordered.popleft()
            quantity_of_food -= current_order
        else:
            food_finished = True
            break
    if food_finished:
        break

if food_ordered:
    print(f"Orders left: ",end="")
    for food_remaining in food_ordered:
        print(f"{food_remaining}", end=" ")

else:
    print("Orders complete")