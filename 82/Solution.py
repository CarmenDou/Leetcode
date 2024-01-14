# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dic = {}
        # tmp = head
        # while tmp:
        #     if tmp.val in dic:
        #         dic[tmp.val] += 1
        #     else:
        #         dic[tmp.val] = 1
        #     tmp = tmp.next
        # dummy = ListNode(0)
        # dummy.next = head
        # tmp = dummy
        # while tmp.next:
        #     if dic[tmp.next.val] >= 2:
        #         tmp.next = tmp.next.next
        #     else:
        #         tmp = tmp.next
        # return dummy.next

#如果遇到前后两个node的值一样，那我们就用value储存这个node的值。然后跳过之后有相同值的node。我们要注意最后一个node的存在，最后一个node是要被跳过还是保留。
        if not head:
            return head
        
        dummy = ListNode(0)
        tail = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                value = cur.val
                while cur and cur.val == value:
                    cur = cur.next
            else:
                tail.next = cur
                tail = tail.next
                cur = cur.next
        
        if cur:
            tail.next = cur
        else:
            tail.next = None
    
        return dummy.next
        

        