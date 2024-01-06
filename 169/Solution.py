
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countNum = Counter(nums)
        count = -1
        res = -1
        for key,value in countNum.items() :
            if value > count :
                count = value
                res = key
        return res

#Leetcode
#摩尔投票法
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        for num in nums:
            if vote == 0 :
                x = num
            if x == num :
                vote += 1
            else :
                vote -= 1
        return x
        