# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        cnt = 1
        queue = deque([(root, root.val)])
        while queue:
            tmp = deque([])
            while queue:
                curNode, maxValue = queue.popleft()
                if curNode.left:
                    if curNode.left.val >= maxValue:
                        cnt += 1
                    tmp.append((curNode.left, max(curNode.left.val, maxValue)))
                if curNode.right:
                    if curNode.right.val >= maxValue:
                        cnt += 1
                    tmp.append((curNode.right, max(curNode.right.val, maxValue)))
            queue = tmp
        return cnt