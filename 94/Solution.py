# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def dfs(root):
        #     nonlocal res
        #     if not root:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)

        # dfs(root)
        # return res

        res = []
        stack = []
        if not root:
            return res

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right
        return res