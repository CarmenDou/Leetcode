class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, subset):
            if i < len(s) and len(subset) >= 4:
                return 

            if i >= len(s):
                if len(subset) == 4:
                    res.append(".".join(subset))
                return

            for j in range(i, len(s)):
                if self.isValid(i, j, s):
                    subset.append(s[i: j+1])
                    dfs(j+1, subset)
                    subset.pop()

        dfs(0, [])
        return res
    
    def isValid(self, i, j, s):
        if s[i] == "0" and j-i+1 > 1:
            return False
        return 0 <= int(s[i: j+1]) and int(s[i: j+1]) <= 255


