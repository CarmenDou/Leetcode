class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curMax = -float('inf'), 0
        for num in nums:
            curMax = max(num, curMax+num)
            res = max(res, curMax)
        return res