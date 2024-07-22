class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.res = ""
        def dfs(i, listS):
            if i >= len(nums):
                if "".join(listS) not in nums:
                    self.res = "".join(listS)
                    return True
                else:
                    return False

            for j in range(2):
                listS.append(str(j))
                if dfs(i+1, listS):
                    return True
                listS.pop()

            return False
        
        dfs(0, [])
        return self.res
