from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_nums = {}
        for num in nums:
            average_value = num * 2 - target

            grope_num = find_nums.get(abs(average_value)) or []
            if average_value > 0:
                grope_num.append(num)
            else:
                grope_num.insert(0, num)

            len_num = len(grope_num)
            if len_num >= 2:
                first_num, last_num = grope_num[0], grope_num[len_num - 1]
                if first_num < last_num:
                    return [nums.index(first_num), nums.index(last_num)]
                elif first_num == last_num and first_num + last_num == target:
                    first_index = nums.index(first_num)
                    return [first_index, nums.index(first_num, first_index + 1)]
            else:
                find_nums[abs(average_value)] = grope_num



if __name__ == '__main__':
    # print(Solution().twoSum([2,7,11,15], 9))
    # print(Solution().twoSum([3,3], 6))
    print(Solution().twoSum([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11))