# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        index = 0
        while index < len(preorder):
            if preorder[index] > root.val:
                break
            index += 1
        root.left = self.bstFromPreorder(preorder[:index])
        root.right = self.bstFromPreorder(preorder[index:])
        return root