def loading_bar(percent):
    first_list = ['.', '.', '.', '.','.', '.', '.', '.','.', '.']
    current_index = 0
    for num in range(0, percent, 10):
        first_list.pop(current_index)
        first_list.insert(current_index, "%")
        current_index += 1
    second_list = "".join(first_list)
    if percent < 100:
        print(f"{percent}% [{second_list}]")
        print("Still loading...")
    else:
        print(f"{percent}% Complete!")
        print(f"[{second_list}]")


percent = int(input())
loading_bar(percent)
