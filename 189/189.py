class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        aux = nums[0:len(nums)-k]
        del nums[0:len(nums)-k]
        nums = nums.extend(aux)

# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         while k > 0 :
#             aux = nums[len(nums)-1]
#             nums.pop(len(nums)-1)
#             nums.insert(0,aux)
#             k -= 1

# Note:
# We have to pay attention to the base operation of list.
# 1) For one element
#         a）insert/append
#         b)  pop/remove
# 3) For a part of elements
#         a)  extend
#         b)  del