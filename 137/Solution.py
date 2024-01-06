from collections import Counter

class Solution():
	def singleNumber(self,nums):
		dictCount = Counter(nums)
		for key,value in dictCount.items() :
			if value == 1 :
				return key

#Leetcode bit operation
class Solution(object):
    def singleNumber(self, nums):
        a = 0; b = 0
        for i in range(len(nums)):
            b = b^nums[i] & ~a
            a = a^nums[i] & ~b

        return b


		