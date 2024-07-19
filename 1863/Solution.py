class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def backtrack(i, xorTotal):
            if i >= len(nums):
                self.res += xorTotal
                return
            
            tmp = xorTotal ^ nums[i]
            backtrack(i+1, tmp)
            backtrack(i+1, xorTotal)
        
        backtrack(0, 0)

        return self.res

