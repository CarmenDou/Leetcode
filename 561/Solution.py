class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for index,num in enumerate(nums):
            if index % 2 == 0:
                res += num
        return res
        