# Valid Palindrome

## Solution 1

- Use a new str to store the str after removing all the characters, not alpha or numbers.

  ```python
  newStr = ""
  for c in s:
    if c.isalnum():
      newStr += c.lower()
  return newStr == newStr[::-1]
  ```

  

## Solution 2

- Pointer