class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dirt = {}
        for i in range(len(nums)):
            if nums[i] not in dirt:
                dirt[nums[i]] = i
            else:
                if abs(dirt[nums[i]] - i) <= k:
                    return True
                else:
                    dirt[nums[i]] = i
        return False
