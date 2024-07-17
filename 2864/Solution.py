class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dictCnt = Counter(s)
        res = ""
        for i in range(dictCnt["1"]-1):
            res += "1"
        if "0" in dictCnt:
            for i in range(dictCnt["0"]):
                res += "0"
        res += "1"
        return res