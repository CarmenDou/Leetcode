class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # BFS
        # use = {}
        # use[0] = 0
        # minUse = float("inf")
        # h = [0]
        # heapq.heapify(h)
        # for day in days:
        #     while h and h[0] < day:
        #         curDay = heapq.heappop(h)
        #         if day+1-1 not in use:
        #             use[day+1-1] = use[curDay] + costs[0]
        #         use[day+1-1] = min(use[day+1-1], use[curDay] + costs[0])
        #         if day+1-1 >= days[-1]:
        #             minUse = min(minUse, use[day+1-1])
        #         if day+1-1 not in h:
        #             heapq.heappush(h, day+1-1)

        #         if day+7-1 not in use:
        #             use[day+7-1] = use[curDay] + costs[1]
        #         use[day+7-1] = min(use[day+7-1], use[curDay] + costs[1])
        #         if day+7-1 >= days[-1]:
        #             minUse = min(minUse, use[day+7-1])
        #         if day+7-1 not in h:
        #             heapq.heappush(h, day+7-1)

        #         if day+30-1 not in use:
        #             use[day+30-1] = use[curDay] + costs[2]
        #         use[day+30-1] = min(use[day+30-1], use[curDay] + costs[2])
        #         if day+30-1 >= days[-1]:
        #             minUse = min(minUse, use[day+30-1])
        #         if day+30-1 not in h:
        #             heapq.heappush(h, day+30-1)
        # return minUse

        # Bottom-up DP
        dp = [0]*(len(days)+1)
        for i in reversed(range(len(days))):
            print(i)
            j = i
            dp[i] = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost+dp[j])
        return dp[0]
        