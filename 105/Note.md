# Construct Binary Tree from Preorder and Inorder Traversal

## Solution 1

- ```python
  				if not preorder or not inorder:
              return None
          root = TreeNode(preorder[0])
          mid = inorder.index(preorder[0])
          root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
          root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
  
          return root
  ```

  

