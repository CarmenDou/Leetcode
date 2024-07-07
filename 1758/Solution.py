class Solution:
    def minOperations(self, s: str) -> int:
        cnt1, cnt2 = 0, 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1":
                cnt1 += 1
            if i % 2 == 1 and s[i] == "0":
                cnt1 += 1
            if i % 2 == 0 and s[i] == "0":
                cnt2 += 1
            if i % 2 == 1 and s[i] == "1":
                cnt2 += 1
        return min(cnt1, cnt2)


