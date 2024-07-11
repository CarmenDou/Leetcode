class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = set()
        island2 = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, island):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in island1 or (r, c) in island2 or grid[r][c] == 0:
                return

            island.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, island)
            
        i = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if i == 0:
                        dfs(r, c, island1)
                        i += 1
                    else:
                        dfs(r, c, island2)
        
        res = 0
        while True:
            tmp = set()
            for r, c in island1:
                for dr, dc in directions:
                    if (r+dr, c+dc) in island2:
                        print(r, dr, c, dc)
                        return res
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] == 0:
                        tmp.add((r+dr, c+dc))
            res += 1
            island1 = tmp