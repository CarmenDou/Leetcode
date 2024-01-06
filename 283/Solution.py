class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)) :
            if nums[i] == 0 :
                if index == -1 :
                    index = i
            else :
                if index != -1 :
                    nums[index] = nums[i]
                    nums[i] = 0
                    index = index + 1
            
        return nums