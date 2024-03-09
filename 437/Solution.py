# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # res = 0

        # def dfs(root, targetSum):
        #     if not root:
        #         return 
        #     sumOfValue(root, 0, targetSum)
        #     dfs(root.left, targetSum)
        #     dfs(root.right, targetSum)

        # def sumOfValue(root, sum, targetSum):
        #     nonlocal res
        #     if not root:
        #         return 
        #     sum += root.val
        #     if sum == targetSum:
        #         res += 1
        #     sumOfValue(root.left, sum, targetSum)
        #     sumOfValue(root.right, sum, targetSum)

        # dfs(root, targetSum)
        # return res

        if not root:
            return 0
        
        return self.helper(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)

    def helper(self,root,targetSum):
        res=0
        if not root:
            return 0
            
        targetSum -= root.val
        if targetSum == 0:
            res+=1
        res+=self.helper(root.left,targetSum)
        res+=self.helper(root.right,targetSum)

        return res
        