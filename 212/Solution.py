class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # res = []
        # path = set()
        # ROW, COL = len(board), len(board[0])

        # def dfs(r, c, s):
        #     if (r, c) in path or r < 0 or r >= ROW or c < 0 or c >= COL:
        #         if s in words and s not in res:
        #             res.append(s) 
        #         return
            
        #     path.add((r,c))
        #     dfs(r-1, c, s+board[r][c])
        #     dfs(r+1, c, s+board[r][c])
        #     dfs(r, c-1, s+board[r][c])
        #     dfs(r, c+1, s+board[r][c])
        #     path.remove((r,c))

        # for r in range(ROW):
        #     for c in range(COL):
        #         dfs(r, c, "")
        
        # return res

        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
