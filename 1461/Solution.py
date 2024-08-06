class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        for i in range(0, len(s)-k+1):
            res.add(s[i: i+k])
        return True if len(res) == 2**k else False