# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion好难，我又哭了 这道题需要考虑整个左子树和整个右子树。
# 如果左子树或者右子树不存在就判断左右子树是否相等。相反返回True，不相等返回False。
# 如果左右子树存在且值不相等，就返回False。
# 如果左子树和右子树都存在且值相等则递归判断左子树的右子树与右子树的左子树，左子树的左子树与右子树的右子树。
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.mirror(root.left,root.right)

    def mirror(self, left, right):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        else:
            return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
            