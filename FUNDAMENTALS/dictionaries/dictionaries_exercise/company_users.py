command = input()

all_employee_information = {}

while command != "End":
    current_command = command.split(" -> ")
    company = current_command[0]
    employee_id = current_command[1]
    if company not in all_employee_information:
        all_employee_information[company] = []
    if employee_id not in all_employee_information[company]:
        all_employee_information[company].append(employee_id)

    command = input()

for item, value in all_employee_information.items():
    print(item)
    for employee in value:
        print(f"-- {employee}")
