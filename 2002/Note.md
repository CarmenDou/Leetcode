# Maximum Product of the Length of Two palindromic Subsequences

## Solution 1

- Use bitmask to loop every possible sequence, if the sequence is palindromic, then store it in the dictionary.
  - how to get the sequence according to bitmask, we can & each bit, if mask & (1 << i), that means we choose that index, and we should add it to the sequence.
- Use two loops to traverse every two palindromic subsequences and see whether they have the same index.
  -  if m1 & m2 != 0, then they have the same index, else don't.