# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        dummy = ListNode(float('inf'))
        dummy.next = head
        flag = False
        while dummy.next:
            if dummy.val not in nums and dummy.next.val in nums:
                count += 1
            dummy = dummy.next
        
        return count