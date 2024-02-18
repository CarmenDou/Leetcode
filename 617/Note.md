- 比较顺畅的思路是如果root1，root2都存在就把root1.val=root1.val+root2.val。如果root1不存在就返回root2.如果root2不存在就返回root1. 然后再merge左子树和右子树

  ```python
  if root1 and root2:
    root1.val += root2.val
    if not root1:
      return root2
    if not root2:
      return root1
    root1.left = self.mergeTrees(root1.left,root2.left)
    root1.right = self.mergeTrees(root1.right,root2.right)
    return root1
  ```

  

