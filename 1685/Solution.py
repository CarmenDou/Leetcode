class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        preSum, postSum = [], []
        pre, post, l = 0, sum(nums), len(nums)
        res = []
        for i, num in enumerate(nums):
            preSum.append(pre)
            pre += nums[i]
            post -= nums[i]
            postSum.append(post)
        for i, num in enumerate(nums):
            res.append(num*i-preSum[i]+postSum[i]-num*(l-i-1))
        return res
