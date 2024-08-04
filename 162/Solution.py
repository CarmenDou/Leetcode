class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l <= r:
            m = (l+r)//2
            if (m-1 < 0 or nums[m-1] < nums[m]) and (m+1 >= len(nums) or nums[m] > nums[m+1]):
                return m
            if nums[m-1] < nums[m]:
                l = m
            else:
                r = m
        
        