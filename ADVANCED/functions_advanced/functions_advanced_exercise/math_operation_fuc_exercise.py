def math_operations(*args, **kwargs):
    def check(current_idx):
        if current_idx < len(args):
            return True
        else:
            return False

    for i in range(0, len(args), 4):
        if check(i):
            kwargs["a"] += args[i]
        if check(i + 1):
            kwargs["s"] -= args[i + 1]
        if check(i + 2):
            if args[i + 2] == 0:
                pass
            else:
                kwargs["d"] = kwargs["d"] / args[i + 2]

        if check(i + 3):
            kwargs["m"] *= args[i + 3]

    final_result = ""
    sorted_dict = sorted(kwargs.items(), key=lambda x: ((-x[1]), (x[0])))

    for k in range(len(sorted_dict)):
        for l in range(len(sorted_dict[k])):
            if l == len(sorted_dict[k]) - 1:
                final_result += f"{sorted_dict[k][l]:.1f}\n"
            else:
                final_result += f"{sorted_dict[k][l]}: "

    return final_result[:-1]


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
