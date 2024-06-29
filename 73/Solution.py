class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        tmp = []
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    tmp.append((r, c))
        
        for r, c in tmp:
            visited.add((r, c))
            for i in range(ROWS):
                if (i, c) not in visited:
                    visited.add((i, c))
                    matrix[i][c] = 0
            for i in range(COLS):
                if (r, i) not in visited:
                    visited.add((r, i))
                    matrix[r][i] = 0
        return matrix

                