"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        while len(intervals) > 1:
            tmp = []
            intervals.sort(key = lambda i : i.start)
            prevInterval = Interval(-float("inf"), -float("inf"))
            for interval in intervals:
                if interval.start >= prevInterval.end:
                    prevInterval = interval
                else:
                    if prevInterval.end < interval.end:
                        tmp.append(interval)
                    else:
                        tmp.append(prevInterval)
                        prevInterval = interval
            res += 1
            intervals = tmp
        return res + len(intervals)
