class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return []
        else:
            A.sort(key=lambda x: x % 2)
            B = A[int(len(A) / 2):]
            A = A[:int(len(A) / 2)]
            for i in range(len(B)):
                A.insert(2 * i + 1, B[i])
            return A
