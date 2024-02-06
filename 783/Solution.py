# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     self.tmp = []
    #     self.dfs(root)
    #     sorted_tmp = sorted(self.tmp)
    #     res = float('inf')
    #     i = 1
    #     while i < len(sorted_tmp):
    #         if res > sorted_tmp[i] - sorted_tmp[i-1]:
    #             res = sorted_tmp[i] - sorted_tmp[i-1]
    #         i += 1
    #     return res

    # def dfs(self,root):
    #     if not root:
    #         return
    #     self.tmp.append(root.val)
    #     self.dfs(root.left)
    #     self.dfs(root.right)

### 因为是BTS
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.res=min(self.res,root.val-self.prev)
            self.prev=root.val
            dfs(root.right)
            
        self.res=float("inf")
        self.prev=float("-inf")
        dfs(root)
        return self.res