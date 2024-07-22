class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = 0

        def backtrack(i, subset):
            if i >= len(nums):
                if subset:
                    self.res += 1
                return 

            if self.isValid(subset, nums[i], k):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()
            backtrack(i+1, subset)
            
    
        backtrack(0, [])
        return self.res
    
    def isValid(self, subset, n, diff):
        for num in subset:
            if abs(num-n) == diff:
                return False
        return True
