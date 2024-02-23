# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
###递归遍历
        if not root:
            return
        def helper(root,res):
            if not root:
                return
            res.append(root.val)
            helper(root.left,res)
            helper(root.right,res)
            return res
        
        return helper(root,[])

###循环遍历
        res = []
        if not root:
            return res
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            
            cur_node = stack.pop()
            root = cur_node.right
        
        return res