class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, end = 0, len(s) - 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                end = i
                break

        for i in range(end, -1, -1):
            if s[i] == ' ':
                break
            else:
                length += 1
        return length


if __name__ == '__main__':
    print('test1:', Solution().lengthOfLastWord('a'))