class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]
        if n <= 2:
            return fib[n]
        else:
            for i in range(n - 2):
                fib.append(sum(fib))
                fib.pop(0)
        return fib.pop()
