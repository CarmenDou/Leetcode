# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 

        def findMax(nums):
            res = 0
            index = 0
            for i, num in enumerate(nums):
                if num > res:
                    res = num
                    index = i
            return(res,index)

        num, index = findMax(nums)
        root = TreeNode(num)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 

        ori_nums = nums[:]
        nums.sort(reverse=True)
        index = ori_nums.index(nums[0])
        root = TreeNode(nums[0])
        root.left = self.constructMaximumBinaryTree(ori_nums[0:index])
        root.right = self.constructMaximumBinaryTree(ori_nums[index+1:])
        return root

        