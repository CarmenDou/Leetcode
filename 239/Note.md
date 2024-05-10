### 找区间内的最大值

- 维护一个递减栈

  - 如果栈的长度大于窗口长度的话，栈底元素出栈。

    ```python
    if i>=k and i-stack[0]>=k:
      stack.pop(0)
    # i>=k是防止一开始stack为空时out of range
    ```

  - 维护递减栈代码

    ```python
    while stack and nums[stack[-1]]<val:
      stack.pop()
    ```

    

- 然后将栈底元素append到res里。

  ```python
  if i>k-2:
    res.append(nums[stack[0]])
  # i>k-2是因为从到了下标为k-1的时候才开始考虑第一波slide的最大值是多少
  ```

  

