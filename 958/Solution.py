# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        vals = []

        def helper(root, depth):
            if not root:
                if len(vals) <= depth:
                    vals.append(["null"])
                else:
                    vals[depth].append("null")
                return
            
            if len(vals) <= depth:
                vals.append([root.val])
            else:
                vals[depth].append(root.val)

            helper(root.left, depth+1)
            helper(root.right, depth+1)     

        helper(root, 0)
        for i in range(len(vals)-1):
            if i < len(vals) -2 and "null" in vals[i]:
                return False
            
            if i == len(vals) -2:
                pre = "pre"
                for s in vals[i]:
                    if pre == "null" and s != "null":
                        return False
                    pre = s

        return True

            