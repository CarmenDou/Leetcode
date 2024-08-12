class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(cnt):
            if cnt < 2:
                return -1
            res = float('inf')
            if cnt % 2 == 0:
                res = min(res, cnt/2)
            else:
                res = min(res, cnt//2+1)
            if cnt % 3 == 0:
                res = min(res, cnt/3)
            else:
                res = min(res, cnt//3+1)
            return int(res)

        count = Counter(nums)
        res = 0
        for num, cnt in count.items():
            if helper(cnt) == -1:
                return -1
            res += helper(cnt)
        return res

