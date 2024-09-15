# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # aux = []
        # def helper(root):
        #     nonlocal aux
        #     if not root:
        #         return 
        #     if root.val != key:
        #         aux.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # aux.sort()
        # def convertBST(nums):
        #     if not nums:
        #         return None
        #     low, high = 0, len(nums)-1
        #     mid = (low+high)//2
        #     root = TreeNode(nums[mid])
        #     root.left = convertBST(nums[:mid])
        #     root.right = convertBST(nums[mid+1:])
        #     return root
        # return convertBST(aux)

        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root