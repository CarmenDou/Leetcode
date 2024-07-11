class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        queue, visited = set(), set()
        queue.add((0, 0))
        visited.add((0, 0))
        cnt = 1
        while queue:
            if (ROWS-1, COLS-1) in queue:
                return cnt

            tmp = set()
            for r, c in queue:
                for dr, dc in directions:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in visited:
                        tmp.add((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            cnt += 1
            queue = tmp
        return -1
