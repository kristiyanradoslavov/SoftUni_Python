def even_odd(*args):
    even_nums = []
    odd_nums = []
    command = args[-1]
    for i in range(0, len(args) - 1):
        if args[i] % 2 == 0:
            even_nums.append(args[i])
        else:
            odd_nums.append(args[i])
    if command == "even":
        return even_nums
    elif command == "odd":
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
