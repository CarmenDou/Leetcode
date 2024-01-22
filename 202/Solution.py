class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while True:
            m = 0
            while n:
                m += (n%10)**2
                n /= 10
            if m == 1:
                return True
            elif m in dic:
                return False
            else:
                dic[m] = 1
            n = m
        