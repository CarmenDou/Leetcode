# Reorder List

## Solution 1

- Split the linked list into two parts, reverse the second, and insert it into the first. 

- How could we know which is the first part and which is the second part, we can use a slow and fast pointer.

  ```python3
          slow, fast = head, head.next
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
  
          second = slow.next
          prev = slow.next = None
  ```

  

