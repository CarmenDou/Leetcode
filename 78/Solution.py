class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def helper(index, res, nums, path):
            if index > len(nums):
                return 

            res.append(path)
            for i in range(index, len(nums)):
                helper(i+1, res, nums, path+[nums[i]])

        helper(0, res, nums, path)
        return res
