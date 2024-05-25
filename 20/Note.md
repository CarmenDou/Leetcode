# Valid Parentheses

## Solution 1:

- Use stack, and we can use a hashmap to store the match type.

  ```python
  				stack = []
          closeToOpen = {")": "(", "]": "[", "}": "{"}
  
          for c in s:
              if c in closeToOpen:
                  if stack and stack[-1] == closeToOpen[c]:
                      stack.pop()
                  else:
                      return False
              else:
                  stack.append(c)
          
          return True if not stack else False
  ```

  