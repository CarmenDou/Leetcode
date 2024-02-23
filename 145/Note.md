- 这道题我们要学会用迭代后序遍历，和前中遍历不同的是我们要用last_visit来判断当前节点的右节点是否被访问过，如果是的话就要pop这个节点，不是的话，就将当前节点设置为右节点。

  ```python
  class Solution:
      def postorderTraversal(self, root: TreeNode) -> List[int]:  
          res=[]
          stack=[]
          last_visit=None
          if not root:
              return res
          while stack or root:
              while root:
                  stack.append(root)
                  root=root.left
              
              cur_node=stack[-1]
              if not cur_node.right or cur_node.right==last_visit:
                  item=stack.pop()
                  res.append(item.val)
                  last_visit=item
              
              elif cur_node.right:
                  root=cur_node.right
          
          return res 
  ```

- 