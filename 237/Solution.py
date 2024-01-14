# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#这道题的思路比较巧妙，因为题目只给了node，我们将node.next指向它的下下个数，再把node的值变成他的下个数即可。
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # p = node
        # while p.next.next != None:
        #     p.val = p.next.val
        #     p = p.next
        # p.val = p.next.val
        # p.next = None

        if node and node.next:
            del_node=node.next
            node.next=node.next.next
            node.val=del_node.val


        
        