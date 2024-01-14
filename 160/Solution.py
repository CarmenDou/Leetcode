# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p_A,p_B = headA,headB
        len_A,len_B = 0,0
        while p_A != None:
            len_A += 1
            p_A = p_A.next
        while p_B != None:
            len_B += 1
            p_B = p_B.next
        p_A,p_B = headA,headB

        if len_A > len_B:
            diff = len_A - len_B
            i = 1
            while i <= diff:
                p_A = p_A.next
                i += 1
        else:
            diff = len_B - len_A
            i = 1
            while i <= diff:
                p_B = p_B.next
                i += 1
        while p_B != None:
            if p_B == p_A:
                return p_B
            p_B = p_B.next
            p_A = p_A.next
        return None