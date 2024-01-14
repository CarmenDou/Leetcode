# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#第一种思路 第一种思路最简单，用一个set存储已经有的节点，然后遍历head。当head在set中存在的时候就返回head。
#第二种思路 这个方法很tricky。
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while head:
            if head not in visited:
                visited.add(head)
            else:
                return head
            head = head.next

        slow,quick = head,head
        while quick:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                n = slow.next
                m = head
                while m != n:
                    m = m.next
                    n = n.next
                    return m
        return None