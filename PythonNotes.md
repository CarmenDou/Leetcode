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

  

- 

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