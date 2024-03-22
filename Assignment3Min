class Solution:
    def isUgly(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # arr = [1]
        # while True:
        #     tmp = []
        #     while arr:
        #         i = arr.pop()
        #         if i*2 not in tmp: 
        #             tmp.append(i*2)
        #         if i*3 not in tmp:
        #             tmp.append(i*3)
        #         if i*5 not in tmp:
        #             tmp.append(i*5)
        #     tmp = sorted(tmp)
        #     if n in tmp:
        #         return True
        #     if tmp[0] > n:
        #         return False
        #     arr = tmp

        if n<=0:
            return False
        for x in[2,3,5]:
            while n%x==0:
                n=n/x
                
        return n==1