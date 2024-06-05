# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):    
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r-1, c) 
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)

        return cnt

# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return  islands

# My way
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    self.dfs(grid,i,j)
                    res += 1
        
        return res

    def dfs(self,grid,i,j):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            dx = direction[0] + i
            dy = direction[1] + j
            if dx >= 0 and dy >= 0 and dx < len(grid) and dy < len(grid[0]):
                if grid[dx][dy] == "1":
                    grid[dx][dy] = "0"
                    self.dfs(grid,dx,dy)