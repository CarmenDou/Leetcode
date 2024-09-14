# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cntNode = 0
        prev = ListNode()
        tmp = prev.next = head
        while tmp:
            cntNode += 1
            tmp = tmp.next
            prev = prev.next
        rotate = k % cntNode

        if rotate == 0:
            return head

        slow, fast = head, head
        i = 0
        while i <= rotate:
            fast = fast.next
            i += 1
        while fast:
            slow = slow.next
            fast = fast.next
        
        tmp = head
        head = slow.next
        slow.next = None
        prev.next = tmp
        return head
        