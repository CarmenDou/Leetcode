class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "X":
                return 
            
            board[r][c] = "X"
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                    if board[r][c] == "O":
                        dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited:
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"