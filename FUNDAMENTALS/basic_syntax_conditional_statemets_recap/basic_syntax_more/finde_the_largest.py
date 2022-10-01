string = input()

result = sorted(string)
pre_final = "".join(result)
final_result = pre_final[-1::-1]

print(final_result)