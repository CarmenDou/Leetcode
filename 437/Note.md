1. sum-=root.val,如果sum==0,则res加1

2. 对root的左右子树进行递归，并加上res的结果

3. 返回res

   ```python
   def helper(self,root,sum_):
           res=0
           if not root:
               return 0
               
           sum_-=root.val
           if sum_==0:
               res+=1
           res+=self.helper(root.left,sum_)
           res+=self.helper(root.right,sum_)
   
           return res
   ```

   对根节点进行操作时，我们也要对root的左右节点进行递归。

   ```python
   def pathSum(self, root: TreeNode, sum: int) -> int:
   	if not root:
       return 0
     
     return self.helper(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
   ```

   