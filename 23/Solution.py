# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(float('inf'))
        while True:
            tmp = None
            flag = True
            for head in lists:
                if head:
                    flag = False
                    if dummy.val >= head.val:
                        tmp = head
            if tmp:
                dummy.next = tmp
                tmp = tmp.next
                dummy = dummy.next
            if flag:
                break
            print(dummy)
        return dummy.next
        