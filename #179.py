# first method
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# second method
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        cmp = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        largestNumber = ''.join(sorted(nums, key=cmp))
        if largestNumber[0] == '0':
            return '0'
        else:
            return largestNumber
