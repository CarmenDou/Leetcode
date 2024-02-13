# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if not p and not q:
        #     return True
        # if (not p and q) or (p and not q):
        #     return False
        # q1 = deque([(p,0)])
        # q2 = deque([(q,0)])
        # while q1 and q2:
        #     cur_p, depth_p = q1.popleft()
        #     cur_q, depth_q = q2.popleft()
        #     if (cur_p.left and not cur_q.left) or (cur_p.right and not cur_q.right):
        #         return False

        #     if cur_p.val != cur_q.val:
        #         return False

        #     if cur_p.left:
        #         q1.append((cur_p.left,depth_p+1))
        #     if cur_p.right:
        #         q1.append((cur_p.right,depth_p+1))

        #     if cur_q.left:
        #         q2.append((cur_q.left,depth_q+1))
        #     if cur_q.right:
        #         q2.append((cur_q.right,depth_q+1))

        # return not q1 and not q2
        
        if p and not q:
            return False
        elif not p and q:
            return False
        elif not p and not q:
            return True
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)