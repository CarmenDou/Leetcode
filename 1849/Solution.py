class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i, nums):
            if i >= len(s) and len(nums) > 1:
                return True

            for j in range(i, len(s)):
                if (not nums) or (nums[-1] - int(s[i: j+1]) == 1):
                    nums.append(int(s[i: j+1]))
                    if dfs(j+1, nums):
                        return True
                    nums.pop()
            return False

        return dfs(0, [])

            
