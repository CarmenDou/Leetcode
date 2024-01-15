# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy,tail = ListNode(0),ListNode(0)
        dummy.next = l1
        count = 0
        while l1 and l2:
            count = count + l1.val + l2.val
            l1.val = count % 10
            count = count // 10
            tail = l1
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                count = count + l1.val
                l1.val = count % 10
                count = count // 10
                tail = l1
                l1 = l1.next

        if l2:
            tail.next = l2
            while l2:
                count = count + l2.val
                l2.val = count % 10
                count = count // 10
                tail = l2
                l2 = l2.next
        
        if count != 0:
            p = ListNode(count)
            tail.next = p
        
        return dummy.next
        