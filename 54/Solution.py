class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        r, c = 0, 0
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        dr, dc = 0, 1
        while True:
            res.append(matrix[r][c])
            visited.add((r, c))
            if r+dr < 0 or r+dr >= ROWS or c+dc < 0 or c+dc >= COLS or (r+dr, c+dc) in visited:
                rNew, cNew = r, c
                for dr_new, dc_new in directions:
                    if r+dr_new >= 0 and r+dr_new < ROWS and c+dc_new >= 0 and c+dc_new < COLS and (r+dr_new, c+dc_new) not in visited:
                        rNew, cNew = r+dr_new, c+dc_new
                        break
                if rNew == r and cNew == c:
                    break
                dr, dc = dr_new, dc_new
            r, c = r+dr, c+dc
        return res



