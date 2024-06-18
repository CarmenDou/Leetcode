class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visit = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                (i, j) = (r, c)
                tmp1 = matrix[i][j]
                while (i, j) not in visit:
                    # value
                    visit.add((i, j))
                    tmp2 = matrix[j][COLS-1-i]
                    matrix[j][COLS-1-i] = tmp1
                    tmp1 = tmp2
                    # index
                    tmp3 = i
                    i = j
                    j = COLS-1-tmp3
        
        # print(matrix)
        return matrix
        