# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # dummy,dummy_head,tmp = ListNode(0),ListNode(0),ListNode(0)
        # dummy_head.next = head
        # tmp = dummy_head
        # n = 0
        # while tmp:
        #     if n+1 < left:
        #         tmp = tmp.next
        #     elif n+1>=left and n+1 <= right:
        #         p = tmp.next
        #         tmp.next = tmp.next.next
        #         p.next = dummy.next
        #         dummy.next = p
        #         if n+1 == left:
        #             tail = p
        #     else:
        #         break
        #     n += 1
        # tail.next = tmp.next
        # tmp.next = dummy.next

        # return dummy_head.next

###################################
        if not head:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        i=1
        
        while pre.next and i<left:
            i+=1
            pre=pre.next
            
        tail=pre
        cur=pre.next
        
        while cur.next and i<right:
            i+=1
            tmp=cur.next
            cur.next=tmp.next
            tmp.next=tail.next
            tail.next=tmp
            
        
        return dummy.next


