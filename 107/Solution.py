# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append((root,1))
        tmp = []
        last_depth = 1
        while queue:
            cur_node,depth = queue.popleft()
            if cur_node.left:
                queue.append((cur_node.left,depth+1))
            if cur_node.right:
                queue.append((cur_node.right,depth+1))
            if last_depth == depth:
                tmp.append(cur_node.val)
            else:
                last_depth = depth
                res.append(tmp)
                tmp = [cur_node.val] 
            
        if tmp:
            res.append(tmp)
            
        return res[::-1]
        