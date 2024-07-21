class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0

        def dfs(i, sChar):
            if i >= len(arr):
                self.maxLen = max(self.maxLen, len(sChar))
                return

            if self.isValid(i, arr, sChar):
                dfs(i+1, sChar+arr[i])

            dfs(i+1, sChar)

        dfs(0, "")
        return self.maxLen

    def isValid(self, j, arr, sChar):
        for s in arr[j]:
            if s in sChar:
                return False
            sChar += s
        return True
        
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0

        def dfs(i, sChar):
            if i >= len(arr):
                self.maxLen = max(self.maxLen, len(sChar))
                return

            for j in range(i, len(arr)):
                if self.isValid(j, arr, sChar):
                    dfs(j+1, sChar+arr[j])

            dfs(i+1, sChar)

        dfs(0, "")
        return self.maxLen
                
    def isValid(self, j, arr, sChar):
        for s in arr[j]:
            if s in sChar:
                return False
            sChar += s
        return True

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i+1))
        return backtrack(0)


