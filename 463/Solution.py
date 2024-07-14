class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def helper(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 1
            else:
                return 0
        
        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        perimeter += helper(r+dr, c+dc)
        return perimeter

