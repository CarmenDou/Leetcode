# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head

        h = ListNode()
        h.next = head
        p = h
        while p != None:
            while p.next != None and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return h.next


        