class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        M = len(matrix)
        N = len(matrix[0])
        res = []
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        left = 0
        right = N - 1
        up = 0
        down = M - 1
        mark = 0
        x = 0
        y = 0
        while len(res) != M * N:
            if mark == 0 and y == right:
                mark += 1
                up += 1
            if mark == 1 and x == down:
                mark += 1
                right -= 1
            if mark == 2 and y == left:
                mark += 1
                down -= 1
            if mark == 3 and x == up:
                mark += 1
                left += 1
            res.append(matrix[x][y])
            mark %= 4
            x += move[mark][0]
            y += move[mark][1]
        return res
