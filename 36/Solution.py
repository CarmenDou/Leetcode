class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWS, COLS = len(board), len(board[0])
        # # Scan each row
        # for r in range(ROWS):
        #     tmp = {}
        #     for c in range(COLS):
        #         if not board[r][c] == ".":
        #             if board[r][c] in tmp:
        #                 return False
        #             else:
        #                 tmp[board[r][c]] = board[r][c]
        
        # # Scan each col
        # for c in range(COLS):
        #     tmp = {}
        #     for r in range(ROWS):
        #         if not board[r][c] == ".":
        #             if board[r][c] in tmp:
        #                 return False
        #             else:
        #                 tmp[board[r][c]] = board[r][c]
        
        # # Scan each nine 3 x 3 sub-boxes
        # for r in range(0,ROWS,3):
        #     for c in range(0,COLS,3):
        #         tmp = {}
        #         directions = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        #         for dr, dc in directions:
        #             if not board[r+dr][c+dc] == ".":
        #                 if board[r+dr][c+dc] in tmp:
        #                     return False
        #                 else:
        #                     tmp[board[r+dr][c+dc]] = board[r+dr][c+dc]
        # return True

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True

