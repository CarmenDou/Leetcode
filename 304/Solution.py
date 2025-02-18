class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.space = [[0 for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            sumRow = 0
            for c in range(COLS):
                sumRow += matrix[r][c]
                if r > 0:
                    self.space[r][c] = self.space[r-1][c] + sumRow
                else:
                    self.space[r][c] = sumRow
        return 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1-1 < 0 and col1-1 >= 0:
            return self.space[row2][col2] - self.space[row2][col1-1]
        if row1-1 < 0 and col1-1 < 0:
            return self.space[row2][col2]
        if row1-1 >= 0 and col1-1 < 0:
            return self.space[row2][col2] - self.space[row1-1][col2]
        if row1-1 >= 0 and col1-1 >= 0:
            return self.space[row2][col2] - self.space[row1-1][col2] - self.space[row2][col1-1] + self.space[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)