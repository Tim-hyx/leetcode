class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 0:
            return []
        else:
            merge = [intervals[0]]
            for i in intervals[1:]:
                # if the current interval does not overlap with the previous, simply append it.
                if i[0] > merge[-1][1]:
                    merge.append(i)
                # otherwise, there is overlap, so we merge the current and previous intervals.
                else:
                    merge[-1][1] = max(merge[-1][1], i[1])
            return merge
