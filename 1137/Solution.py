class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1 or n == 2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        if n == 0 :
            return 0
        elif n== 1 or n == 2:
            return 1
        else:
            dq = deque([0,1,1],3)
            i = 3
            while i <= n:
                dq.append(dq[0]+dq[1]+dq[2])
                i += 1
            return dq[-1]
