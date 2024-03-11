# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # target = val

        # def dfs(root):
        #     nonlocal target 
        #     if not root:
        #         return 

        #     if root.val > target:
        #         if root.left:
        #             dfs(root.left)
        #         else:
        #             root.left = TreeNode(target)
        #     else:
        #         if root.right:
        #             dfs(root.right)
        #         else:
        #             root.right = TreeNode(target)

        #     if not root.left and not root.right:
        #         if root.val >= target:
        #             root.left = TreeNode(val)
        #         else:
        #             root.right = TreeNode(val)
        #         return 

        # if not root:
        #     return TreeNode(val)
        # dfs(root)
        # return root


        if not root:
            return TreeNode(val)
        
        def helper(root,val):
            if not root:
                return
            
            if not root.left and val<root.val:
                root.left=TreeNode(val)
                return
            if not root.right and val>root.val:
                root.right=TreeNode(val)
                return
            
            if val<root.val:
                helper(root.left,val)
            else :
                helper(root.right,val)
                
            return root
        
        helper(root,val)
        return root

