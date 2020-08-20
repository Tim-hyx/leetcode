class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my solution but can't pass last three tests
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                last = 0 - (nums[i] + nums[j])
                if last in nums[j + 1:]:
                    result.append([nums[i], nums[j], last])
        res = []
        check = []
        for x in result:
            if x not in check:
                res.append(x)
                check.append(x)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)
