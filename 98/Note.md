# Validate Binary Search Tree

## Solution 1

- DFS

  ![Image1](/Users/douwei/Desktop/Leetcode/98/Image1.jpg)

- ```python
  def valid(node, left, right):
              if not node:
                  return True
              if not (node.val < right and node.val > left):
                  return False
              return valid(node.left, left, node.val) and valid(node.right, node.val, right)
          return valid(root, float("-inf"), float("inf"))
  ```



## Solution 2 (My way)

- BFS means that preorder is sorted, therefore we use preorder to get each node and judge whether it is sorted asec.

- ```python
      		self.res = True
          self.pre = -float('inf')
          self.preorder(root)
          return self.res
      def preorder(self, root):
          if not root:
              return 
          self.preorder(root.left)
          if self.pre >= root.val:
              self.res = False
          self.pre = root.val
          self.preorder(root.right)
          
  ```

  