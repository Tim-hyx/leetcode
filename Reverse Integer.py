class Solution:
    def reverse(self, x: int) -> int:
        if 2 ** 31 * (-1) <= x <= 2 ** 31 - 1:
            strg = str(x)
            if x < 0:
                a = abs(x)
                strg = str(a)
                revst = '-' + strg[::-1]
            else:
                revst = strg[::-1]
            if int(revst) >= 2 ** 31 - 1 or int(revst) <= 2 ** 31 * (-1):
                return 0
            return int(revst)
        else:
            return 0
