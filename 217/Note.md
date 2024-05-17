# Contains Duplicate

## Solution1

- For each num, compare it to the rest of the nums and see whether there is any same num.
- Time complexity: O(n^2)
- Space complexity: O(1)

## Solution2

- First, sort the nums, then compare two consecutive nums each time and see whether they are the same.

  ```python
  nums.sort()
  for i in range(1,len(nums)):
    if nums[i-1] == nums[i]:
      return True
  return False
  ```

- Time complexity: O(nlogn) 

  - Sort: O(nlogn)
  - Compare: O(n)

- Space complexity: O(1)

## Solution3

- Use hashset.

  ```python
  hashset = set()
  for n in nums:
    if n in hashset:
      return True
    hashset.add(n)
  
  return False
  ```

- Time complexity: O(n)

- Space complexity: O(n)

## My Solution

- Use dictionary(hash map).

  ```python
  if not nums:
    return False
  dic = defaultdict(int)
  for num in nums:
    dic[num] += 1
  for key, value in dic.items():
    if value > 1:
      return True
  return False
  ```

- Time complexity: O(n)

- Space complexity: O(n)





