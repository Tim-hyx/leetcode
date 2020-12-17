class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0
        for i in range(1, len(prices)):
            cash = max(cash, prices[i] + hold - fee)
            hold = max(hold, cash - prices[i])
        return cash
