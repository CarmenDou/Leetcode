class Solution:
    def maxScore(self, s: str) -> int:
        base = 0
        diff = -float("inf")
        cur = 0
        for i in range(len(s)):
            if s[i] == "1":
                base += 1
            if s[i] == "0" and i != len(s)-1:
                cur += 1
            if s[i] == "1" and i != len(s)-1:
                cur -= 1
            diff = max(diff, cur)
        return base+diff