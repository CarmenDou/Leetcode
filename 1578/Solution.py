class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r, res = 0, 0, 0
        sumTime, maxTime = neededTime[0], neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                r = i
                sumTime += neededTime[i]
                maxTime = max(maxTime, neededTime[i])
            else:
                if r > l:
                    res += (sumTime-maxTime)
                l, r = i, i
                sumTime, maxTime = neededTime[i], neededTime[i]
            
        if r > l:
            res += (sumTime-maxTime)
        return res
                    

