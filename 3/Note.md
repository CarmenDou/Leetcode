# Longest Substring Without Repeating Characters

## Solution 1

- Sliding windows: use a set to store the character, and l to represent the start, when the existing character shows up, remove the character from the left until the existing character is removed.

  ```python
  				charSet = set()
          l, res = 0, 0
          for r in range(len(s)):
              while s[r] in charSet:
                  charSet.remove(s[l])
                  l += 1
              charSet.add(s[r])
              res = max(res, r-l+1)
          return res
  ```

  

