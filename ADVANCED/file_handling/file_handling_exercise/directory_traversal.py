import os
import re

# The input should be .\files_traversal_task - because I have created all the files in that folder
# If the input is just . it will work again, but it will show the files in the current folder.
directory = input()

file_dictionary = {}

for i in os.listdir(directory):
    file = os.path.join(directory, i)

    if os.path.isfile(file):
        current_result = re.split('\\\\', file)
        file_name = current_result[-1]
        file_extension = file_name.split(".")[-1]

        if file_extension not in file_dictionary:
            file_dictionary[file_extension] = []
        file_dictionary[file_extension].append(file_name)

sorted_dict = sorted(file_dictionary.items(), key= lambda x: x)

final_result = ""
for key, value in sorted_dict:
    final_result += f".{key}\n"
    for i in sorted(value):
        final_result += f"- - - {i}\n"

with open("report.txt", "w") as new_file:
    new_file.write(final_result)
