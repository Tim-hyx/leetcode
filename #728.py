class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            string = str(i)
            re = 0
            for j in range(len(string)):
                if string[j] != '0':
                    if i % int(string[j]) == 0:
                        re += 1
            if re == len(string):
                res.append(i)
        return res
