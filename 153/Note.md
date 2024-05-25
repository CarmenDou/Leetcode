# Find Minimum in Rotated Sorted Array

## Solution 1

- Using binary search.

  if nums[m] >= nums[l], then means from l:m it is sorted, then the smaller element is in m+1, r.

  ```python
          res = nums[0]
          l, r = 0, len(nums)-1
          while l <= r:
              if nums[l] < nums[r]:
                  res = min(res, nums[l])
                  break
  
              m = (l+r) // 2
              res = min(res, nums[m])
              if nums[m] >= nums[l]:
                  l = m + 1
              else:
                  r = m - 1
          return res
  ```

  