class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        res = [-1, -1]
        mid = helper(0, len(nums)-1)
        if mid == -1:
            return res
        else:
            start, end = mid, mid
            while start != -1:
                res[0] = start
                start = helper(0, start-1)
            while end != -1:
                res[1] = end
                end = helper(end+1, len(nums)-1)
        return res
