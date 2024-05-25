# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # My way
        cnt = 0
        tmp = head
        while tmp:
            cnt += 1
            tmp = tmp.next
        
        tmp = head
        k = (cnt-1)//2
        while k > 0 :
            tmp = tmp.next
            k -= 1

        l = tmp.next
        tmp.next = None

        pre, curr = None, l
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt


        # Solution 1
        l = pre
        tmp1, tmp2 = l, head
        while tmp1:
            tmp = tmp1.next
            tmp1.next = tmp2.next
            tmp2.next = tmp1
            tmp1 = tmp
            tmp2 = tmp2.next.next
        return head


        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        