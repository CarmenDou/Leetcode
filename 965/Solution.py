# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    # dfs
    #     if not root:
    #         return True
    #     self.pre = root.val
    #     self.res = True
    #     self.dfs(root)
    #     return self.res

    # def dfs(self,root):
    #     if not root or not self.res:
    #         return
    #     if self.pre != root.val:
    #         self.res = False
    #     self.dfs(root.left)
    #     self.dfs(root.right)

    # #bfs
    #     if not root:
    #         return True
    #     pre = root.val
    #     queue = deque([root])
    #     while queue:
    #         node = queue.popleft()
    #         if pre != node.val:
    #             return False
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     return True
        if not root:
            return True
        return (not root.left or root.left.val==root.val) and (not root.right or root.right.val==root.val) and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

        