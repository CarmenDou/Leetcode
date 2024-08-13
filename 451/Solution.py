class Solution:
    def frequencySort(self, s: str) -> str:
        countS = Counter(s)
        sorted_count = sorted(countS.items(), key = lambda x: (-x[1], x[0]))
        res = ""
        for c, cnt in sorted_count:
            res += c*cnt
        return res
