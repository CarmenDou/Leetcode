class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        len_N = len(nums)
        preN = -1
        for i in range(len_N):
            if nums[i] != preN:
                special = len_N - i
                if special <= nums[i] and preN < special:
                    return special
                preN = nums[i]
        return -1
