class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))):
            return True
        else:
            return False
