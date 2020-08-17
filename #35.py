class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target > max(nums):
                return len(nums)
            if target < min(nums):
                return 0
            for i in range(len(nums) - 1):
                if nums[i] < target < nums[i + 1]:
                    return i + 1
