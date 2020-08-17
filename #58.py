class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            s = list(s.split())
            if len(s) == 0:
                return 0
            return len(s[-1])
