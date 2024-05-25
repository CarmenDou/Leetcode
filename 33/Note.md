# Search in rotated sorted array

## Solution 1

- For example,

  | 4    | 5    | 6    | 7    | 0    | 1    | 2    |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

  L						  M													R

  We can see that the left portion is sorted, if we would like to find the target from the right portion, then the target should be smaller than nums[l] or larger than nums[mid].

  | 4    | 5    | 6    | 7    | 0    | 1    | 2    |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

  L						  							M						R

  We can see that the right portion is sorted, if we would like to find the target from the left portion, then the target should be smaller than nums[mid] or larger than nums[r].

  ```python3
  						# left sorted portion
              if nums[l] <= nums[mid]:
                  if target > nums[mid] or target < nums[l]:
                      l = mid + 1
                  else:
                      r  = mid - 1
              # right sorted portion
              else:
                  if target < nums[mid] or target > nums[r]:
                      r = mid - 1
                  else:
                      l = mid + 1
  ```

  