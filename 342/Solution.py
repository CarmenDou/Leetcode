class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = bin(n)[2:]
        count0 = m.count("0")
        return (count0 % 2 == 0) and (n&(n-1) == 0) and (n > 0)

#Leetcode
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num>0 and (num&(num-1))==0 and (num&0b01010101010101010101010101010101==num))