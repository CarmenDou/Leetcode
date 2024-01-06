class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxNum = 0
        # startIndex = -1
        # endIndex = -1
        # for index,num in enumerate(nums):
        #     if num == 0:
        #         if endIndex <> -1:
        #             maxNum = max(maxNum,endIndex-startIndex+1)
        #             startIndex = -1
        #             endIndex = -1
        #     else:
        #         if startIndex <> -1:
        #             endIndex = index
        #         else:
        #             startIndex = index
        #             endIndex = index
        # if endIndex <> -1:
        #     maxNum = max(maxNum,endIndex-startIndex+1)
        # return maxNum

        count = 0
        countMax = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                countMax = max(countMax,count)
                count = 0
        return max(countMax,count)