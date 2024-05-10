class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack=[]
        res=[]
        for i,val in enumerate(nums):
            if i>=k and i-stack[0]>=k:
                stack.pop(0)
            while stack and nums[stack[-1]]<val:
                stack.pop()
            
            stack.append(i)

            if i>k-2:
                res.append(nums[stack[0]])

        return res