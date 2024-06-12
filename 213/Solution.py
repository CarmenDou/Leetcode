class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) <= 2:
        #     return max(nums[0],nums[1])
        
        # dp = [0]*len(nums)
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # dp2 = [0]*len(nums)
        # dp2[1], dp2[2] = nums[1], max(nums[1], nums[2]) 
        # for i in range(2, len(nums)):
        #     dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        #     if i > 2:
        #         dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1])
        
        # dp[-1] = max(dp[-2], dp2[-1])
        # return dp[-1]

        # [rob1, rob2, n, n+1]
        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                newRob = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))