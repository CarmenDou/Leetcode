# Linked List Cycle

## Solution 1

- Set a slow and fast two-pointer, the fast pointer will catch up with the slow pointer.

  ```python
  				slow, fast = head, head
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
              if slow == fast:
                  return True
          return False
  ```

  