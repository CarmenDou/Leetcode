# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.mistake1 = None
        self.mistake2 = None
        self.inorder(root)
        self.mistake1.val, self.mistake2.val = self.mistake2.val, self.mistake1.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.mistake1:
                self.mistake1 = self.pre
            self.mistake2 = root
        self.pre = root
        self.inorder(root.right)
    
        