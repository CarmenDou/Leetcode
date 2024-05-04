class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(n):
            return n > 1 and all(n%i for i in range(2,int(n**0.5)+1))

        for i in range(1,6):
            for m in range(10**(i-1), 10**i):
                m = str(m)
                x = int(m+m[-2::-1])
                if x >= n and isPrime(x):
                    return x
        
            for m in range(10**(i-1), 10**i):
                m = str(m)
                x = int(m+m[-1::-1])
                if x >= n and isPrime(x):
                    return x