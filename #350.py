from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        output = []
        for num in nums2:
            if count[num] > 0:
                output.append(num)
                count[num] -= 1
        return output
