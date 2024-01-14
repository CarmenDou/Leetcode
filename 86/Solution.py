# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy_A = ListNode(0)
        dummy_B = ListNode(0)
        dummy_A.next = dummy_B.next = None
        tail_A,tail_B = dummy_A,dummy_B

        while head:
            if head.val < x:
                tail_A.next = head
                head = head.next
                tail_A = tail_A.next
                tail_A.next = None
            else:
                tail_B.next = head
                head = head.next
                tail_B = tail_B.next
                tail_B.next = None

        tail_A.next = dummy_B.next

        return dummy_A.next
        