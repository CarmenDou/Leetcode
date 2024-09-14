# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        firstK, endK, end = dummy, dummy, dummy
        i = 1
        while i <= k:
            end = end.next
            firstK = firstK.next
            i += 1
        while end:
            end = end.next
            endK = endK.next
        tmp = firstK.val
        firstK.val = endK.val
        endK.val = tmp
        return dummy.next
        