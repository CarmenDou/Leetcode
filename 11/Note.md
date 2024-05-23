# Container With Most Water

## Solution 1

- To maximum the area, we should try to let the height higher, so we can set two-pointer, if left is lower than move to right, if right is lower than move to left.

  ```python
  				res = 0
          l, r = 0, len(height) - 1
          while l < r :
              area = (r-l) * min(height[l],height[r])
              res = max(res,area)
  
              if height[l] < height[r]:
                  l += 1
              elif height[l] >= height[r]:
                  r -= 1
          return res
          
  ```

  