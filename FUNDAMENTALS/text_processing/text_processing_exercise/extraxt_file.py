file_info = input().split('\\')
information = file_info[-1]

final_info = information.split(".")

print(f"File name: {final_info[0]}")
print(f"File extension: {final_info[1]}")
