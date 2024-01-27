class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        table = [0]*(n+3)
        table[0] = 1
        i = 0
        while i <= n:
            if table[i] != 0:
                table[i+1] += table[i]    
                table[i+2] += table[i]
            i += 1
        return table[n]