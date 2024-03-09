- 考察如何遍历树

-  重点是什么时候把sum加到res里，是到叶子结点再加，所以我们要判断下这个是不是叶子结点，那么就用if not root.left and not root.right去判断

  ```python
  def dfs(root, sum):
    nonlocal res
    if not root:
      return
    sum = sum*2 + root.val
    if not root.left and not root.right:
      res += sum
      dfs(root.left, sum)
      dfs(root.right, sum)
  
  ```

- 