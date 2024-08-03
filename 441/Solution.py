class Solution:
    def arrangeCoins(self, n: int) -> int:
        res, cnt = 0, 0
        while True:
            if cnt >= n:
                break
            res += 1
            cnt += res
        return res-1 if cnt > n else res
