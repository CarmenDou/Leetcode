class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        print(points)
        stack = []
        for point in points:
            if stack and point[0] <= stack[-1][1]:
                    l_start, l_end = stack.pop()
                    stack.append([point[0], min(point[1], l_end)])
            else:
                stack.append(point)
        return len(stack)
            