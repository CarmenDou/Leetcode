# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res, self.cnt = 0, 0
        self.preorder(root, k)
        return self.res

    def preorder(self, root, k):
        if not root:
            return 
        self.preorder(root.left, k)
        if self.cnt < k:
            self.res = root.val
        self.cnt += 1
        self.preorder(root.right, k)

        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right