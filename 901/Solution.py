class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        val = 0
        while self.stack and self.stack[-1][0] <= price:
            val += self.stack[-1][1]
            self.stack.pop()
        val += 1
        self.stack.append([price,val])
        return self.stack[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)