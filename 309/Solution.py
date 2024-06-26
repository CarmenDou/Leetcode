class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = [-float('inf')] * (len(prices)+2)
        maxProfits[-1], maxProfits[-2], maxProfits[-3] = 0, 0, 0
        for i in range(len(prices)-2, -1, -1):
            tmpMax = - float('inf')
            for j in range(i+1, len(prices)):
                tmpMax = max(tmpMax, prices[j] - prices[i] + maxProfits[j+2])
            maxProfits[i] = max(tmpMax, maxProfits[i+1])

        return maxProfits[0]