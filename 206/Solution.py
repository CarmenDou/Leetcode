# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next :
            return head
            
        tail = head
        ccur = head.next
        while ccur != None :
            head.next = ccur.next
            ccur.next = tail
            tail = ccur
            ccur = head.next

        return tail

        # iterative, easier to understand
        pre, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
