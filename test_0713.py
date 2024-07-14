class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        nMap, n = {}, len(board)
        for i in range(1, n**2+1):
            r = n-1-int((i-1)/n)
            if (r % 2 == 0 and n % 2 == 0) or (r % 2 != 0 and n % 2 != 0):
                c = n-1-(i-1)%n
            else:
                c = (i-1)%n
            nMap[i] = (r, c)
        # print(nMap)
        step = 0
        visited, cur = set(), set()
        visited.add(1)
        cur.add(1)
        j = 0
        while cur:
            if n**2 in cur:
                return step
            tmp = set()
            for p in cur:
                for q in range(p + 1, min(p + 6, n**2)+1):
                    r, c = nMap[q]
                    if board[r][c] == -1 and board[r][c] not in visited:
                        tmp.add(q)
                        visited.add(q)
                    if board[r][c] != -1 and board[r][c] not in visited:
                        tmp.add(board[r][c])
                        visited.add(board[r][c])
            cur = tmp
            step += 1
            j += 1
            print(cur, visited)
        return -1