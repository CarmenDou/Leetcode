class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])  
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 
            
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][COLS-1] == 1:
                dfs(r, COLS-1)

        for c in range(COLS):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[ROWS-1][c] == 1:
                dfs(ROWS-1, c)

        landCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    landCount += 1
        return landCount

            
