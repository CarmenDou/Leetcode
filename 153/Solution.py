class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[-1] >= nums[0]:
        #     return nums[0]
        
        # low, high = 0, len(nums)-1
        # while low < high:
        #     mid = low + (high-low)//2
        #     if nums[low] < nums[mid]:
        #         low = mid
        #     else:
        #         high = mid

        # return nums[mid+1]

        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res