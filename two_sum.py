class Solution:
    def two_sum(self, number_list, target):

        seen_values = {}
        for index, number in enumerate(number_list):
            compare = target - number
            if compare in seen_values:
                return [seen_values[compare], index]
            seen_values[number] = index
        raise ValueError("No two sum solution")


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().two_sum(nums, target))
