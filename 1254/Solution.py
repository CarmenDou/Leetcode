class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
                return 

            grid[r][c] = 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for i in range(ROWS):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][COLS-1] == 0:
                dfs(i, COLS-1)

        for i in range(COLS):
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[ROWS-1][i] == 0:
                dfs(ROWS-1, i)

        cnt = 0
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    cnt += 1

        return cnt