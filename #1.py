class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        length=len(nums)
        for i in range(length):
            dict[nums[i]]=i
        for i in range(length):
            a=target-nums[i]
            if a in nums and dict.get(a)!=i:
                return [i,dict.get(a)]
