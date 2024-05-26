# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Solution 1
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

        # My way
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        del_node = count-n
        dummy = ListNode()
        dummy.next = head
        p = dummy
        count = 0
        while p:
            if count == del_node:
                p.next = p.next.next
            else:
                p = p.next
            count += 1
        return dummy.next