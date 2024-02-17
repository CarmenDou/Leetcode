# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.newTree = TreeNode()
        self.cur = self.newTree
        self.dfs(root)
        return self.newTree.right

    def dfs(self,root):
        if not root:
            return 

        self.dfs(root.left)
        tmp = TreeNode(root.val)
        self.cur.right = tmp
        self.cur = self.cur.right
        self.dfs(root.right)

    ### do not assign extra space
        dummy = cur = TreeNode(None)
        
        def inordertree(root):
            nonlocal cur
            if root:
                inordertree(root.left)
                root.left=None
                cur.right=root
                cur=cur.right
                inordertree(root.right)
        
        inordertree(root)
        return dummy.right