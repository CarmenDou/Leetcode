# Insert Interval

## Solution 1

- Case 1
  - newInterval[1] < intervals[i][0]
    - res.append(newInterval)
    - return res + intervals[i:]
- Case 2
  - newInterval[0] > intervals[i][1]
    - res.append(intervals[i])
- Case 3
  - newInterval and intervals have junctions
    - newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]

