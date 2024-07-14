class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))
        if len(queue) == 0 or len(queue) == ROWS * COLS:
            return -1
        
        cnt = -1
        while queue:
            tmp = []
            for r, c in queue:
                for dr, dc in directions:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in tmp:
                        grid[r+dr][c+dc] = 1
                        tmp.append((r+dr, c+dc))
            queue = tmp
            cnt += 1
        return cnt