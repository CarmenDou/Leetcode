class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumArray = sum(nums)
        preSum = 0
        for index,num in enumerate(nums):
            if preSum == sumArray - preSum - num:
                return index
            preSum += num
        return -1