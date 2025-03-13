from math import log10, pow

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        len_x = int(log10(x))
        num, invert_num = 1, int(pow(10, len_x))
        for i in range((len_x + 1) // 2):
            low_num = x % (num * 10) // num
            up_num = x  % (invert_num * 10) // invert_num

            num *= 10
            invert_num //= 10

            if low_num != up_num:
                return False
        return True


if __name__ == '__main__':
    # print(Solution().twoSum([2,7,11,15], 9))
    # print(Solution().twoSum([3,3], 6))
    # print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(1001))
