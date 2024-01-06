class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        if len(nums) < 2 :
            return res
        else:
            if nums[0] > nums[1]:
                larNum = nums[0]
                larNumIndex = 0
                seclarNum = nums[1]
            else:
                larNum = nums[1]
                larNumIndex = 1
                seclarNum = nums[0]
            for i in range(2,len(nums)):
                if nums[i] <= seclarNum:
                    pass
                elif nums[i] > seclarNum and nums[i] < larNum:
                    seclarNum = nums[i]
                elif nums[i] > larNum:
                    seclarNum = larNum
                    larNum = nums[i]
                    larNumIndex = i
            if seclarNum * 2 <= larNum:
                res = larNumIndex
            return res

class Solution(object):
    def dominantIndex(self, nums):
        large,se_large=0,0
        pos=-1
        
        for index,num in enumerate(nums):
            if num>large:
                large=num
                pos=index
        
        for num in nums:
            if num!=large:
                se_large=max(num,se_large)
        
        if se_large*2<=large:
            return pos
        else:
            return -1
        