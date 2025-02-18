class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        def dfs(r, c, count, direction):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == ".":
                return False
            
            count += 1
            if board[r][c] == color:
                if count >= 3:
                    return True
                else:
                    return False
            else:
                dr, dc = directions[direction]
                return dfs(r+dr, c+dc, count, direction)
            
        for i in range(len(directions)):
            dr, dc = directions[i]
            if dfs(rMove+dr, cMove+dc, 1, i):
                return True
        return False