def fill_the_box(height, length, width, *args):
    v = height * length * width
    count_of_cubes = 0
    cubes_left = 0
    for j in range(len(args) - 1):
        if args[j] == "Finish":
            break
        cubes_left += args[j]

    for i in args:
        if i == "Finish":
            break
        if v > 0:
            v -= i
            count_of_cubes += i
            cubes_left -= i

        elif v < 0:
            break

    if v > 0:
        return f"There is free space in the box. You could put {v} more cubes."
    elif v < 0:
        return f"No more free space! You have {cubes_left - v} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
