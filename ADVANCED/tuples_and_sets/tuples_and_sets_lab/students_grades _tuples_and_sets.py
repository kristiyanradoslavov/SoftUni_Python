count_of_students = int(input())

students_dict = {}

for i in range(count_of_students):
    student, grade = input().split()
    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(float(grade))


for key, value in students_dict.items():
    average_grade = sum(value) / len(value)
    all_grades = ' '.join(str(f'{change:.2f}') for change in value)
    print(f"{key} -> {all_grades} (avg: {average_grade:.2f})")
