class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        l = len(nums)-1
        dp = set()
        dp.add(nums[l])
        i = l-1
        while i >= 0:
            tmp = dp.copy()
            for n in dp:
                tmp.add(n+nums[i])
            dp = tmp.copy()
            i -= 1
        
        return True if target in dp else False