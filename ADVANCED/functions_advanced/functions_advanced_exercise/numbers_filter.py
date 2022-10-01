def even_odd_filter(**kwargs):
    all_nums = {}

    for key, value in kwargs.items():
        if key == "odd":
            all_nums[key] = [x for x in value if x % 2 != 0]

        else:
            all_nums[key] = [x for x in value if x % 2 == 0]

    final_result = sorted(all_nums.items(), key= lambda x: -len(x[1]))
    final_dict = {}
    for i in range(len(final_result)):
        final_dict[final_result[i][0]] = final_result[i][1]

    return final_dict


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
