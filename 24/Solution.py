
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#each time change the pairs, setting a dummy, cur and tmp point. dummy point uses to lead the whole linkedlist. tmp point uses to present the cur.next when we change the cur.next and that can make me find the node.
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        cur = dummy
        dummy.next = head
        while cur.next:
            tmp = cur.next
            if not tmp.next:
                break
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp

            cur = cur.next.next

        return dummy.next

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         pre = ListNode(0)
#         pre.next = head
#         ccur = head
#         head = pre
#         i = 0
#         while True :
#             if not ccur :
#                 return head.next
#             if not ccur.next :
#                 return head.next
#             tmp = ccur.next.next
#             ccur.next.next = ccur
#             ccur = ccur.next
#             ccur.next.next = tmp
#             pre.next = ccur
#             pre = pre.next.next
#             ccur = tmp

            

        