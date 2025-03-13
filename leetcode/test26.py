from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            if len(nums) >= 2:
                i, j = 0, 1
                while j < len(nums):
                    if nums[i] == nums[j]:
                        j += 1
                    else:
                        i += 1
                        if j != len(nums):
                            nums[i] = nums[j]
                        j += 1

                for k in range(i + 1, len(nums)):
                    nums[k] = '_'

                return i + 1
            else:
                return 1
        return 0


if __name__ == '__main__':
    array = [1,1,2]
    print('test1:', Solution().removeDuplicates(array), array)
    array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print('test2:', Solution().removeDuplicates(array), array)