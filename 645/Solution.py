class Solution():
	def findErrorNums(self, nums):
		count = []
		for x in range(len(nums)+1):
			count.append(0)
		for x in nums:
			count[x] = count[x] + 1
		for x in range(1,len(count)):
			if count[x] > 1 :
				dup = x
			elif count[x] == 0 :
				loss = x
			
		return [dup,loss]
					
#Leetcode
class Solution(object):
    def findErrorNums(self, nums):
        res = []
        for index in nums:
            if nums[abs(index)-1]<0:
                res.append(abs(index))
            else:
                nums[abs(index)-1]*=-1
        
        for i,num in enumerate(nums):
            if num>0:
                res.append(i+1)
        
        return res

		