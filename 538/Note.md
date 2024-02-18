- 这道题本质是需要我们右中左遍历，像Dr. Lu说的反转中序遍历。

  ```python
  def postorder(root):
    nonlocal sum
    if not root:
      return
    postorder(root.right)
    sum += root.val
    root.val = sum
    postorder(root.left)
  ```

  