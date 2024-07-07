class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        self.flag = True
        cnt = 0

        def helper(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0:
                return
            if grid1[r][c] == 0:
                self.flag = False
            grid2[r][c] = 0
            for dr, dc in directions:
                helper(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    self.flag = True
                    helper(r, c)
                    if self.flag:
                        cnt += 1
    
        return cnt
