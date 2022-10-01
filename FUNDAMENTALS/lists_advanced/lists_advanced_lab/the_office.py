employees = list(map(int, input().split(" ")))
factor = int(input())

# employees = list(map(lambda a: int(a) * factor, employees)) - how to change the current list

second_list = []
for employ in employees:
    emp = employ * factor
    second_list.append(emp)

average_count = sum(second_list) / len(second_list)

happy_people = [x for x in second_list if x >= average_count]


if len(happy_people) >= (len(second_list) / 2):
    print(f"Score: {len(happy_people)}/{len(second_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(second_list)}. Employees are not happy!")