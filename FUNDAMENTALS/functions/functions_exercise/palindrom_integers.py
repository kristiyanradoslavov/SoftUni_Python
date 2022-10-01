def check(list_of_numbers):
    for i in range(0, len(list_of_numbers)):
        current_num = list_of_numbers[i]
        num = []
        for j in range(len(current_num) -1, -1, -1):
            num.append(current_num[j])
        my_num = "".join(num)
        if my_num == current_num:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
check(numbers)
