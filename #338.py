class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            binary = bin(i).replace('0b','')
            num1 = binary.count('1')
            res.append(num1)
        return res
        
# 不用内置函数
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            x = 0
            while i > 0:
                i &= i - 1
                x += 1
            res.append(x)
        return res
