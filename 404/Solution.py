# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, bLeft, sum):
        if root:
            if not root.left and not root.right:
                if bLeft:
                    self.sum += root.val
                    return
                else:
                    return
            else:
                self.helper(root.left,True, self.sum)
                self.helper(root.right, False, self.sum)
        else:
            return 
            
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.helper(root, False, self.sum)
        return self.sum


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.sum=0
        
        def depthFirstSeach(root):
            if root is None:
                return 0
            
            leftRoot=root.left
            rightRot=root.right
            
            if root.left:    
                leftLeave_ofLeft=root.left.left
                rightLeave_ofLeft=root.left.right
                value_ofLeft=root.left.val
                if leftLeave_ofLeft == None and rightLeave_ofLeft == None:
                    self.sum+=value_ofLeft      
                    
            depthFirstSeach(leftRoot)
            depthFirstSeach(rightRot)
            
        depthFirstSeach(root)
        return self.sum

        