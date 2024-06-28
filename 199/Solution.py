# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        queue = deque([root])
        res = []
        while queue:
            tmp = deque([])
            while queue:
                curNode = queue.popleft()
                if curNode.left:
                    tmp.append(curNode.left)
                if curNode.right:
                    tmp.append(curNode.right)
            res.append(curNode.val)
            queue = tmp
        return res
        
            