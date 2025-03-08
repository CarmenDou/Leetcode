class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key = lambda x:x[0])
        # print(sorted_points)
        result = -float("inf")
        for i in range(1, len(sorted_points)):
            result = max(result, sorted_points[i][0]-sorted_points[i-1][0])

        return result
