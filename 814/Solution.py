# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
            
        left=self.pruneTree(root.left)
        right=self.pruneTree(root.right)
        
        if left and (not left.left) and (not left.right) and (left.val==0):
            left=None
        if right and (not right.left) and (not right.right) and (right.val==0):
            right=None
        
        root.left=left
        root.right=right
        
        return root
        