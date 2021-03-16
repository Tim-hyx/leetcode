class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        count = 0
        res = [[0] * n for i in range(n)]
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        left = 0
        right = n - 1
        up = 0
        down = n - 1
        mark = 0
        x = 0
        y = 0
        while count != n ** 2:
            count += 1
            res[x][y] += count
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
            mark %= 4
            x += move[mark][0]
            y += move[mark][1]
        return res
