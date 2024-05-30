# Find Median from Data Stream

## Solution 1

- Heap
  - Small Heap (Get Max Heap Value)
  - Large Heap (Get Min Heap Value)
  - Use built-in structure: heapq(Min-Heap) and how to get Max value in Smaill Heap, we can store -1*val, and then the small[0] stores the original max value and we can get it -1 * small[0]

- Time complexity: O(logn)

  

