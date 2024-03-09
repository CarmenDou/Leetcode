# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, sum):
            nonlocal res
            if not root:
                return 
            sum = sum*2 + root.val
            if not root.left and not root.right:
                res += sum
            dfs(root.left, sum)
            dfs(root.right, sum)

        dfs(root, 0)
        return res
        

        