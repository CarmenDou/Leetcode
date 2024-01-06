class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        while x < len(nums) :
            if nums[x] == val :
                nums.pop(x)
                x = x - 1
            x = x + 1
        return len(nums)

#Leetcode
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for num in nums :
            if num != val :
                nums[index] = num
                index += 1
        return index

        