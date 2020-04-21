class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        test = 0
        for i in s[::-1]:
            if values[i] >= test:
                number += values[i]
            else:
                number -= values[i]
            test = values[i]
        return number
