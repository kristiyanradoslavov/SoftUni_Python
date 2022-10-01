count_of_inputs = int(input())

students_information = {}

for count in range(count_of_inputs):
    student = input()
    grade = float(input())
    if student not in students_information:
        students_information[student] = []
    students_information[student].append(grade)

for item, value in students_information.items():
    average_grade = sum(value) / len(students_information[item])
    if average_grade >= 4.50:
        print(f"{item} -> {average_grade:.2f}")


