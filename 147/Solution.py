# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy,p,tmp = ListNode(0-float('inf')),ListNode(0-float('inf')),ListNode(0-float('inf'))
        # while head:
        #     p = dummy
        #     while p.next:
        #         if head.val <= p.next.val:
        #             tmp = head.next
        #             head.next = p.next
        #             p.next = head
        #             head = tmp
        #             break
        #         p = p.next

        #     if not p.next:
        #         tmp = head.next
        #         head.next = p.next
        #         p.next = head
        #         head = tmp

        # return dummy.next


        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        
        while cur and cur.next:
            if cur.next.val<=cur.val:
                tmp=cur.next
                cur.next=tmp.next
                pre=dummy.next
                tail=dummy
                while pre:
                    if pre.val<tmp.val:
                        pre=pre.next
                        tail=tail.next
                    else:
                        tmp.next=pre
                        tail.next=tmp
                        break
            else:
                cur=cur.next
        
        return dummy.next



        