class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        posIndex, negIndex = 0, 1
        for num in nums:
            if num > 0 :
                res[posIndex] = num
                posIndex += 2
            else:
                res[negIndex] = num
                negIndex += 2
        return res