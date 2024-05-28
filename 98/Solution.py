# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Solution 1
        # def valid(node, left, right):
        #     if not node:
        #         return True
        #     if not (node.val < right and node.val > left):
        #         return False
        #     return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # return valid(root, float("-inf"), float("inf"))


    # Solution 2   
    #     self.res = True
    #     self.pre = -float('inf')
    #     self.preorder(root)
    #     return self.res
    # def preorder(self, root):
    #     if not root:
    #         return 
    #     self.preorder(root.left)
    #     if self.pre >= root.val:
    #         self.res = False
    #     self.pre = root.val
    #     self.preorder(root.right)
        