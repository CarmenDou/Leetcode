- 通过堆排序可以知道前k个最小的距离，heapq是默认最小堆排。

- 然后可以用字典把距离和点的对应关系记录下来。

  ```python
  import heapq
  from collections import defaultdict
  class Solution:
      def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
          heap = []
          dic = defaultdict(list)
          for point in points:
              x, y = point[0], point[1]
              square_distance = x*x + y*y
              dic[square_distance].append(point)
              heapq.heappush(heap, square_distance)
          res = []
          while k > 0:
              square_distance = heapq.heappop(heap)
              print(square_distance)
              for point in dic[square_distance]:
                  res.append(point)
              k -= len(dic[square_distance])
          return res
  
  
          
  ```

  