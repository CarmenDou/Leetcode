# Longest Consecutive Sequence

## Solution1

- For example:

  | 100  | 4    | 200  | 1    | 3    | 2    |
  | ---- | ---- | ---- | ---- | ---- | ---- |

  We can see that there are three sequences:

  | 1    | 2    | 3    | 4    |
  | ---- | ---- | ---- | ---- |

  | 100  |
  | ---- |

  | 200  |
  | ---- |

  And how to define a sequence start, that is there is not a number before it, which means there is not 0 before 1. And since we define a start, and then we can keep finding whether there is a number after it to make the sequence longer. The worse time complexity is the array is reverse and each number will be visited twice. Therefore, the time complexity is O(n).

- Time complexity: O(n)

  ```python
  numSet = set(nums)
  longest = 0
  
  for n in nums:
    #check if its the start of a sequnce
    if (n-1) not in numSet:
      length = 0
      while (n+length) in numSet:
        length += 1
        longest = max(length, longest)
  return longest
  ```

  