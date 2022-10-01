note = input()
note_list = [0] * 10

while note != "End":
    current_list = note.split("-")
    priority = int(current_list[0]) - 1
    note_info = current_list[1]
    note_list.pop(priority)
    note_list.insert(priority, note_info)
    note = input()

final_list = [zero for zero in note_list if zero != 0]

print(final_list)