# Counting Bits

## Solution 1

- n & 1 and then swift to right

- Time complexity: O(nlogn)

  ```python
  				res = []
          for i in range(n+1):
              cnt = 0
              while i:
                  if i & 1 == 1:
                      cnt += 1
                  i = i >> 1
              res.append(cnt)
  
          return res
  ```

  

## Solution 2

- dp

- Time complexity: O(n)

  ![Image1](https://github.com/CarmenDou/Leetcode/blob/master/338/Image1.jpg)

  ```python
  				dp = [0] * (n+1)
          offset = 1
          for i in range(1, n+1):
              if offset * 2 == i:
                  offset = i
              dp[i] = 1 + dp[i-offset]
          return dp
  ```

  

