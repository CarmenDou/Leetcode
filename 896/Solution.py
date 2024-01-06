class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bIncrease = False
        bDecrease = False
        lastNum = nums[0]
        for x in range(1,len(nums)) :
            if nums[x] > lastNum :
                bIncrease = True
            elif nums[x] < lastNum :
                bDecrease = True
            lastNum = nums[x]
        return not (bIncrease and bDecrease)

        