"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # n = len(intervals)
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if intervals[j].start > intervals[j+1].start:
        #             intervals[j], intervals[j+1] = intervals[j+1], intervals[j]

        intervals.sort(key = lambda i : i.start)            
        prevEnd = -float("inf")
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start >= prevEnd:
                prevEnd = end
            else:
                return False
        return True
