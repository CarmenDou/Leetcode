class Solution(object):
    def countSetBits(self,n):
        count = 0
        while n != 0 :
            n = n & (n-1)
            count += 1
        return count

    def isPrime(self,n):
        if n == 0 or n == 1 :
            return False
        else :
            for x in range(2,n) :
                if n % x == 0 :
                    return False
            return True

    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        iCountPrimeSetBits = 0
        for x in range(left,right+1) :
            iSetBits = self.countSetBits(x)
            if self.isPrime(iSetBits) :
                iCountPrimeSetBits += 1
        return iCountPrimeSetBits
        