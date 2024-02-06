# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        self.searchTree(root,low,high)
        return self.sum

    def searchTree(self,root,low,high):
        if not root:
            return 

        if root.val >= low and root.val <= high:
            self.sum += root.val

        self.searchTree(root.left,low,high)
        self.searchTree(root.right,low,high)
    
####recursion
def rangeSumBST(self, root, low, high):
        res=0
        if not root:
            return res
        if root.val>=low and root.val<=high:
            res+=root.val
        res+= self.rangeSumBST(root.left,low,high)
        res+= self.rangeSumBST(root.right,low,high)
        
        return res
        