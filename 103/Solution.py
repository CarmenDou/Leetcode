# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        if not root:
            return self.result
        
        def helper(root, depth):
            if not root:
                return 
            
            if len(self.result) <= depth:
                self.result.append([root.val])
            else:
                self.result[depth].append(root.val)
            
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        
        helper(root, 0)
        for i, l in enumerate(self.result):
            if i % 2 == 1:
                self.result[i] = self.result[i][::-1]
        return self.result
        