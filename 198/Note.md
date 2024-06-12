# House Robber

## Solution1

- Main idea: find the maximum of each of the two situations.
  - Rob the first house and the maximum from the third house to the end.
  - Skip the first house and rob from the second house to the end. 
  - We can write like this rob = max(arr[0] + rob[2:n], rob[1:n])