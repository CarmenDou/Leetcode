#Leetcode
#贪心算法
#use two variables, one for minimum price before judging position, one for maximum profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for x in range(1,len(prices)) :
            if prices[x] < minPrice :
                minPrice = prices[x]
                continue
            if prices[x] - minPrice > maxProfit :
                maxProfit = prices[x] - minPrice
        return maxProfit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = prices[0]
        maxProfit = max - min
        for price in prices :
            if price < min :
                min = price
                max = price
            elif price > max :
                max = price
            if maxProfit < max - min :
                maxProfit = max - min

        return maxProfit
        

        