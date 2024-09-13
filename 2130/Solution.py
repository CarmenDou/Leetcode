# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        res = -float("inf")
        n = len(stack)
        mid = int(n/2)
        for i in range(mid):
            res = max(res, stack[i]+stack[n-1-i])
        return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # res = -float("inf")
        # n = len(stack)
        # mid = int(n/2)
        # for i in range(mid):
        #     res = max(res, stack[i]+stack[n-1-i])
        # return res

        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        res = 0
        while slow:
            res = max(res, prev.val+slow.val)
            prev = prev.next
            slow = slow.next
        return res
        
