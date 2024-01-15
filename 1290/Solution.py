# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # count = 0
        # while head:
        #     count = count * 2 + head.val
        #     head = head.next
        # return count

        c=""
        temp=head
        while(temp!=None):
            c+=str(temp.val)
            temp=temp.next
        x= int(c,2)
        return x
        