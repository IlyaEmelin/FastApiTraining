from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i, char in enumerate(strs[0]):
            try:
                if all(strs[j][i] == char for j in range(1, len(strs))):
                    result += char
                else:
                    return result
            except IndexError:
                return result
        return result


if __name__ == '__main__':
    # print(Solution().twoSum([2,7,11,15], 9))
    # print(Solution().twoSum([3,3], 6))
    # print(Solution().isPalindrome(10))
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))