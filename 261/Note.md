# Graph Valid Tree

## Solution 1

- Tree: Do not have a loop and every node should be connected.

- ```python
  if not n:
    return True
  
  adj = {i: [] for i in range(n)}
  for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)
  
  visit = set()
  def dfs(i, prev):
    if i in visit:
      return False
    
    visit.add(i)
    for j in adj[i]:
      if j == prev:
        continue
      if not dfs(j, i):
        return False
    return True
  return dfs(0, -1) and n == len(visit)
      
  ```

  

