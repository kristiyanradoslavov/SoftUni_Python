import sys
from collections import deque


def change_time(seconds, minutes, hours):
    final_seconds = seconds
    final_minutes = minutes
    final_hours = hours
    final_seconds += 1
    if final_seconds >= 60:
        final_seconds = 00
        final_minutes += 1
        if final_minutes >= 60:
            final_minutes = 00
            final_hours += 1
            if final_hours >= 24:
                final_seconds = 00
                final_minutes = 00
                final_hours = 00
    return final_seconds, final_minutes, final_hours


robot_information = input().split(";")
hours, minutes, seconds = list(map(int, input().split(":")))

current_hour = hours
current_minute = minutes
current_second = seconds

robot_information_dict = {}

for robot in robot_information:
    name, time = robot.split("-")
    robot_information_dict[name] = {}
    robot_information_dict[name]["Time"] = float(time)
    robot_information_dict[name]["Status"] = True

assembly_line_queue = deque()

current_command = input()

while current_command != "End":
    product = current_command
    product_is_assigned = False
    current_second, current_minute, current_hour = change_time(current_second, current_minute, current_hour)
    for current_robot in robot_information_dict:
        if robot_information_dict[current_robot]["Status"] is True:
            product_is_assigned = True
            robot_information_dict[current_robot]["Status"] = False
            print(f"{current_robot} - {product} [{current_hour}:{current_minute}:{current_second}]")
            break

        else:
            continue
    if not product_is_assigned:
        assembly_line_queue.append(product)
        lowest_time = sys.maxsize
        for i in robot_information_dict:
            if robot_information_dict[i]["Time"] < lowest_time:
                lowest_time = robot_information_dict[i]["Time"]

    current_command = input()
