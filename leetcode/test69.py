class Solution:
    def mySqrt(self, x: int) -> int:
        start, stop, average, result = 0, x, 1, 1
        while start <= stop:
            average = (start + stop) // 2
            result = average * average

            if result < x:
                start = average + 1
            elif x < result:
                stop = average - 1
            else:
                return average

        if result <= x:
            return average
        return average - 1


if __name__ == '__main__':
    print('test1:', Solution().mySqrt(1), 1)