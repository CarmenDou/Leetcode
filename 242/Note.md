# Valid Anagram

## Solution1

- First sort, and then compare two sorted lists.

  ```python
  list_s = sorted(s)
  list_t = sorted(t)
  return list_s == list_t
  ```

## Solution2

- Use the dictionary to calculate all the letters in the string and compare the two dictionaries.

  ```python
  if len(s) != len(t):
    return False
  countS, countT = defaultdict(int), defaultdict(int)
  for i in range(len(s)):
    countS[s[i]] += 1
    countT[t[i]] += 1
  return countS == countT
  
  # Or in python, there is a built-in function called Counter.
  return Counter(s) == Counter(t)
  ```

## MySolution

- The same as Solution 1.

