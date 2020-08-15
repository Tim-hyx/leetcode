class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        return_str = ''
        while s:
            for i in sorted(set(s)):
                return_str += i
                s.remove(i)
            for j in sorted(set(s), reverse=True):
                return_str += j
                s.remove(j)
        return return_str
