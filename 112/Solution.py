# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False

        if not root:
            return res

        def dfs(root,target):
            nonlocal res
            if not root:
                return 

            if root and not root.left and not root.right:
                if target - root.val == 0 :
                    res = True
                    
            dfs(root.left,target-root.val)
            dfs(root.right,target-root.val)
            
        dfs(root,targetSum)
        return res