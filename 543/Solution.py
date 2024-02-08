# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def __init__(self):
    #     self.res = 0

    # def diameterOfBinaryTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 

    #     tmp = 0
    #     max_left = self.maxDepth(root.left)
    #     max_right = self.maxDepth(root.right)
    #     tmp = tmp + max_left + max_right
    #     self.res = max(self.res,tmp)
    #     self.diameterOfBinaryTree(root.left)
    #     self.diameterOfBinaryTree(root.right)

    #     return self.res

    # def maxDepth(self,root):
    #     if not root:
    #         return 0
    #     return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res=0
        
        def helper(root):
            nonlocal res
            
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)
            
            if root.left:
                left+=1
            if root.right:
                right+=1
            
            res=max(left+right,res)
            
            return max(left,right)
        
        helper(root)
        
        return res