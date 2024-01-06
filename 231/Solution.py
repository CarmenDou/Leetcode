class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        #pay attention to the case when n == 0
        if n == 0 :
            return False
        else :
            while n != 1 :
                if n % 2 != 0 :
                    return False
                n = n / 2
            return True

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 :
            return False
        elif (n-1) & n == 0 :
            return True
        else :
            return False

# Leetcode
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n&(n-1))==0