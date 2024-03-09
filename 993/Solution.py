# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return 
        queue = []
        queue.append(root)
        while queue:
            tmp = []
            xFlag = False
            yFlag = False
            while queue:
                cur = queue.pop()
                if cur.left and cur.right:
                    if (cur.left.val  == x and cur.right.val == y) or (cur.left.val  == y and cur.right.val == x):
                        return False
                if cur.left:
                    tmp.append(cur.left)
                    if cur.left.val == x:
                        xFlag = True
                    if cur.left.val == y:
                        yFlag = True
                if cur.right:
                    tmp.append(cur.right)
                    if cur.right.val == x:
                        xFlag = True
                    if cur.right.val == y:
                        yFlag = True
            
            queue = tmp
            if xFlag and yFlag:
                return True
        return False


