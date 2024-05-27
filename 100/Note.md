# Same Tree

## Solution 1

- Recursive

- DFS

- Time complexity: O(p+q)

  ```python
  				if not p and not q:
              return True
          elif (not p and q) or (p and not q):
              return False
  
          return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  ```

  

