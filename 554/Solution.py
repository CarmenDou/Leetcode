class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = []
        ROWS = len(wall)
        for r in range(ROWS):
            sum = 0
            for c in range(len(wall[r])-1):
                sum += wall[r][c]
                count.append(sum)
        dicCount = Counter(count)
        if not dicCount:
            return ROWS
        sort_dicCount = sorted(dicCount.values())
        return ROWS - sort_dicCount[-1]