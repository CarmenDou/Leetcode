# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        tmp = head
        while tmp:
            while stack and stack[-1] < tmp.val:
                stack.pop()
            stack.append(tmp.val)
            tmp = tmp.next
        dummy = ListNode()
        dummy.next = head
        for val in stack:
            dummy = dummy.next
            dummy.val = val
        dummy.next = None
        return head
