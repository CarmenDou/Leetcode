# Clone Graph

## Solution 1

- DFS

- Hashmap

  ![Image](https://github.com/CarmenDou/Leetcode/blob/master/133/Image1.jpg)

  ```python
  oldToNew = {}
  
          def dfs(node):
              if node in oldToNew:
                  return oldToNew[node]
              
              copy = Node(node.val)
              oldToNew[node] = copy
  
              for nei in node.neighbors:
                  copy.neighbors.append(dfs(nei))
              return copy
  
          return dfs(node) if node else None
          
  ```

  