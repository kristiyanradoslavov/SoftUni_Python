from collections import deque


def check_colors(first, second):
    f_string = first + second
    s_string = second + first
    if f_string == "red" or f_string == "yellow" or f_string == "blue" \
            or f_string == "orange" or f_string == "purple" or f_string == "green":
        colors_found.append(f_string)
        if first_half:
            first_half.popleft()
        if second_half:
            second_half.pop()
    elif s_string == "red" or s_string == "yellow" or s_string == "blue" \
            or s_string == "orange" or s_string == "purple" or s_string == "green":
        colors_found.append(s_string)
        if first_half:
            first_half.popleft()
        if second_half:
            second_half.pop()
    else:
        if first_half:
            first_string = first_half.popleft()
            first_string = first_string[:-1]
            if first_string:
                first_half.append(first_string)
        if second_half:
            second_string = second_half.pop()
            second_string = second_string[:-1]
            if second_string:
                second_half.appendleft(second_string)


def split_input():
    first_half.clear()
    second_half.clear()
    if len(string_with_colors) % 2 == 0:
        for i in range(len(string_with_colors)):
            if i >= len(string_with_colors) // 2:
                second_half.append(string_with_colors[i])
            else:
                first_half.append(string_with_colors[i])
    else:
        for j in range(len(string_with_colors)):
            if j >= len(string_with_colors) // 2:
                second_half.append(string_with_colors[j])
            else:
                first_half.append(string_with_colors[j])


string_with_colors = input().lower().split()
first_half = deque()
second_half = deque()

colors_found = []

while string_with_colors:
    if len(string_with_colors) > 1:
        split_input()
        first_substring = first_half[0]
        second_substring = second_half[-1]
        check_colors(first_substring, second_substring)
        string_with_colors = first_half + second_half

    else:
        final_substring = string_with_colors[0]
        dummy = ""
        check_colors(final_substring, dummy)
        string_with_colors.pop()

final_list = []
for color in colors_found:
    if color == "orange":
        if "red" in colors_found:
            if "yellow" in colors_found:
                final_list.append(color)
    elif color == "purple":
        if "red" in colors_found:
            if "blue" in colors_found:
                final_list.append(color)
    elif color == "green":
        if "yellow" in colors_found:
            if "blue" in colors_found:
                final_list.append(color)
    else:
        final_list.append(color)

print(final_list)
