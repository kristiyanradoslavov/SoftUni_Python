numbers = input().split(", ")

nums = [num for num in range(0, len(numbers)) if int(numbers[num]) % 2 == 0]

print(nums)