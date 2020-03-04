class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            a=str(x)
            b=a[::-1]
            if b==a:
                return a
