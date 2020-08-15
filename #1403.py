class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        return_list = []
        if len(nums) == 1 or len(nums) == 0:
            return nums
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                return_list.append(max(nums))
                return return_list
            else:
                return nums
        else:
            nums = sorted(nums, reverse=True)
            for i in range(len(nums)):
                return_list.append(nums[i])
                if sum(nums[i + 1:]) < sum(return_list):
                    break
        return return_list
