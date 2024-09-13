# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next
        mid = int(cnt//2) + 1
        while mid > 1:
            head = head.next
            mid -= 1 
        return head

