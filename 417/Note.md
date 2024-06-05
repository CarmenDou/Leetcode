# Pacific Atlantic Water Flow

## Solution 1

- DFS

  - From every grid which near the ocean to other girds

  - return function:

    ```python
    if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                    return
    ```

    

