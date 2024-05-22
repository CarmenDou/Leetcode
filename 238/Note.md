# product of Array Except Self

## Solution 1

- Except Self means prefix nums and postfix nums, which means the result is the product of prefix times the product of postfix.

  For example,

  nums

  | 1    | 2    | 3    | 4    |
  | ---- | ---- | ---- | ---- |

  prefix(default is 1, which means the product of nums before num[0] is 1)

  | 1    | 1    | 2    | 6    |
  | ---- | ---- | ---- | ---- |

  Postfix(default is 1)

  | 24   | 12   | 4    | 1    |
  | ---- | ---- | ---- | ---- |

  ```python
  len_nums = len(nums)
  res = [1] *len_nums
  pre, post = 1, 1
  prefix, postfix = [1] *len_nums, [1] *len_nums
  for i in range(len_nums):
    prefix[i] = pre
    pre *= nums[i]
    
  for i in range(len_nums-1,-1,-1):
    postfix[i] = post
    post *= nums[i]
  
  for i in range(len_nums):
    res[i] = prefix[i]*postfix[i]
              
  return res
  ```

## Solution2

- This solution solves the follow-up: Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

- Do not use prefix and postfix arrays, use res array to store each prefix and postfix.

  ```python
  len_nums = len(nums)
  res = [1] * (len_nums)
  prefix, postfix = 1, 1
  
  for i in range(len_nums):
    res[i] = prefix
    prefix *= nums[i]
  
  for i in range(len(nums)-1,-1,-1):
    res[i] *= postfix
    postfix *= nums[i]
  
  return res 
  ```

- 