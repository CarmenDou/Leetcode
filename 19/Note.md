# Remove Nth Node From End of List

## Solution 1

- Two pointer

  L - R distances are equal to Nth, but because we want to remove the Nth node, we must create a dummy point to head, where L starts.

  ```python
  				dummy = ListNode(0, head)
          left = dummy
          right = head
          while n > 0 and right:
              right = right.next
              n -= 1
          while right:
              left = left.next
              right = right.next
          left.next = left.next.next
          return dummy.next
  ```

  