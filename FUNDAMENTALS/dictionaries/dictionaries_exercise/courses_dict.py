command = input()

all_users = {}
num = 1
while command != "end":
    course_information = command.split(" : ")
    course_name = course_information[0]
    student_name = course_information[1]
    if course_name not in all_users:
        all_users[course_name] = []
    all_users[course_name].append(student_name)
    command = input()

for key, value in all_users.items():
    print(f"{key}: {len(all_users[key])}")
    for i in value:
        print(f"-- {''.join(i)}")
