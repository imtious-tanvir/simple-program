def two_sum(number_list, target):
    seen_values = {}
    for index, number in enumerate(number_list):
        compare = target - number
        if compare in seen_values:
            return [seen_values[compare], index]
        seen_values[number] = index
    raise ValueError("No two sum solution")


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))
