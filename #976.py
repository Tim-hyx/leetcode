class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        sum_list = [A[i] + A[i + 1] + A[i + 2] for i in range(len(A) - 2) if A[i] + A[i + 1] > A[i + 2]]
        if len(sum_list) == 0:
            return 0
        else:
            return max(sum_list)
