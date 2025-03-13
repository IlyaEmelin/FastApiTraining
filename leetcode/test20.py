class Solution:
    CHAR_DICT = {')': '(', ']': '[', '}': '{'}

    def __is_open_type(self, char):
        return char in self.CHAR_DICT.values()

    def isValid(self, s: str) -> bool:
        i, depth_group = 0, []
        for char in s:
            if self.__is_open_type(char):
                depth_group.append(char)
                i += 1
            else:
                i -= 1
                if i < 0:
                    return False
                select_char = depth_group.pop(i)
                if select_char != self.CHAR_DICT[char]:
                    return False
        return not depth_group


if __name__ == '__main__':
    print('()', Solution().isValid('()'))
    print('()[]{}', Solution().isValid('()[]{}'))
    print('(]', Solution().isValid('(]'))
    print('([])', Solution().isValid('([])'))