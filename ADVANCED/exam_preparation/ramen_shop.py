from collections import deque

bowls_of_ramen = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))


while bowls_of_ramen and customers:
    current_ramen = bowls_of_ramen[-1]
    current_customer = customers[0]

    if current_ramen == current_customer:
        bowls_of_ramen.pop()
        customers.popleft()

    elif current_ramen > current_customer:
        bowls_of_ramen[-1] -= current_customer
        customers.popleft()

    elif current_ramen < current_customer:
        customers[0] -= current_ramen
        bowls_of_ramen.pop()


if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")