# Longest Repeating Character Replacement

## Solution 1

- Sliding Window

  We know that WindowLen - count[character] <= k results from repeating characters.

  To maximize the result, we should minimize the character number we replace, and then we should know the maximum character, therefore we use a hashmap to store. 

  And when even if we minimize the character number we replace, it still > k, then we should move the left of the sliding window to the right and minus the count of characters.

  ```python
  				count = defaultdict(int)
          res = 0
          l = 0
          for r in range(len(s)):
              count[s[r]] += 1
              while (r - l + 1) - max(count.values()) > k:
                  count[s[l]] -= 1
                  l += 1
              res = max(res, r - l + 1)
          return res
  ```

  