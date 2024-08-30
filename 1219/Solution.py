class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.res = 0
        def dfs(r, c, visit, cur):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                self.res = max(self.res, cur)
                return 
            
            visit.add((r, c))
            cur += grid[r][c]
            for dr, dc in directions:
                dfs(r+dr, c+dc, visit, cur)
            visit.remove((r, c))
            cur -= grid[r][c]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    dfs(r, c, set(), 0)
        return self.res

            