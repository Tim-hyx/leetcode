class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort(reverse=True)
        salary.pop()
        salary.sort()
        salary.pop()
        return sum(salary) / len(salary)
