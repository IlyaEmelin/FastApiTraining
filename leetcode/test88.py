from typing import List
from collections import deque


class Solution:

    @staticmethod
    def __get_num2(deque2, nums2, j):
        try:
            num2 = deque2.pop()
        except IndexError:
            try:
                num2 = nums2[j]
                j += 1
            except IndexError:
                return None, j
        return num2, j

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, n + m - 1
        while i >= 0 and j >= 0:
            num1, num2 = nums1[i], nums2[j]
            if num1 < num2:
                nums1[k] = num2
                j -= 1
                k -= 1
            else:
                nums1[k] = num1
                i -= 1
                k -= 1

        while k >= 0 and j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



if __name__ == '__main__':
    # nums1 = [4,5,6,0,0,0]
    # Solution().merge(
    #     nums1,
    #     3,
    #     [1,2,3],
    #     3
    # )
    # print(
    #     'test1:',
    #     nums1
    # )
    nums1 = [1,2,3,0,0,0]
    Solution().merge(
        nums1,
        3,
        [2,5,6],
        3
    )
    print(
        'test2:',
        nums1
    )