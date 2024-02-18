# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0

        def postorder(root):
            nonlocal sum
            if not root:
                return 
            postorder(root.right)
            sum += root.val
            root.val = sum
            postorder(root.left)

        postorder(root)
        return root

        