# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def preorder(t):
            if not t:
                return ""
            if not t.left and not t.right:
                return str(t.val)
            elif not t.right:
                return str(t.val)+"("+preorder(t.left)+")"
            else:
                return str(t.val)+"("+preorder(t.left)+")"+"("+preorder(t.right)+")"

        res = preorder(root)
        return res