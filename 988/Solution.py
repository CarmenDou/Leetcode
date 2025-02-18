# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        letter = [""]*26
        for i in range(26):
            letter[i] = chr(ord('a')+i)
        self.result = ""
        def dfs(root, paths):
            if not root:
                return
            paths.appendleft(letter[root.val])
            if not root.left and not root.right:
                if not self.result or self.result > "".join(paths):
                    self.result = "".join(paths)
            dfs(root.left, paths)
            dfs(root.right, paths)
            paths.popleft()

        dfs(root, deque([]))
        return self.result
            