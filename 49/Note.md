# Group Anagrams

## Solution1

- Use hashmap, the key is the count of each word, the value is each word that has the same count of words.

  ```python
  res = defaultdict(list)
  for s in strs:
    count = [0] * 26
    for c in s:
      count[ord(c) - ord("a")] += 1
      # list cannot be the key of dictionary, so we have to change it to tuple.
      res[tuple(count)].append(s)
  return res.values()
  ```

  

- Time complexity: O(m*n), m means the length of list strs, n means the average size of each word.

## Solution2

- It's almost the same as Solution 1.

  ```python
  dic = defaultdict(list)
  for s in strs:
    # list cannot be the key of dictionary, so I try to change it to str.
    dic["".join(sorted(s))].append(s)
  return dic.values()
  ```

  