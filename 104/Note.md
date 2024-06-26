# Maximum Depth of Binary Tree

## Solution 1

- DFS

- Recursive

  ```python
  				if not root:
              return 0
          return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
  ```

## Solution 2

- BFS

- Using queue

  ```python
  				if not root:
              return 0
          
          level = 0
          q = deque([root])
          while q:
              for i in range(len(q)):
                  node = q.popleft()
                  if node.left:
                      q.append(node.left)
                  if node.right:
                      q.append(node.right)
              level += 1
          return level
  ```

## Solution 3

- DFS

- Iterative

  ```python
  				if not root:
              return 0
          stack = [[root,1]]
          res = 0
          
          while stack:
              node, depth = stack.pop()
              if node:
                  res = max(res, depth)
                  stack.append([node.left, depth+1])
                  stack.append([node.right, depth+1])
          return res
  
  ```

  