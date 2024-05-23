# 3Sum

## Solution 1

- First, sort the array, and then loop each element, and then the question comes to 2 sum problem, if the sum is larger than the target then move the right point to the left, if the sum is smaller than the target, then move left point to the right, if the sum is equal to target, then keep moving left point to right until it does not equal to the pre num.

- Time complexity: O(nlogn) for sort, O(n^2) for loop, therefore is O(n^2)

  ```python
  				res = []
          nums.sort()
  
          for i, a in enumerate(nums):
              if i > 0 and a == nums[i-1]:
                  continue
              l, r = i+1 ,len(nums)-1
              while l < r:
                  threeSum =  a + nums[l] + nums[r]
                  if threeSum > 0:
                      r-= 1
                  elif threeSum < 0:
                      l += 1
                  else:
                      res.append([a, nums[l], nums[r]])
                      l += 1
                      while nums[l] == nums[l-1] and l < r:
                          l += 1
          return res
  ```

  