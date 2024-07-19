# Matchsticks to Square

## Solution 1

- backtrack

- 4 sides, each time we try to put the matchsticks[i] into one side and when sides[j] + matchsticks[i] <= length, then we do backtracking. If there is one solution, then return true else keep putting.

  ![Image1](https://github.com/CarmenDou/Leetcode/blob/master/473/Image1.jpg)

  ```python
  class Solution:
      def makesquare(self, matchsticks: List[int]) -> bool:
          length = sum(matchsticks) // 4
          sides = [0] * 4
  
          if sum(matchsticks) / 4 != length:
              return False
  
          matchsticks.sort(reverse=True)
  
          def backtrack(i):
              if  i == len(matchsticks):
                  return True
  
              for j in range(4):
                  if sides[j] + matchsticks[i] <= length:
                      sides[j] += matchsticks[i]
                      if backtrack(i+1):
                          return True
                      sides[j] -= matchsticks[i]
              
              return False
  
          return backtrack(0)
          
  ```

  