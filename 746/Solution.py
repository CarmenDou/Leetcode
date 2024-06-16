class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tmp1, tmp2 = 0, 0
        i = 0
        while i < len(cost):
            tmp = min(tmp1+cost[i], tmp2+cost[i])
            tmp1 = tmp2
            tmp2 = tmp
            i += 1
        return min(tmp1,tmp2)