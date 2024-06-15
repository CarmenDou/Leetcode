class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1
        
        def helper(s):
            if s[0] == "0":
                return False
            if int(s) >= 1 and int(s) <= 26:
                return True
            return False

        dp = [0]*len(s)
        dp[0] = 1
        if not helper(s[:2]) and s[1] == "0":
            return 0
        elif helper(s[:2]) and s[1] != "0":
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, len(s)):
            tmp1, tmp2 = 0, 0
            case1 = helper(s[i])
            case2 = helper(s[i-1:i+1])
            if not case1 and not case2:
                return 0
            if case1:
                tmp1 = dp[i-1]
            if case2:
                tmp2 = dp[i-2]
            dp[i] = tmp1 + tmp2
        return dp[-1]

