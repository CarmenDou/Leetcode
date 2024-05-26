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
        # Solution 1
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
            
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


#############################################
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
        