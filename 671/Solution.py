# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    #     self.min = [root.val,root.val]
        
    #     self.helper(root)
    #     return self.min[-1] if self.min[0] != self.min[1] else -1

    # def helper(self,root):
    #     if not root:
    #         return
                
    #     if (self.min[0] == self.min[1]) or (self.min[-1] > root.val and self.min[0] != root.val):
    #         self.min[-1] = root.val
    #     self.helper(root.left)
    #     self.helper(root.right) 
    #     

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