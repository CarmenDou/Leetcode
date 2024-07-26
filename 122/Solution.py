class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyIndex = 0
        i = 1
        while i < len(prices):
            if prices[i] < prices[i-1]:
                profit += prices[i-1] - prices[buyIndex]
                buyIndex = i
            i += 1
        profit += prices[i-1] - prices[buyIndex]
        return profit