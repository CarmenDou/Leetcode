# Single Element in a Sorted Array

## Solution 1

- Leftsize means the number on the left. If it is odd, it means the number on the left; otherwise, it means the number on the right.

  ```python
  leftSize = m-1 if nums[m-1] == nums[m] else m
  if leftSize % 2:
    r = m-1
  else:
    l = m+1 
  ```

  