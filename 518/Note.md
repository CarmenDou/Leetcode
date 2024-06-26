# Coin Change 2

## Solution 1

- 2D DP

  这个数组如coin = 1，amount = 2的数组下标是指，包含coin1，2，5达到amount = 2的可能性，那么就有两个方向，一个是只包含coin=1，然后看amount-coin既往右有多少可能性，以及往下一格（除了coin=1，能达到amount的可能性）

  ![Image](https://github.com/CarmenDou/Leetcode/blob/master/518/Image1.jpg)

  