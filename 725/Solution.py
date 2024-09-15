# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next
        diff, base = cnt%k, cnt//k
        tmp = head
        i, j = 0, 1
        res = []
        partHead = cur = head
        while cur:
            if (i < diff and j < base+1) or (i >=diff and j < base):
                cur = cur.next
                j += 1
            else:
                tmp = cur.next
                cur.next = None
                res.append(partHead)
                cur = tmp
                partHead = cur
                i += 1
                j = 1
        while i < k:
            res.append(None)
            i += 1
        return res

