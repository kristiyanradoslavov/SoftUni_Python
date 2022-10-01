from collections import deque
all_customers = deque()
command = input()

while command != "End":
    if command == "Paid":
        for _ in range(len(all_customers)):
            print(all_customers.popleft())
        command = input()
        continue

    current_customer = command
    all_customers.append(current_customer)
    command = input()

if all_customers:
    print(f"{len(all_customers)} people remaining.")
else:
    print("0 people remaining.")