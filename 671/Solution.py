# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        else:
            self.first_min = root.val
            self.second_min = float('inf')
            self.searchTree(root)

        return self.second_min if self.second_min != float('inf') else -1

    def searchTree(self,root):
        if not root:
            return
        
        if self.first_min != root.val and self.second_min > root.val:
            self.second_min = root.val

        self.searchTree(root.left)
        self.searchTree(root.right)
    
### 广度搜索用队列    

    if not root:
        return -1

    queue = deque()
    queue.append(root)
    min_val = root.val
    second_min = float('inf')
    found = False

    while queue:
        cur = queue.popleft()
        if cur.val > min.val and cur.val < second_min:
            second_min = cur.val
            found = True
            continue
        if not cur.left:
            continue

        queue.append(cur.left)
        queue.append()

    return second_min if found else -1