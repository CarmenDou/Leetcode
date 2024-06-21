from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i in range(len(s)):
            lastIndex[s[i]] = i
        res = []
        cnt, curLastIndex = 0, 0
        for i in range(len(s)):
            if i <= curLastIndex:
                cnt += 1
            else:
                res.append(cnt)
                cnt = 1
            curLastIndex = max(curLastIndex, lastIndex[s[i]])
        res.append(cnt)
        return res