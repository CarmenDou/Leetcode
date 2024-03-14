class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n == 1:
            return n
        
        count=[0]*(n+1)
        for i,j in trust:
            count[i]-=1
            count[j]+=1
        
        for i in range(0,len(count)):
            if count[i]==n-1:
                return i
        
        return -1
        