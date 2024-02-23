- 这题拆分一下思路，首先我们要知道每个子树的和，就是左子树和+右子树和+自身值。

  ```python
  def helper(root):
    if not root:
      return 0
    left=helper(root.left)
    right=helper(root.right)
    return left+right+root.val
  ```

- 然后节点左右子树的差就是我们要的结果。

  ```python
  def helper(root):
    nonlocal res
    if not root:
      return 0
    left=helper(root.left)
    right=helper(root.right)
    res += abs(left-right)
    return left+right+root.val
  ```

  