# Encode and Decode Strings

## Solution1

- Record the length of each str and use a # to insert before the true str like below, and then when decoding, just read the length and get the str.

  ```python
  class Solution:
  
      def encode(self, strs: List[str]) -> str:
          res = ""
          for s in strs:
              res += str(len(s)) + "#" + s
          return res
      def decode(self, s: str) -> List[str]:
          res,i = [], 0
          while i < len(s):
              j = i
              while s[j] != "#":
                  j += 1
              length = int(s[i:j])
              res.append(s[j+1: j+1+length])
              i = j+1+length
          return res
  ```

  

