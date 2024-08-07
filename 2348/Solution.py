from collections import defaultdict
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt, res = 0, 0
        zeroLenth = defaultdict(int)
        for num in nums:
            if num == 0:
                cnt += 1
            elif num != 0 and cnt != 0:
                zeroLenth[cnt] += 1
                cnt = 0
            else:
                pass
        if cnt != 0:
            zeroLenth[cnt] += 1

        for key, value in zeroLenth.items():
            res += (1+key)*key*value/2
        return int(res)
