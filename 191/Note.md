# Number of 1 Bits

## Solution 1

- Bit manipulation

  ```python
  				cnt = 0
          while n:
              if n & 1 == 1:
                  cnt += 1
              n = n >> 1
          return cnt
  ```

  

