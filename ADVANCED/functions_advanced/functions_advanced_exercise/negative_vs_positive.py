def numbers(*args):
    negative_nums = 0
    positive_nums = 0
    for i in args:
        if int(i) > 0:
            positive_nums += i
        else:
            negative_nums += i

    if abs(negative_nums) > abs(positive_nums):
        print(negative_nums)
        print(positive_nums)
        return "The negatives are stronger than the positives"
    else:
        print(negative_nums)
        print(positive_nums)
        return "The positives are stronger than the negatives"


all_nums = [int(x) for x in input().split()]

print(numbers(*all_nums))
