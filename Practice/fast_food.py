from collections import deque

food_quantity = int(input())

food_orders = deque(map(int, input().split()))
orders_copy = food_orders.copy()

biggest_order = max(food_orders)
print(biggest_order)

for i in range(len(food_orders)):
    if food_quantity - food_orders[i] >= 0:
        food_quantity -= food_orders[i]
        orders_copy.popleft()
    else:
        print(f"Orders left: {' '.join(map(str, orders_copy))}")
        break
else:
    print("Orders complete")


