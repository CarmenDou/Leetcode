# Two Sum

## Solution1

- Using hashmap, we can see whether target - num is in hashmap, if so, then return the index.

  ```python
  prevMap = {} # val: index
  for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff],i]
    prevMap[n] = i
  ```

## Solution2

- Just Bruce searches, for each num to see whether there is another num that can be added to the target.

  ```python
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums[j] == target:
        return [i,j]
  ```

  