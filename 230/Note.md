# Kth Smallest Element in a BST

## Solution 1

- stack

- ```python
  				n = 0
          stack = []
          cur = root
          while cur or stack:
              while cur:
                  stack.append(cur)
                  cur = cur.left
              cur = stack.pop()
              n += 1
              if n == k:
                  return cur.val
              cur = cur.right
  ```

## Solution 2 (My way)

- Just inorder to loop each node.

  ```python
          self.res, self.cnt = 0, 0
          self.inorder(root, k)
          return self.res
  
      def inorder(self, root, k):
          if not root:
              return 
          self.inorder(root.left, k)
          if self.cnt < k:
              self.res = root.val
          self.cnt += 1
          self.inorder(root.right, k)
  ```

  