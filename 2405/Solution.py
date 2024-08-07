class Solution:
    def partitionString(self, s: str) -> int:
        substr = ""
        cnt = 0
        for c in s:
            if c in substr:
                cnt += 1
                substr = ""
            substr += c
        cnt += 1
        return cnt