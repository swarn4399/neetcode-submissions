class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i] - buy
            max_profit = max(max_profit, profit)
            if prices[i] < buy:
                buy = prices[i]
        return max_profit

        