class Solution(object):
    def countBit(self,n) :
        count = 0
        while n != 0 :
            n &= (n-1)
            count += 1
        return count

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        return self.countBit(n)
        