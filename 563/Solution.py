# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        # if not root:
        #     return res

        # def update_val(root):
        #     nonlocal res
        #     if not root:
        #         return 
        #     root.val = abs(sum_subtree(root.left) - sum_subtree(root.right))
        #     res += root.val
        #     if root.left:
        #         update_val(root.left)
        #     if root.right:
        #         update_val(root.right)

        #     return 

        # def sum_subtree(root):
        #     if not root:
        #         return 0
        #     return root.val + sum_subtree(root.left) + sum_subtree(root.right)
        
        # update_val(root)
        # return res
            
        def helper(root):
            nonlocal res
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            res += abs(left-right)
            return left + right + root.val

        helper(root)
        return res