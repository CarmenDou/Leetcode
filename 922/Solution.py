# use loop to change the odd postion with even number of even position with odd number
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        while True :
            if i < len(nums) and nums[i] % 2 == 0 :
                i += 2
            if j < len(nums) and nums[j] % 2 == 1 :
                j += 2
            if i >= len(nums) or j >= len(nums) :
                break
            nums[i],nums[j] = nums[j],nums[i]
        return nums
            

# My way
# class Solution(object):
#     def sortArrayByParityII(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         auxOdd = []
#         auxEven = []
#         for i in range(len(nums)) :
#             if (i % 2 == 0 and nums[i] % 2 != 0) :
#                 auxEven.append(i)
#             if (i % 2 != 0 and nums[i] % 2 == 0) :
#                 auxOdd.append(i)

#         for i in range(len(auxOdd)) :
#             temp = nums[auxOdd[i]]
#             nums[auxOdd[i]] = nums[auxEven[i]] 
#             nums[auxEven[i]] = temp

#         return nums
        