# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_head = list2
        while list2:
            list2_end = list2
            list2 = list2.next
        tmp1, tmp2 = list1, list1
        for i in range(a, b+2):
            tmp2 = tmp2.next
        for i in range(1, a):
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        tmp1.next = list2_head
        list2_end.next = tmp2
        return list1

        