纠正binary search tree

- 特点：中序遍历是有序的，因此如果在中序遍历时遇到倒序的节点即为错误节点

- 解题思路：定义一个self.pre指向当前节点的前驱节点，中序遍历。

  - 如果前驱节点的值 > 当前节点的值，则为错误节点，将节点复制给self.mistake1和self.mistake2。

    ```python
    				if self.pre and self.pre.val > root.val:
                if not self.mistake1:
                    self.mistake1 = self.pre
                self.mistake2 = root
            self.pre = root
    ```

    

  - 找到这两个节点后，交换错误节点值。