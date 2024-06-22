class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area, maxArea = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return
            
            self.area += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                self.area = 0
                if grid[r][c] == 1:
                    dfs(r, c)
                maxArea = max(maxArea, self.area)
        return maxArea