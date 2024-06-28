class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # visited = set()
        # r, c = 0, 0
        # ROWS, COLS = len(matrix), len(matrix[0])
        # directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # res = []
        # dr, dc = 0, 1
        # while True:
        #     res.append(matrix[r][c])
        #     visited.add((r, c))
        #     if r+dr < 0 or r+dr >= ROWS or c+dc < 0 or c+dc >= COLS or (r+dr, c+dc) in visited:
        #         rNew, cNew = r, c
        #         for dr_new, dc_new in directions:
        #             if r+dr_new >= 0 and r+dr_new < ROWS and c+dc_new >= 0 and c+dc_new < COLS and (r+dr_new, c+dc_new) not in visited:
        #                 rNew, cNew = r+dr_new, c+dc_new
        #                 break
        #         if rNew == r and cNew == c:
        #             break
        #         dr, dc = dr_new, dc_new
        #     r, c = r+dr, c+dc
        # return res

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1 

        return res



