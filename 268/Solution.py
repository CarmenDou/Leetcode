class Solution():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        missingNum = len(nums)
        for x in range(0,len(nums)):
            if x != nums[x] :
                missingNum = x
                break
        return missingNum

#Leetcode
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(1,len(nums)+1) :
            x = x ^ i ^ nums[i-1]
        return x