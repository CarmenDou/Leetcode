# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # res = False

        # def isEqual(root1,root2):
        #     if (not root1 and root2) or (root1 and not root2):
        #         return False
        #     if not root1 and not root2:
        #         return True
        #     return root1.val == root2.val and isEqual(root1.left,root2.left) and isEqual(root1.right,root2.right)

        # def dfs(root,subRoot):
        #     nonlocal res
        #     if not root:
        #         return
        #     if isEqual(root,subRoot):
        #         res = True
        #         return res
        #     dfs(root.left,subRoot)
        #     dfs(root.right,subRoot)

        # dfs(root,subRoot)
        # return res

        if not root:
            return False
        
        return self.DFS(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def DFS(self,s,t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
            
        return s.val==t.val and self.DFS(s.left,t.left) and self.DFS(s.right,t.right)
