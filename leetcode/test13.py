class Solution:
    ROMAN_NUMERALS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    SUBTRACTION = {
        ('I', 'V'): 4,
        ('I', 'X'): 9,
        ('X', 'L'): 40,
        ('X', 'C'): 90,
        ('C', 'D'): 400,
        ('C', 'M'): 900
    }

    def romanToInt(self, s: str) -> int:
        i, len_s, result = 0, len(s), 0
        while i < len_s:
            num, next_num = s[i], s[i + 1] if i + 1 < len_s else None

            sub_num = self.SUBTRACTION.get((num, next_num))
            if sub_num is not None:
                result += sub_num
                i += 1
            else:
                result += self.ROMAN_NUMERALS.get(num)
            i += 1
        return result
