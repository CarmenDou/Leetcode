class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # self.res = False
        # self.colLen = len(board[0])
        # self.rowLen = len(board)
        # self.visited = [[0 for j in range(self.colLen)] for i in range(self.rowLen)]

        # def dfs(i, j, curStr):
        #     if len(curStr) == len(word):
        #         if curStr == word:
        #             self.res = True
        #         return
        #     elif len(curStr) > len(word):
        #         return 
        #     else:
        #         if curStr != word[:len(curStr)]:
        #             return 
            
        #     if not self.visited[i][j]:
        #         self.visited[i][j] = 1
        #         if i+1 < self.rowLen:
        #             dfs(i+1, j, curStr+board[i][j])
        #         if i-1 >= 0:
        #             dfs(i-1, j, curStr+board[i][j])
        #         if j+1 < self.colLen:
        #             dfs(i, j+1, curStr+board[i][j])
        #         if j-1 >= 0:
        #             dfs(i, j-1, curStr+board[i][j])
        #         self.visited[i][j] = 0

        # if self.rowLen == 1 and self.colLen == 1:
        #     if board[0][0] == word:
        #         return True
        #     else:
        #         return False

        # for i in range(self.rowLen):
        #     for j in range(self.colLen):
        #         dfs(i, j, "")

        # return self.res

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >=ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (
                dfs(r+1, c, i+1) or 
                dfs(r-1, c, i+1) or 
                dfs(r, c+1, i+1) or 
                dfs(r, c-1, i+1)
            )
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

