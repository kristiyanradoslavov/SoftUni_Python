employee_one_can_help = int(input())
employee_two_can_help = int(input())
employee_three_can_help = int(input())
count_of_students = int(input())

total_answered_per_hour = employee_one_can_help + employee_two_can_help + employee_three_can_help
total_hours = 1


while count_of_students > 0:
    if total_hours % 4 == 0:
        total_hours += 1
        continue
    if count_of_students >= total_answered_per_hour:
        count_of_students -= total_answered_per_hour
        total_hours += 1
    else:
        count_of_students -= count_of_students
        total_hours += 1

total_hours -= 1
print(f"Time needed: {total_hours}h.")