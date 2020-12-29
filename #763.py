class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i, j in enumerate(S):
            last[ord(j) - ord('a')] = i  # 找到每个字母的最后位置
        res = []
        start = end = 0
        for i, j in enumerate(S):
            end = max(end, last[ord(j) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1  # 寻找下一个片段
        return res
