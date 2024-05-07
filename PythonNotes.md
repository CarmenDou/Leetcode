

# 数据结构

## 字典

- dict.keys()和dict.values()

  得到key的数组或者value的数组

## 列表

- remove方法可以移除元素
- sort方法是对List本身排序，所以返回值为Null

# 函数

## 排序

### Sorted

- Lambda

  默认升序，- 则降序

  例如：

  ```python
  from collections import defaultdict
  class Solution:
      def topKFrequent(self, words: List[str], k: int) -> List[str]:
          dic = defaultdict(int)
          for word in words:
              dic[word] += 1
          sort_dic = sorted(dic.items(),key = lambda x : (-x[1],x[0]))[:k]
          return [ string for string, count in sort_dic]  
  ```

- str类型的sorted

  排序后是数组

  ```python
  str = "123"
  print(sorted(str))
  #[1,2,3]
  ```

  

## Math 

### Trunc

返回x 截断整数的部分,即返回整数部分,忽略小数部分。

```python
math.trunc(x/10)
```



# 包

## collections

### defaultdict

- defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，默认为None。它覆盖一个方法并添加一个可写实例变量。

- defaultdict其他功能与dict相同，但会为一个不存在的键**提供默认值，如int,set,str,list函数等**，从而避免KeyError异常。

  举例1：int作为初始化函数参数

  ```python
  from collections import defaultdict
  s = "mississippi"
  d = defaultdict(int)
  for k in s:
  	d[k] += 1
  print(d)
  ```

  举例2：set作为初始化函数参数

  ```python
  from collections import defaultdict
  s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
  d = defaultdict(set)
  for k, v in s:
      d[k].add(v)
  print(d)
  ```

## Heapq

heapq默认是最小顶堆

1. Heappush(heap,n)数据堆入

   ```python
   import heapq
   array = [10,17,50,7,30,24,27,45,15,5,36,21]
   heap = []
   for num in array:
     heapq.heappush(heap, num)
   print("array", array)
   print("heap:", heap)
   
   array: [10,17,50,7,30,24,27,45,15,5,36,21]
   heap: [5,7,21,15,10,24,27,45,17,30,36,50]
   ```

2.  Heappop(heap)将数组堆中的最小元素弹出

   ```python
   heapq.heappop(heap)
   5
   ```

3.  

4. 

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
                
        return heapq.heappop(heap)
```



# 算法

## Backtracking

Reference: https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/#1313

```python
def backtrack(state: State, choices: list[choice], res: list[state]):
    """回溯算法框架"""
    # 判断是否为解
    if is_solution(state):
        # 记录解
        record_solution(state, res)
        # 不再继续搜索
        return
    # 遍历所有选择
    for choice in choices:
        # 剪枝：判断选择是否合法
        if is_valid(state, choice):
            # 尝试：做出选择，更新状态
            make_choice(state, choice)
            backtrack(state, choices, res)
            # 回退：撤销选择，恢复到之前的状态
            undo_choice(state, choice)
```

 

## BFS

Deque可以用元祖存每层的值和层级，比如：

```python
queue = deque([(root,0)])
while queue:
  node, depth = queue.popleft()
  if node.left:
    queue.append((node.left,depth+1))
 	if node.right:
    queue.append((node.right,depth+1))
```

# 排序

## 堆排序

堆结构：首先必须满足完全二叉树的定义，每个结点的值都大于或者等于左右孩子结点的值，称为大顶堆，注意没有要求节点的左孩子的值和右孩子的值的大小关系；相反每个结点的值都小于或者等于其左右孩子结点的值，称为小顶堆。

大顶堆特点：arr[i] >= arr[2*i+1] && arr[i] >= arr[2*i+2]

小顶堆特点：arr[i] <= arr[2*i+1] && arr[i] <= arr[2*i+2]

一般升序采用大顶堆，降序采用小顶堆

时间复杂度：O(nlogn)

基本思想：将带排序序列构造成一个大顶堆，这个时候整个序列的最大值就是堆顶的根结点；然后将其与末尾元素交换，此时末尾就是最大值，这部分是有序区。

然后将剩下的n-1个元素重新构造成一个堆，重复执行就能过的到一个有序序列。

# Github提交步骤

1. 提交步骤

   ```bash
   git add .
   git commit -m $(date +%F) 
   git push origin master
   ```

   
