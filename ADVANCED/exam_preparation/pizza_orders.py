from collections import deque

orders = deque(map(int, input().split(", ")))
employee_capacity = list(map(int, input().split(", ")))

total_pizzas = 0

while orders and employee_capacity:
    current_order = orders[0]
    current_employee = employee_capacity[-1]

    if current_order <= 0 or current_order > 10:
        orders.popleft()
        continue

    if current_order <= current_employee:
        total_pizzas += current_order
        orders.popleft()
        employee_capacity.pop()

    else:
        total_pizzas += current_employee
        remaining_pizzas = abs(current_employee - current_order)
        orders.popleft()
        employee_capacity.pop()
        orders.appendleft(remaining_pizzas)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employee_capacity:
        print(f"Employees: {', '.join(map(str, employee_capacity))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")

