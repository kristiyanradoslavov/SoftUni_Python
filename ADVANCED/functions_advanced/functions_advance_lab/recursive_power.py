def recursive_power(x, y):
    result = 1
    if y == 0:
        return result
    result = x * recursive_power(x, y - 1)
    return result


print(recursive_power(2, 10))

# 2 na 10 stepen
#
# 2 ^ 2 = 2 * 2
# 2* 3 = 4 * 2
# 2 *8 = 16
# 2 *16 = 32

