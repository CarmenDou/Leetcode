# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#我们同样可以设快慢两个指针,快指针比慢指针每次多走一步。如果存在环，那快慢两个指针必将相遇，即quick==slow。
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        quick,slow = head,head
        while quick and slow and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False
