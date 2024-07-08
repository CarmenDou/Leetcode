from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = float("inf")
        dictS = defaultdict(list)
        for i in range(len(s)):
            dictS[s[i]].append(i)
        for key, value in dictS.items():
            if len(value) == 1:
                res = min(res, min(value))
        return res if res != float("inf") else -1

        