# Top K Frequent Elements

## Solution1 (My solution)

- use hashmap to store the num, count the number of num, and then sort the dictionary desc and output the first k num.

  ```python
  dic = defaultdict(int)
  for num in nums:
    dic[num] += 1
    sorted_dic = sorted(dic.items(), key = lambda item: item[1], reverse=True)
    res = []
    for i in range(k):
      key, value = sorted_dic[i]
      res.append(key)
  return res
  ```