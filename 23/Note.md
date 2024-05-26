# Merge k Sorted Lists

## Solution 1

- Each time merge two linked-list in lists, therefore we just have to merge logk time.

- Basic operation to merge two lists.

- Time complexity: O(nlogk)

  ```python
  		def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      			
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
  ```

  

## Solution 2 (My way)

- Each time we merge a current linked-list and a new linked-list, therefore we have to merge k time.
- Basic operation to merge two lists.
- Time complexity: O(nk)