# Binary Tree Maximum Path Sum

## Solution 1

- For each node, considering as the top node what is the leftMax and what is the rightMax.

- We would like to know what is the maximum sum we can get with the path running from 3, updating the result.

- What's the value I would like to update to my parent, we don't want to split twice, looking for my left child and right child, and get the maximum of leftMax and rightMax

  ![Image1](https://github.com/CarmenDou/Leetcode/tree/master/100/Image1.jpg)

  ```python
  				def dfs(root):
              if not root:
                  return 0
  
              leftMax = dfs(root.left)
              rightMax = dfs(root.right)
              leftMax = max(leftMax, 0)
              rightMax = max(rightMax, 0)
  
              # complete max path sum with split
              res[0] = max(res[0], root.val + leftMax + rightMax)
  
              return root.val + max(leftMax, rightMax)
  ```

  