class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # res = 0
        # intervals.sort(key = lambda i : i[0])
        # newInterval = [-float("inf"),-float("inf")]
        # for i in range(len(intervals)):
        #     if newInterval[1] <= intervals[i][0]:
        #         newInterval = intervals[i]
        #     else:
        #         if newInterval[1] > intervals[i][1]:
        #             newInterval = intervals[i]
        #         res += 1
        # return res
        
        intervals.sort()
        res = 0
        prevEnd = -float("inf")
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res