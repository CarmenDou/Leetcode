class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # DFS Time Limit Exceeded
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # visited = set()

        # def dfs(r, c, depth):
        #     if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
        #         return 
                
        #     visited.add((r, c))
        #     grid[r][c] = min(grid[r][c], depth)

        #     for dr, dc in directions:
        #         dfs(r+dr, c+dc, depth+1)
        #     visited.remove((r, c))


        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 0:
        #             dfs(r, c, 0)

        # return grid
            
        # BFS
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                   queue.append((r, c)) 
            
        curPath = 0
        while queue:
            tmp = []
            curPath += 1
            while queue:
                r, c = queue.pop()
                for dr, dc in directions:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] == 2147483647:
                        grid[r+dr][c+dc] = curPath
                        tmp.append((r+dr, c+dc))
            queue = tmp

        return grid
        
        